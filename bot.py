# -*- coding: utf-8 -*-
"""
Telegram Group Voice Music Player
Single-file desktop GUI.

Install:
    python -m pip install -U telethon py-tgcalls

Windows/Linux:
    python telegram_music_player.py

Notes:
- API ID / API Hash and normal settings are saved in config.json.
- Telegram login session is saved in telegram_session.session.
- The 2FA password is NOT saved to disk.
- The session file is effectively a login credential. Keep it private.
"""

import asyncio
import json
import os
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

try:
    from telethon import TelegramClient, functions, types
    from telethon.errors import (
        ApiIdInvalidError,
        AuthRestartError,
        FloodWaitError,
        PasswordHashInvalidError,
        PhoneCodeExpiredError,
        PhoneCodeInvalidError,
        PhoneNumberInvalidError,
        SessionPasswordNeededError,
    )
    from pytgcalls import PyTgCalls
    from pytgcalls.types import GroupCallConfig
except ImportError as exc:
    raise SystemExit(
        "Missing package. Install with:\n"
        "python -m pip install -U telethon py-tgcalls\n\n"
        f"Import error: {exc}"
    )


APP_DIR = Path(__file__).resolve().parent
CONFIG_FILE = APP_DIR / "config.json"
SESSION_FILE = APP_DIR / "telegram_session"
MAX_GROUPS = 100


def load_config():
    if not CONFIG_FILE.exists():
        return {
            "api_id": "",
            "api_hash": "",
            "phone": "",
            "songs": [],
            "last_song": "",
            "last_group": "",
        }

    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Invalid config")
    except Exception:
        return {
            "api_id": "",
            "api_hash": "",
            "phone": "",
            "songs": [],
            "last_song": "",
            "last_group": "",
        }

    data.setdefault("songs", [])
    data.setdefault("last_song", "")
    data.setdefault("last_group", "")
    return data


def save_config(data):
    CONFIG_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


class TelegramEngine:
    """Runs Telethon + PyTgCalls inside one dedicated asyncio thread."""

    def __init__(self, notify):
        self.notify = notify
        self.loop = None
        self.thread = None
        self.client = None
        self.calls = None

        self.api_id = None
        self.api_hash = None
        self.phone = None
        self.phone_code_hash = None

        self.authorized = False
        self.waiting_for_code = False
        self.waiting_for_password = False
        self.current_group = None

    def start_thread(self):
        self.thread = threading.Thread(
            target=self._thread_main,
            daemon=True,
            name="telegram-async",
        )
        self.thread.start()

    def _thread_main(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_forever()
        finally:
            pending = asyncio.all_tasks(self.loop)
            for task in pending:
                task.cancel()
            if pending:
                self.loop.run_until_complete(
                    asyncio.gather(*pending, return_exceptions=True)
                )
            self.loop.close()

    def submit(self, coro):
        if not self.loop:
            raise RuntimeError("Async loop is not ready")
        return asyncio.run_coroutine_threadsafe(coro, self.loop)

    async def begin_login(self, api_id, api_hash, phone):
        try:
            self.api_id = int(api_id)
            self.api_hash = api_hash.strip()
            self.phone = phone.strip()

            if self.api_id <= 0 or not self.api_hash or not self.phone:
                raise ValueError("API ID, API Hash and phone are required.")

            self.client = TelegramClient(
                str(SESSION_FILE),
                self.api_id,
                self.api_hash,
            )

            await self.client.connect()

            if await self.client.is_user_authorized():
                await self.finish_runtime()
                me = await self.client.get_me()
                self.notify(
                    "authorized",
                    f"Connected as {me.first_name or ''} "
                    f"{me.last_name or ''}".strip(),
                )
                return

            sent = await self.client.send_code_request(self.phone)
            self.phone_code_hash = sent.phone_code_hash
            self.waiting_for_code = True
            self.waiting_for_password = False
            self.notify(
                "code_needed",
                "Login code sent to your Telegram account.",
            )

        except (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            AuthRestartError,
        ) as exc:
            await self._disconnect_safely()
            self.notify("error", str(exc))
        except Exception as exc:
            await self._disconnect_safely()
            self.notify("error", f"{type(exc).__name__}: {exc}")

    async def submit_code(self, code):
        if not self.client:
            self.notify("error", "Telegram client is not initialized.")
            return

        try:
            await self.client.sign_in(
                phone=self.phone,
                code=code.strip(),
                phone_code_hash=self.phone_code_hash,
            )
            self.waiting_for_code = False
            await self.finish_runtime()
            me = await self.client.get_me()
            self.notify(
                "authorized",
                f"Connected as {me.first_name or ''} "
                f"{me.last_name or ''}".strip(),
            )

        except SessionPasswordNeededError:
            self.waiting_for_code = False
            self.waiting_for_password = True
            self.notify(
                "password_needed",
                "Telegram 2FA password is required.",
            )
        except (PhoneCodeInvalidError, PhoneCodeExpiredError) as exc:
            self.notify("login_error", str(exc))
        except Exception as exc:
            self.notify("error", f"{type(exc).__name__}: {exc}")

    async def submit_password(self, password):
        if not self.client:
            self.notify("error", "Telegram client is not initialized.")
            return

        try:
            await self.client.sign_in(password=password)
            self.waiting_for_password = False
            await self.finish_runtime()
            me = await self.client.get_me()
            self.notify(
                "authorized",
                f"Connected as {me.first_name or ''} "
                f"{me.last_name or ''}".strip(),
            )
        except PasswordHashInvalidError:
            self.notify("login_error", "Wrong 2FA password.")
        except Exception as exc:
            self.notify("error", f"{type(exc).__name__}: {exc}")

    async def finish_runtime(self):
        if self.calls is None:
            self.calls = PyTgCalls(self.client)
            # Current PyTgCalls exposes an async start() method.
            await self.calls.start()

        self.authorized = True

    async def fetch_groups(self):
        if not self.client or not self.authorized:
            raise RuntimeError("Not logged in.")

        groups = []
        count = 0

        async for dialog in self.client.iter_dialogs():
            entity = dialog.entity

            is_basic_group = isinstance(entity, types.Chat)
            is_megagroup = (
                isinstance(entity, types.Channel)
                and bool(getattr(entity, "megagroup", False))
            )

            if not (is_basic_group or is_megagroup):
                continue

            active = False
            try:
                if is_basic_group:
                    full = await self.client(
                        functions.messages.GetFullChatRequest(entity.id)
                    )
                else:
                    full = await self.client(
                        functions.channels.GetFullChannelRequest(entity)
                    )

                active = getattr(full.full_chat, "call", None) is not None
            except FloodWaitError as exc:
                # Don't turn a refresh into an account lockout.
                self.notify(
                    "status",
                    f"Telegram asked us to slow down for {exc.seconds}s.",
                )
                active = False
            except Exception:
                active = False

            groups.append(
                {
                    "id": int(dialog.id),
                    "title": dialog.name or str(dialog.id),
                    "active": active,
                }
            )

            count += 1
            if count >= MAX_GROUPS:
                break

        groups.sort(
            key=lambda x: (
                not x["active"],
                x["title"].casefold(),
            )
        )
        return groups

    async def refresh_one_group_status(self, group_id):
        """Fresh active check just before playback."""
        entity = await self.client.get_entity(group_id)

        if isinstance(entity, types.Chat):
            full = await self.client(
                functions.messages.GetFullChatRequest(entity.id)
            )
        elif isinstance(entity, types.Channel) and getattr(
            entity, "megagroup", False
        ):
            full = await self.client(
                functions.channels.GetFullChannelRequest(entity)
            )
        else:
            return False

        return getattr(full.full_chat, "call", None) is not None

    async def play_song(self, group_id, song_path):
        if not self.client or not self.calls or not self.authorized:
            raise RuntimeError("Not logged in.")

        if not Path(song_path).is_file():
            raise FileNotFoundError(song_path)

        # Do not create a new Voice Chat. Only play when one is active.
        active = await self.refresh_one_group_status(group_id)
        if not active:
            raise RuntimeError(
                "This group does not currently have an active Voice Chat."
            )

        config = GroupCallConfig(auto_start=False)
        await self.calls.play(
            int(group_id),
            str(song_path),
            config=config,
        )
        self.current_group = int(group_id)

    async def stop_song(self, group_id):
        if not self.calls:
            return
        await self.calls.leave_call(int(group_id))
        if self.current_group == int(group_id):
            self.current_group = None

    async def pause_song(self, group_id):
        if self.calls:
            await self.calls.pause(int(group_id))

    async def resume_song(self, group_id):
        if self.calls:
            await self.calls.resume(int(group_id))

    async def disconnect(self):
        try:
            if self.calls and self.current_group is not None:
                try:
                    await self.calls.leave_call(self.current_group)
                except Exception:
                    pass
            self.current_group = None
        finally:
            await self._disconnect_safely()

    async def _disconnect_safely(self):
        try:
            if self.client:
                await self.client.disconnect()
        except Exception:
            pass
        self.authorized = False


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Telegram Voice Music Player")
        self.geometry("1040x680")
        self.minsize(900, 600)

        self.config_data = load_config()
        self.groups = []
        self.group_ids = {}
        self.current_song = None
        self.current_group = None

        self.engine = TelegramEngine(self.engine_notify)
        self.engine.start_thread()

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.build_login()
        self.after(150, self.try_saved_login)

    # ---------- UI helpers ----------

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def set_status(self, text, error=False):
        self.status_var.set(text)
        self.status_label.configure(
            foreground=("#c62828" if error else "#256029")
        )

    def build_login(self):
        self.clear()

        root = ttk.Frame(self, padding=30)
        root.pack(fill="both", expand=True)

        card = ttk.Frame(root, padding=30)
        card.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(
            card,
            text="Telegram Music Player",
            font=("Segoe UI", 23, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=(0, 24))

        ttk.Label(
            card,
            text="API ID",
        ).grid(row=1, column=0, sticky="w", pady=7)

        self.api_id_var = tk.StringVar(
            value=str(self.config_data.get("api_id", ""))
        )
        ttk.Entry(
            card,
            textvariable=self.api_id_var,
            width=42,
        ).grid(row=1, column=1, pady=7, padx=(15, 0))

        ttk.Label(
            card,
            text="API Hash",
        ).grid(row=2, column=0, sticky="w", pady=7)

        self.api_hash_var = tk.StringVar(
            value=self.config_data.get("api_hash", "")
        )
        ttk.Entry(
            card,
            textvariable=self.api_hash_var,
            width=42,
            show="*",
        ).grid(row=2, column=1, pady=7, padx=(15, 0))

        ttk.Label(
            card,
            text="Phone",
        ).grid(row=3, column=0, sticky="w", pady=7)

        self.phone_var = tk.StringVar(
            value=self.config_data.get("phone", "")
        )
        ttk.Entry(
            card,
            textvariable=self.phone_var,
            width=42,
        ).grid(row=3, column=1, pady=7, padx=(15, 0))

        ttk.Button(
            card,
            text="Login",
            command=self.start_login,
        ).grid(row=4, column=0, columnspan=2, pady=(20, 8), ipadx=35)

        self.login_help = ttk.Label(
            card,
            text=(
                "Telegram will send the login code to your account.\n"
                "2FA password will be requested only when needed."
            ),
            justify="center",
        )
        self.login_help.grid(row=5, column=0, columnspan=2, pady=(12, 0))

        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            card,
            textvariable=self.status_var,
            anchor="center",
        )
        self.status_label.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=(18, 0),
        )

    def build_code_popup(self, password=False):
        popup = tk.Toplevel(self)
        popup.title("Telegram Login")
        popup.geometry("380x210")
        popup.transient(self)
        popup.grab_set()
        popup.resizable(False, False)

        title = (
            "Two-Factor Authentication"
            if password
            else "Telegram Login Code"
        )
        prompt = (
            "Enter your Telegram 2FA password:"
            if password
            else "Enter the code sent by Telegram:"
        )

        frame = ttk.Frame(popup, padding=25)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=title,
            font=("Segoe UI", 15, "bold"),
        ).pack(pady=(0, 15))

        ttk.Label(frame, text=prompt).pack()

        var = tk.StringVar()
        entry = ttk.Entry(
            frame,
            textvariable=var,
            width=35,
            show="*" if password else "",
        )
        entry.pack(pady=12)
        entry.focus_set()

        def submit():
            value = var.get().strip()
            if not value:
                return

            popup.grab_release()
            popup.destroy()

            if password:
                self.submit_password(value)
            else:
                self.submit_code(value)

        ttk.Button(
            frame,
            text="Continue",
            command=submit,
        ).pack()

        entry.bind("<Return>", lambda _event: submit())
        popup.protocol("WM_DELETE_WINDOW", popup.destroy)

    def build_main(self, account_text):
        self.clear()

        outer = ttk.Frame(self, padding=12)
        outer.pack(fill="both", expand=True)

        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 10))

        ttk.Label(
            header,
            text="Telegram Music Player",
            font=("Segoe UI", 20, "bold"),
        ).pack(side="left")

        ttk.Label(
            header,
            text=account_text,
        ).pack(side="right")

        body = ttk.Panedwindow(outer, orient="horizontal")
        body.pack(fill="both", expand=True)

        # Songs pane
        left = ttk.Frame(body, padding=10)
        body.add(left, weight=1)

        ttk.Label(
            left,
            text="Music Library",
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w")

        song_buttons = ttk.Frame(left)
        song_buttons.pack(fill="x", pady=8)

        ttk.Button(
            song_buttons,
            text="Add Songs",
            command=self.add_songs,
        ).pack(side="left")

        ttk.Button(
            song_buttons,
            text="Remove",
            command=self.remove_song,
        ).pack(side="left", padx=6)

        self.song_list = tk.Listbox(left)
        self.song_list.pack(fill="both", expand=True)

        # Groups pane
        right = ttk.Frame(body, padding=10)
        body.add(right, weight=1)

        titlebar = ttk.Frame(right)
        titlebar.pack(fill="x")

        ttk.Label(
            titlebar,
            text="Groups / Voice Chats",
            font=("Segoe UI", 14, "bold"),
        ).pack(side="left")

        ttk.Button(
            titlebar,
            text="Refresh",
            command=self.refresh_groups,
        ).pack(side="right")

        self.group_tree = ttk.Treeview(
            right,
            columns=("name", "status"),
            show="headings",
            height=18,
        )
        self.group_tree.heading("name", text="Group")
        self.group_tree.heading("status", text="Voice Chat")
        self.group_tree.column("name", width=350)
        self.group_tree.column("status", width=120, anchor="center")
        self.group_tree.pack(fill="both", expand=True, pady=(8, 10))

        controls = ttk.Frame(right)
        controls.pack(fill="x")

        ttk.Button(
            controls,
            text="▶ Play",
            command=self.play_selected,
        ).pack(side="left")

        ttk.Button(
            controls,
            text="⏸ Pause",
            command=self.pause_selected,
        ).pack(side="left", padx=6)

        ttk.Button(
            controls,
            text="▶ Resume",
            command=self.resume_selected,
        ).pack(side="left")

        ttk.Button(
            controls,
            text="■ Stop",
            command=self.stop_selected,
        ).pack(side="left", padx=6)

        self.now_playing_var = tk.StringVar(value="Nothing playing")
        ttk.Label(
            right,
            textvariable=self.now_playing_var,
            relief="groove",
            padding=8,
        ).pack(fill="x", pady=(12, 0))

        self.status_var = tk.StringVar(value="Loading…")
        self.status_label = ttk.Label(
            outer,
            textvariable=self.status_var,
            anchor="w",
        )
        self.status_label.pack(fill="x", pady=(8, 0))

        self.load_songs_into_ui()
        self.restore_last_selection()

        self.after(200, self.refresh_groups)

    # ---------- Login ----------

    def start_login(self):
        api_id = self.api_id_var.get().strip()
        api_hash = self.api_hash_var.get().strip()
        phone = self.phone_var.get().strip()

        if not api_id or not api_hash or not phone:
            messagebox.showwarning(
                "Missing data",
                "API ID, API Hash and phone are required.",
            )
            return

        self.config_data["api_id"] = api_id
        self.config_data["api_hash"] = api_hash
        self.config_data["phone"] = phone
        save_config(self.config_data)

        self.set_status("Connecting to Telegram…")

        future = self.engine.submit(
            self.engine.begin_login(api_id, api_hash, phone)
        )
        future.add_done_callback(self.future_error)

    def try_saved_login(self):
        api_id = str(self.config_data.get("api_id", "")).strip()
        api_hash = str(self.config_data.get("api_hash", "")).strip()
        phone = str(self.config_data.get("phone", "")).strip()

        # Saved session may already be authorized.
        if api_id and api_hash and phone and SESSION_FILE.with_suffix(
            ".session"
        ).exists():
            self.set_status("Checking saved Telegram session…")

            future = self.engine.submit(
                self.engine.begin_login(api_id, api_hash, phone)
            )
            future.add_done_callback(self.future_error)

    def submit_code(self, code):
        self.set_status("Checking login code…")
        future = self.engine.submit(self.engine.submit_code(code))
        future.add_done_callback(self.future_error)

    def submit_password(self, password):
        self.set_status("Checking 2FA password…")
        future = self.engine.submit(
            self.engine.submit_password(password)
        )
        future.add_done_callback(self.future_error)

    def engine_notify(self, kind, value):
        self.after(0, lambda: self.handle_engine_event(kind, value))

    def handle_engine_event(self, kind, value):
        if kind == "code_needed":
            self.set_status(value)
            self.build_code_popup(password=False)

        elif kind == "password_needed":
            self.set_status(value)
            self.build_code_popup(password=True)

        elif kind == "authorized":
            self.set_status(value)
            self.current_song = None
            self.build_main(value)

        elif kind == "login_error":
            self.set_status(value, error=True)
            messagebox.showerror("Telegram Login", value)

        elif kind == "error":
            self.set_status(value, error=True)
            messagebox.showerror("Error", value)

        elif kind == "status":
            self.set_status(value)

    def future_error(self, future):
        try:
            future.result()
        except Exception as exc:
            self.after(
                0,
                lambda: self.handle_engine_event(
                    "error",
                    f"{type(exc).__name__}: {exc}",
                ),
            )

    # ---------- Songs ----------

    def get_song_paths(self):
        return list(self.config_data.get("songs", []))

    def save_song_state(self):
        self.config_data["songs"] = self.get_song_paths()
        self.config_data["last_song"] = self.current_song or ""
        self.config_data["last_group"] = (
            str(self.current_group) if self.current_group else ""
        )
        save_config(self.config_data)

    def load_songs_into_ui(self):
        if not hasattr(self, "song_list"):
            return

        self.song_list.delete(0, tk.END)
        valid = []

        for path in self.get_song_paths():
            p = Path(path)
            if p.is_file():
                valid.append(str(p))
                self.song_list.insert(tk.END, p.name)

        if valid != self.get_song_paths():
            self.config_data["songs"] = valid
            save_config(self.config_data)

    def add_songs(self):
        paths = filedialog.askopenfilenames(
            title="Select audio files",
            filetypes=[
                (
                    "Audio",
                    "*.mp3 *.m4a *.aac *.wav *.ogg *.opus *.flac",
                ),
                ("All files", "*.*"),
            ],
        )

        if not paths:
            return

        songs = self.get_song_paths()

        for path in paths:
            path = str(Path(path).resolve())
            if path not in songs:
                songs.append(path)

        self.config_data["songs"] = songs
        save_config(self.config_data)
        self.load_songs_into_ui()

    def remove_song(self):
        selection = self.song_list.curselection()
        if not selection:
            return

        index = selection[0]
        songs = self.get_song_paths()

        if index >= len(songs):
            return

        removed = songs.pop(index)
        if removed == self.current_song:
            self.current_song = None

        self.config_data["songs"] = songs
        self.save_song_state()
        self.load_songs_into_ui()

    def selected_song(self):
        selection = self.song_list.curselection()
        if not selection:
            if self.current_song:
                return self.current_song
            return None

        index = selection[0]
        songs = self.get_song_paths()

        if 0 <= index < len(songs):
            return songs[index]

        return None

    def restore_last_selection(self):
        last_song = self.config_data.get("last_song", "")
        songs = self.get_song_paths()

        if last_song in songs:
            index = songs.index(last_song)
            self.song_list.selection_set(index)
            self.song_list.see(index)
            self.current_song = last_song

    # ---------- Groups ----------

    def refresh_groups(self):
        self.set_status("Refreshing groups and active Voice Chats…")
        future = self.engine.submit(self.engine.fetch_groups())
        future.add_done_callback(self.groups_done)

    def groups_done(self, future):
        try:
            groups = future.result()
        except Exception as exc:
            self.after(
                0,
                lambda: self.handle_engine_event(
                    "error",
                    f"Could not load groups: {exc}",
                ),
            )
            return

        self.after(0, lambda: self.show_groups(groups))

    def show_groups(self, groups):
        self.groups = groups
        self.group_ids.clear()

        for item in self.group_tree.get_children():
            self.group_tree.delete(item)

        for group in groups:
            status = "ACTIVE" if group["active"] else "offline"
            iid = str(group["id"])
            self.group_ids[iid] = group["id"]
            self.group_tree.insert(
                "",
                "end",
                iid=iid,
                values=(group["title"], status),
            )

        self.set_status(
            f"{len(groups)} groups loaded. "
            "Playback only starts in an active Voice Chat."
        )

        last_group = str(self.config_data.get("last_group", ""))
        if last_group in self.group_ids:
            self.group_tree.selection_set(last_group)
            self.group_tree.see(last_group)

    def selected_group(self):
        selection = self.group_tree.selection()
        if not selection:
            return None

        iid = selection[0]
        return self.group_ids.get(iid)

    # ---------- Playback ----------

    def play_selected(self):
        song = self.selected_song()
        group_id = self.selected_group()

        if not song:
            messagebox.showwarning("Music", "Choose a song first.")
            return

        if group_id is None:
            messagebox.showwarning("Group", "Choose a group first.")
            return

        self.current_song = song
        self.current_group = group_id
        self.save_song_state()

        self.set_status("Checking Voice Chat and starting playback…")

        future = self.engine.submit(
            self.engine.play_song(group_id, song)
        )
        future.add_done_callback(self.play_done)

    def play_done(self, future):
        try:
            future.result()
        except Exception as exc:
            self.after(
                0,
                lambda: self.handle_engine_event(
                    "error",
                    f"Playback failed: {type(exc).__name__}: {exc}",
                ),
            )
            return

        self.after(0, self.playback_started)

    def playback_started(self):
        title = Path(self.current_song).name if self.current_song else "-"
        self.now_playing_var.set(
            f"Playing: {title}"
        )
        self.set_status(
            "Song is playing in the selected Telegram Voice Chat."
        )

    def stop_selected(self):
        group_id = self.selected_group() or self.current_group

        if group_id is None:
            return

        future = self.engine.submit(
            self.engine.stop_song(group_id)
        )
        future.add_done_callback(self.simple_action_done)

    def pause_selected(self):
        group_id = self.selected_group() or self.current_group

        if group_id is None:
            return

        future = self.engine.submit(
            self.engine.pause_song(group_id)
        )
        future.add_done_callback(self.simple_action_done)

    def resume_selected(self):
        group_id = self.selected_group() or self.current_group

        if group_id is None:
            return

        future = self.engine.submit(
            self.engine.resume_song(group_id)
        )
        future.add_done_callback(self.simple_action_done)

    def simple_action_done(self, future):
        try:
            future.result()
            self.after(0, lambda: self.set_status("Done."))
        except Exception as exc:
            self.after(
                0,
                lambda: self.handle_engine_event(
                    "error",
                    f"{type(exc).__name__}: {exc}",
                ),
            )

    # ---------- Shutdown ----------

    def on_close(self):
        try:
            self.save_song_state()
        except Exception:
            pass

        try:
            if self.engine.loop:
                future = self.engine.submit(self.engine.disconnect())
                try:
                    future.result(timeout=5)
                except Exception:
                    pass
                self.engine.loop.call_soon_threadsafe(
                    self.engine.loop.stop
                )
        except Exception:
            pass

        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
