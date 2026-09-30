from ntpath import join
from pyrogram import (
    Client,
    filters,
    idle
)
import asyncio

from youtubesearchpython import VideosSearch

from pyrogram.errors.exceptions.bad_request_400 import MessageEmpty, MessageTooLong, UserNotParticipant,ChatAdminRequired, ChannelInvalid, MediaEmpty
from pyrogram.types.bots_and_keyboards.callback_query import CallbackQuery
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup
from pyrogram.raw.functions.phone import CreateGroupCall,DiscardGroupCall
from pyrogram.raw.types import GroupCall
from pyrogram.raw.types import InputGroupCall
# from pyrogram.raw.base import InputGroupCall
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums

from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPrivileges,
)

from pyromod import listen

import time, sqlite3, random, aiocron, requests, json, os, re, sys

from pytgcalls import StreamType
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.video_parameters import VideoParameters


import jdatetime
jdatetime.set_locale('fa_IR')


sys.dont_write_bytecode = True

mersad = 8310874437 12345 #ادیت
sudo = 7252911263 #ادیت
path85 = '/root/Ad/Hd1/downloads/'
print('Please Insert a Token First !\nThen Insert a Phone Number !\n\n')

API_ID = 21054083 #ادیت
API_HASH = '5091465e23c1c3f653a55c4411db6500' #ادیت هلپر هستش

# uvloop.install()

api = Client(
    name="MusicPlayer",
    api_id = API_ID,
    api_hash = API_HASH
)

cli = Client(
    name="Cli",
    api_id = API_ID,
    api_hash = API_HASH,
    device_model='Mersad'
)
call_py = PyTgCalls(cli)

db = sqlite3.connect('database.sqlite')
cur = db.cursor()

async def utub(link):
    proc = await asyncio.create_subprocess_exec(
        'youtube-dl',
        '-g',
        '-f',
        'best[height<=?720][width<=?1280]',
        f'{link}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return stdout.decode().split('\n')[0]

cur.execute('''CREATE TABLE IF NOT EXISTS gp(
    namegp TEXT,
    idgp BIGINT,
    linkgp TEXT,
    status INT(20)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS charge(
    idgp BIGINT,
    idadmin BIGINT,
    day INT(20),
    start BIGINT,
    end BIGINT,
    status INT(10),
    link TEXT,
    name TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS charge2(
    idgp BIGINT,
    idadmin BIGINT,
    day INT(20),
    start BIGINT,
    end BIGINT,
    status INT(10),
    link TEXT,
    name TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS information(
    id INT AUTO_INCREMENT PRIMARY_KEY,
    start TEXT,
    about TEXT,
    groupp TEXT,
    adminpv TEXT,
    payamresan TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS users(
    iduser BIGINT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS videoadmins(
    idgp BIGINT,
    idadmin BIGINT,
    nameadmin TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS musicadmin(
    idgp BIGINT,
    idadmin BIGINT,
    nameadmin TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS sudo(
    idsudo BIGINT,
    namesudo TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS owner(
    idowner BIGINT,
    nameowner TEXT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS alll(
    idsadmin BIGINT,
    namesadmin TEXT,
    status INT(20)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS channel(
    idchannel BIGINT,
    namechannel TEXT,
    invite TEXT,
    status INT(20)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS limmit(
    status INT(20),
    count INT(20)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS autoleft(
    status INT(20)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS creators(
    idgp BIGINT,
    creator BIGINT
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS playlist(
    idgp BIGINT,
    path TEXT,
    duration INT(10)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS money1(
    kos INT(20),
    nerkh1 INT(20),
    nerkh2 INT(20)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS paye(
    kos INT(20),
    nerkh INT(20)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS etebar(
    kos INT(20),
    start INT(200),
    end INT(200),
    status INT(20)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS chnl(
    idchnl INT(20),
    start INT(200),
    end INT(200),
    statuschnl INT(20),
    status INT(20)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS ejbar(
    idgp INT(20),
    idadmin INT(20)    
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS startcli(
    start TEXT    
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS banlist(
    idgp BIGINT,
    ban BIGINT
)''')
db.commit()

# if os.path.isfile('chnl.txt'):
#     pass
# else:
#     os.system('touch chnl.txt')

cur.execute('SELECT * FROM information WHERE id=1')
check_exists = cur.fetchone()
if check_exists == None:
    try:
        cur.execute('''INSERT INTO
            information(id,start,about,groupp,adminpv,payamresan)
            VALUES(1,"START","ABOUT","+NFHJK4757FDSDF","bdchvjndchvj","dbgchjnebdh")''') #ادیت
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute('''INSERT INTO
            information(id,start,about,groupp,adminpv,payamresan)
            VALUES(1,"START","ABOUT","+NFHJK4757FDSDF","bdchvjndchvj","dbgchjnebdh")''') #ادیت
    db.commit()

cur.execute('SELECT * FROM money1')
if cur.fetchall() == []:
    query = 'INSERT INTO money1(kos,nerkh1,nerkh2) VALUES(?,?,?)'
    try:
        cur.execute(query, (1,10000,25000))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (1,10000,25000))
    db.commit()
    query = 'INSERT INTO money1(kos,nerkh1,nerkh2) VALUES(?,?,?)'
    try:
        cur.execute(query, (2,15000,30000))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (2,15000,30000))
    db.commit()

cur.execute('SELECT * FROM startcli')
if cur.fetchall() == []:
    query = 'INSERT INTO startcli(start) VALUES(?)'
    try:
        cur.execute(query, ('Hi MENTION',))
    except sqlite3.OperationalError :
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, ('Hi MENTION',))
    db.commit()

cur.execute('SELECT * FROM paye')
if cur.fetchall() == []:
    query = 'INSERT INTO paye(kos,nerkh) VALUES(?,?)'
    try:
        cur.execute(query, (1,50000))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (1,50000))
    db.commit()


########################################################################################################
playing = {}
playlis = {}
########################################################################################################

def idsudos():
    lis = []
    cur.execute('SELECT * FROM sudo')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])
    return lis

def idowner():
    lis = []
    cur.execute('SELECT * FROM owner')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])
    return lis

def idmusic(chat_id):
    lis = []
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[1])
    return lis

def idvideo(chat_id):
    lis = []
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[1])
    return lis

def allvideo():
    lis = []
    cur.execute('SELECT * FROM alll WHERE status=1')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])
    return lis

def allmusic():
    lis = []
    cur.execute('SELECT * FROM alll WHERE status=0')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])
    return lis

def creators(chat_id):
    lis = []
    cur.execute(f'SELECT * FROM creators WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[1])
    return lis

def readusers():
    lis = []
    cur.execute('SELECT * FROM users')
    for i in cur.fetchall():
        lis.append(i[0])
    return lis

def gpmusic():
    lis = []
    cur.execute('SELECT * FROM charge')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

def gpvideo():
    lis = []
    cur.execute('SELECT * FROM charge2')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

def insmusic():
    lis = []
    cur.execute('SELECT * FROM gp WHERE status=0')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

def insvideo():
    lis = []
    cur.execute('SELECT * FROM gp WHERE status=1')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

def moz(status:int):
    lis = []
    cur.execute(f'SELECT * FROM charge WHERE status={status}')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

def kir(status:int):
    lis = []
    cur.execute(f'SELECT * FROM charge2 WHERE status={status}')
    x = cur.fetchall()
    if x == []:
        return []
    for i in x:
        lis.append(i[0])

    return lis

########################################################################################################

########################################################################################################

async def checkjoin(c:Client, m:Message, user_id):
    list_moaf = []
    cur.execute(f'SELECT * FROM ejbar WHERE idgp={m.chat.id}')
    x = cur.fetchall()
    if x == []:
        pass
    else:
        for i in x:
            list_moaf.append(i[1])
    if user_id in list_moaf:
        return None
    cur.execute('SELECT * FROM channel')
    x = cur.fetchall()
    aa = [InlineKeyboardButton(text='▪️ کانال ما',url=f"{x[0][2]}")]
    mar = InlineKeyboardMarkup([aa])
    bb = [InlineKeyboardButton(text='▪️ کانال ربات',url=f"{x[0][2]}")]
    kup = InlineKeyboardMarkup([bb])
    try:
        id = x[0][0]
        await c.get_chat_member(id, user_id)
        return None
    
        
    except UserNotParticipant:
        await m.reply(f'◂ کاربر عزیز {m.from_user.mention(m.from_user.first_name)} برای دستور دادن به ربات ابتدا باید در کانال ربات عضو شوید.',reply_markup=mar)
        return 'kos'
    except ChatAdminRequired:
        await m.reply(f'• لطفا ابتدا ربات را در کانال زیر ادمین کرده و سپس مجددا تلاش کنید !',reply_markup=kup)
        return 'kir'
    except ChannelInvalid:
        await m.reply('• لطفا ابتدا ربات را در کانال زیر ادمین کرده و سپس مجددا تلاش کنید !',reply_markup=kup)
        return 'kir'
    except:
        await m.reply(f'• کاربر عزیز {m.from_user.mention(m.from_user.first_name)} لطفا ابتدا در کانال زیر عضو شوید و سپس مجددا تلاش کنید !',reply_markup=mar)
        return 'kos'

######################################################################

######################################################################

api.start()
call_py.start()

@api.on_message(filters.private & filters.regex(r'^/start$'))
async def startt(c:Client, m:Message):
    kirsag = ""
    cur.execute('SELECT * FROM channel')
    kirsag = cur.fetchall()
    if kirsag == []:
        kirsag = 'https://t.me/CiaConfig'
    else:
        kirsag = kirsag[0][2]
    chat_id = m.chat.id
    message_id = m.id
    information_tuple = ()
    cur.execute('SELECT * FROM information WHERE id=1')
    for i in cur.fetchall():
        information_tuple = i
    a = [InlineKeyboardButton(text='📚 اطلاعات بیشتر',callback_data='aboutus')]
    b = [InlineKeyboardButton(text='💻 خرید مستقیم از سازنده',url=f"https://t.me/{information_tuple[4]}")]
    d = [InlineKeyboardButton(text='▪️ کانال ربات',url=f"{kirsag}"),InlineKeyboardButton(text='▪️ گروه پشتیبانی',url=f"https://t.me/{information_tuple[3]}")]
    k = [InlineKeyboardButton(text='📮 خرید غیر مستقیم',url=f"https://t.me/{information_tuple[5]}")]
    global ab
    ab = InlineKeyboardMarkup([a,b,d,k])
    e = [InlineKeyboardButton(text='بازگشت 🔙',callback_data='back')]
    global back
    back = InlineKeyboardMarkup([e])
    start = information_tuple[1]
    if 'MENTION' in start:
        start = start.replace('MENTION',m.from_user.mention(m.from_user.first_name))
    if 'BOLD' in start:
        start = start.replace('BOLD','**')
    if 'USERID' in start:
        start = start.replace('USERID',m.from_user.id)
    await c.send_message(chat_id,start,reply_markup=ab, reply_to_message_id=message_id)

    if chat_id == mersad:
        await c.send_message(chat_id,'**◆ به پنل برنامه نویس خوش آمدید ♡**',reply_to_message_id=message_id, reply_markup=ReplyKeyboardMarkup([
            ['📊 وضعیت'],
            ['📑 دریافت فاکتور', '📆 میزان اعتبار'],
            ['تنظیم نرخ پایه'],
            ['تنظیم نرخ ویدیو', 'تنظیم نرخ موزیک'],
            ['نرخ فروش موزیک','نرخ فروش ویدیو'],
            ['📨 ارسال همگانی','📨 ارسال همگانی گروه ها'],
            ['▪️اجبار ورود فعال','▫️اجبار ورود غیرفعال'],
            ['📋 لیست گروه های فعال موزیک'],
            ['📁 لیست گروه های تمدید موزیک'],
            ['📋 لیست گروه های فعال ویدیو'],
            ['📁 لیست گروه های تمدید ویدیو'],
            ['⚠️ لیست گروه های فاقد اعتبار'],
            ['❌ حذف سودو','📌 تنظیم سودو'],
            ['❌ حذف ادمین','📌 تنظیم ادمین'],
            ['👥 لیست سودو های ربات'],
            ['🗑 حذف گروه ویدیو','🗑 حذف گروه موزیک'],
            ['📬 ارسال به سودو'],
            ['✏️ تنظیم استارت','📚 تنظیم درباره ما'],
            ['📬 تنظیم پیامرسان','📥 تنظیم پی وی'],
            ['📢 تنظیم کانال','👥 تنظیم گروه'],
            ['تنظیم محدودیت 🔏','✏️ تنظیم استارت هلپر'],
            ['محدودیت نصب فعال ⚠️', 'محدودیت نصب غیرفعال ♻️'],
            ['▪️ خروج خودکار فعال','▫️ خروج خودکار غیرفعال']
            ],resize_keyboard=True,one_time_keyboard=True
        ))
    elif chat_id == sudo:
        await c.send_message(chat_id,'**◆ به پنل ادمین خوش آمدید ♡**',reply_to_message_id=message_id, reply_markup=ReplyKeyboardMarkup([
            ['📊 وضعیت'],
            ['📑 دریافت فاکتور', '📆 میزان اعتبار'],
            ['📨 ارسال همگانی','📨 ارسال همگانی گروه ها'],
            ['▪️اجبار ورود فعال','▫️اجبار ورود غیرفعال'],
            ['📋 لیست گروه های فعال موزیک'],
            ['📁 لیست گروه های تمدید موزیک'],
            ['📋 لیست گروه های فعال ویدیو'],
            ['📁 لیست گروه های تمدید ویدیو'],
            ['⚠️ لیست گروه های فاقد اعتبار'],
            ['❌ حذف سودو','📌 تنظیم سودو'],
            ['❌ حذف ادمین','📌 تنظیم ادمین'],
            ['👥 لیست سودو های ربات'],
            ['🗑 حذف گروه ویدیو','🗑 حذف گروه موزیک'],
            ['▪️ خروج خودکار فعال','▫️ خروج خودکار غیرفعال']
            ],resize_keyboard=True,one_time_keyboard=True
        ))
    cur.execute(f'SELECT * FROM users WHERE iduser={m.chat.id}')
    if cur.fetchall()==[]:
        try:
            cur.execute(f'INSERT INTO users(iduser) VALUES({m.chat.id})')
        except sqlite3.OperationalError:
            os.system('fuser -k database.sqlite')
            cur.execute(f'INSERT INTO users(iduser) VALUES({m.chat.id})')
        db.commit()

@api.on_message(filters.private & filters.user([mersad,sudo]) & filters.regex(r'^(📊 وضعیت)$'))
async def vaziat(c:Client,m:Message):
    user_id = m.from_user.id
    vidactive = len(kir(0))
    vidtam = len(kir(1))
    musactive = len(moz(0))
    mustam = len(moz(1))
    allvaz = len([*moz(2),*kir(2)])
    chargevid = len([*kir(0),*kir(1)])
    chargemus = len([*moz(0),*moz(1)])

    cur.execute('SELECT * FROM gp WHERE status=0')
    muscount = len(cur.fetchall())
    cur.execute('SELECT * FROM gp WHERE status=1')
    vidcount = len(cur.fetchall())
    
    cur.execute('SELECT * FROM autoleft')
    a = cur.fetchall()
    left = "ٔتعریف نشده" if a == [] else "فعال" if int(a[0][0]) == 1 else "غیرفعال"

    cur.execute('SELECT * FROM channel')
    ab = cur.fetchall()
    chan = "ٔتعریف نشده" if ab == [] else "فعال" if int(ab[0][3]) == 1 else "غیرفعال"

    await m.reply(
        f'''
◄ وضعیت و آمار ربات :

◂ آیدی عددی مدیر کل : {user_id}

─┅━ **آمار گروه ها** ━┅─

◂ تعداد گروه تحت مدیریت موزیک : {musactive}

◂ تعداد گروه تحت مدیریت ویدیو : {vidactive}

◂ تعداد گروه تمدید موزیک : {mustam}

◂ تعداد گروه تمدید ویدیو : {vidtam}

◂ تعداد گروه بدون اعتبار : {allvaz}

─┅━ **تنظیمات ربات** ━┅─

◂ اجبار ورود : {chan}

◂ خروج خودکار : {left}
        '''
    )

@api.on_message(filters.private & filters.user([mersad,sudo]) & filters.regex(r'^(▪️ خروج خودکار فعال)$'))
async def setlimmit(c:Client,m:Message):
    cur.execute('SELECT * FROM autoleft')
    status = cur.fetchall()
    if status == []:
        query = 'INSERT INTO autoleft(status) VALUES(?)'
        try:
            cur.execute(query, (1,))
        except sqlite3.OperationalError:
            os.system('fuser -k database.sqlite')
            cur.execute(query, (1,))
        db.commit()
    else:
        cur.execute('UPDATE autoleft SET status=1')
        db.commit()
    await m.reply('• خروج خودکار فعال شد !')

@api.on_message(filters.private & filters.user([mersad,sudo]) & filters.regex(r'^(▫️ خروج خودکار غیرفعال)$'))
async def setlimmit(c:Client,m:Message):
    cur.execute('SELECT * FROM autoleft')
    status = cur.fetchall()
    if status == []:
        query = 'INSERT INTO autoleft(status) VALUES(?)'
        try:
            cur.execute(query, (int(0),))
        except sqlite3.OperationalError:
            os.system('fuser -k database.sqlite')
            cur.execute(query, (int(0),))
        db.commit()
    else:
        cur.execute('UPDATE autoleft SET status=0')
        db.commit()
    await m.reply('• خروج خودکار غیرفعال شد !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^(تنظیم محدودیت 🔏)$'))
async def setlimmit(c:Client,m:Message):
    mesg = await c.ask(m.chat.id, '• مقدار مورد نظر جهت محدودیت نصب را وارد کنید !')
    cur.execute('SELECT * FROM limmit')
    x = cur.fetchall()
    if x != []:
        cur.execute(f'UPDATE limmit SET count={int(mesg.text)}')
    else:
        query = "INSERT INTO limmit(status,count) VALUES(?,?)"
        try:
            cur.execute(query, (0,int(mesg.text)))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (0,int(mesg.text)))
    db.commit()
    await m.reply('• مقدار محدودیت با موفقیت تنظیم شد !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^(محدودیت نصب فعال ⚠️)$'))
async def onlimmit(c:Client,m:Message):
    cur.execute('SELECT * FROM limmit')
    x = cur.fetchall()
    if x != []:
        cur.execute(f'UPDATE limmit SET status=1')
    else:
        query = "INSERT INTO limmit(status,count) VALUES(?,?)"
        try:
            cur.execute(query, (1,30))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (1,30))
    db.commit()
    await m.reply('• محدودیت با موفقیت فعال شد !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^(محدودیت نصب غیرفعال ♻️)$'))
async def offlimmit(c:Client,m:Message):
    cur.execute('SELECT * FROM limmit')
    x = cur.fetchall()
    if x != []:
        cur.execute(f'UPDATE limmit SET status=0')
    else:
        query = "INSERT INTO limmit(status,count) VALUES(?,?)"
        try:
            cur.execute(query, (0,30))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (0,30))
    db.commit()
    await m.reply('• محدودیت با موفقیت غیرفعال شد !')

@api.on_message(filters.private & filters.user([mersad, sudo]) & filters.regex(r'^📨 ارسال همگانی گروه ها$'))
async def hamegani(c:Client,m:Message):
    hameg = await c.ask(m.chat.id,"◂ عبارت مورد نیاز جهت ارسال به تمام گروه هارا ارسال کنید (جهت لغو از دستور ( /canncel ) استفاده کنید !)")
    if hameg.text == '/canncel':
        await m.reply('• شما به منوی اصلی بازگشتید !')
        return
    kh = await c.send_message(m.chat.id,'• در حال ارسال متن به تمامی گروه ها ...\n◂ چند دقیقه منتظر بمانید !')
    cur.execute('SELECT * FROM charge')
    for i in cur.fetchall():
        try:
            await c.copy_message(i[0],m.chat.id,m.id+2)
        except:
            pass
    cur.execute('SELECT * FROM charge2')
    for ii in cur.fetchall():
        try:
            await c.copy_message(ii[0],m.chat.id,m.id+2)
        except:
            pass
    await kh.edit('• متن مورد نظر به تمامی گروه های ربات با موفقیت ارسال شد !')

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📨 ارسال همگانی$'))
async def hamegani(c:Client,m:Message):
    hameg = await c.ask(m.chat.id,"◂ مورد مورد نظر برای ارسال همگانی را وارد کنید و برای لغو از دستور ( /canncel ) استفاده کنید :")
    if hameg.text == '/canncel':
        await m.reply('• شما به منوی اصلی بازگشتید !')
        return
    kh = await c.send_message(m.chat.id,'• در حال ارسال به تمامی کاربران ...\n◂ چند دقیقه منتظر بمانید !')
    cur.execute('SELECT * FROM users')
    for i in cur.fetchall():
        try:
            await c.copy_message(i[0],m.chat.id,m.id+2)
        except:
            pass
    await kh.edit('• به تمامی کاربران ربات با موفقیت ارسال شد !')

@api.on_message(filters.private & filters.user([mersad, sudo]) & (filters.regex(r'^▪️اجبار ورود فعال$') | filters.regex(r'^([Jj][Oo][Ii][Nn][Oo][Nn])$')))
async def kos2(c:Client, m:Message):
    cur.execute('SELECT * FROM channel')
    x = cur.fetchall()
    if x[0][0] == None:
        await m.reply('• لطفا ابتدا یک کانال برای این بخش تنظیم کنید !')
        return
    cur.execute('UPDATE channel SET status=1')
    db.commit()
    await m.reply('• اجبار ورود فعال شد !')

@api.on_message(filters.private & filters.user([mersad, sudo]) & (filters.regex(r'^▫️اجبار ورود غیرفعال$') | filters.regex(r'^([Jj][Oo][Ii][Nn][Oo][Ff][Ff])$')))
async def koks(c:Client, m:Message):
    cur.execute('SELECT * FROM channel')
    x = cur.fetchall()
    if x[0][0] == None:
        await m.reply('• لطفا ابتدا یک کانال برای این بخش تنظیم کنید !')
        return
    cur.execute('UPDATE channel SET status=0')
    db.commit()
    await m.reply('• اجبار ورود غیرفعال شد !')

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📋 لیست گروه های فعال موزیک$'))
async def acdxcft(c:Client,m:Message):
    charlist = ''
    count = 0
    etebar = 0
    goh = 0
    cur.execute('SELECT * FROM charge WHERE status=0')
    for i in cur.fetchall():
        count += 1
        etebar = int(i[4] - time.time())
        etebar = int(etebar / 60 / 60 / 24)
        charlist += f'{count} - {i[7]}\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n◂ اعتبار : `{etebar}` روز\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
        etebar = 0
        if count == 26:

            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        elif count == 51:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        elif count == 75:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        else:
            pass
    if goh == 0 or goh == 1 or goh == 2 :
        try:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
        except MessageEmpty:
            await c.send_message(m.chat.id,'• در حال حاضر گروه فعالی ثبت نشده است !',reply_to_message_id=m.id)
    elif goh==1:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    elif goh==2:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    elif goh==3:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    charlist = ''

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📁 لیست گروه های تمدید موزیک$'))
async def acwet(c:Client,m:Message):
    charlist = ''
    charlist1 = ""
    count = 0
    cur.execute('SELECT * FROM charge WHERE status=1')
    for i in cur.fetchall():
        count += 1
        etebar = int(i[4] - time.time())
        etebar = int(etebar / 60 / 60 )
        # charlist += f'{count} - [{req.title}]({req.invite_link})\n◂ شناسه گروه : `{req.id}`\n◂ اعتبار : `{etebar}` ساعت\n┈┅━─━─━─━─•◈•─━─━─━─━┅┈\n'
        charlist += f'{count} - {i[7]}\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n◂ اعتبار : `{etebar}` ساعت\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
    try:
        if len(charlist) > 4024:
            charlist11 = 0
            for i in charlist:
                charlist11 += 1
                charlist1 += i
                if charlist11 > 4024:
                    break

        charlist = charlist.replace(charlist1,"")
        if charlist1 not in charlist:
            status = True
        else:
            status = False

        if status == True:
            await c.send_message(m.chat.id,charlist1,reply_to_message_id=m.id,disable_web_page_preview=True)
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
        else:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    except MessageEmpty:
        await c.send_message(m.chat.id,'• در حال حاضر گروه تمدیدی ثبت نشده است !',reply_to_message_id=m.id)
    charlist = ''

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📋 لیست گروه های فعال ویدیو$'))
async def acsdet(c:Client,m:Message):
    charlist = ''
    count = 0
    etebar = 0
    goh = 0
    cur.execute('SELECT * FROM charge2 WHERE status=0')
    for i in cur.fetchall():
        count += 1
        etebar = int(i[4] - time.time())
        etebar = int(etebar / 60 / 60 / 24)
        charlist += f'{count} - {i[7]}\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n◂ اعتبار : `{etebar}` روز\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
        etebar = 0
        if count == 26:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        elif count == 51:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        elif count == 75:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
            charlist = charlist.replace(charlist,'')
            goh += 1
        else:
            pass
    if goh == 0:
        try:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
        except MessageEmpty:
            await c.send_message(m.chat.id,'• در حال حاضر گروه فعالی ثبت نشده است !',reply_to_message_id=m.id)
    elif goh==1:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    elif goh==2:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    elif goh==3:
        await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    charlist = ''

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📁 لیست گروه های تمدید ویدیو$'))
async def acxsdxddt(c:Client,m:Message):
    charlist = ''
    count = 0
    cur.execute('SELECT * FROM charge2 WHERE status=1')
    for i in cur.fetchall():
        count += 1
        etebar = int(i[4] - time.time())
        etebar = int(etebar / 60 / 60 )
        # charlist += f'{count} - [{req.title}]({req.invite_link})\n◂ شناسه گروه : `{req.id}`\n◂ اعتبار : `{etebar}` ساعت\n┈┅━─━─━─━─•◈•─━─━─━─━┅┈\n'
        charlist += f'{count} - {i[7]}\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n◂ اعتبار : `{etebar}` ساعت\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
    try:
        if len(charlist) > 4024:
            charlist1 = ""
            charlist11 = 0
            for i in charlist:
                charlist11 += 1
                charlist1 += i
                if charlist11 > 4024:
                    break
        try:
            charlist = charlist.replace(charlist1,"")
            status = True
        except:
            status = False
        if status == True:
            await c.send_message(m.chat.id,charlist1,reply_to_message_id=m.id,disable_web_page_preview=True)
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
        else:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    except MessageEmpty:
        await c.send_message(m.chat.id,'• در حال حاضر گروه تمدیدی ثبت نشده است !',reply_to_message_id=m.id)
    charlist = ''

@api.on_message(filters.private & filters.user([sudo,mersad]) & filters.regex(r'^⚠️ لیست گروه های فاقد اعتبار$'))
async def acdsxxaxt(c:Client,m:Message):
    charlist = ''
    count = 0
    cur.execute('SELECT * FROM charge WHERE status=2')
    for i in cur.fetchall():
        count += 1
        charlist += f'{count} - {i[7]} (#Music)\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
    cur.execute('SELECT * FROM charge2 WHERE status=2')
    for i in cur.fetchall():
        count += 1
        charlist += f'{count} - {i[7]} (#Video)\n◂ شناسه گروه : `{i[0]}`\n◂ لینک گروه : [برای ورود کلیک کنید.]({i[6]})\n─┅━━━━━━━━✥━━━━━━━━┅─\n'

    try:
        if len(charlist) > 4024:
            charlist1 = ""
            charlist11 = 0
            for i in charlist:
                charlist11 += 1
                charlist1 += i
                if charlist11 > 4024:
                    break
        try:
            charlist = charlist.replace(charlist1,"")
            status = True
        except:
            status = False
        if status == True:
            await c.send_message(m.chat.id,charlist1,reply_to_message_id=m.id,disable_web_page_preview=True)
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
        else:
            await c.send_message(m.chat.id,charlist,reply_to_message_id=m.id,disable_web_page_preview=True)
    except MessageEmpty:
        await c.send_message(m.chat.id,'• در حال حاضر گروه فاقد اعتباری ثبت نشده است !',reply_to_message_id=m.id)
    charlist = ''

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📌 تنظیم سودو$'))
async def addsudopv(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    sud = await c.ask(chat_id,'**•** آیدی عددی کاربر مورد نظر را وارد کنید **:**')
    try:
        req = await c.get_chat(int(sud.text))
    except:
        await c.send_message(chat_id,'**•** کاربر مورد نظر یافت نشد **!**',reply_to_message_id=message_id)
        return
    cur.execute(f'SELECT * FROM sudo WHERE idsudo={req.id}')
    if cur.fetchall() != []:
        await m.reply('• این کاربر از قبل در لیست سودو ها موجود میباشد !')
        return
    query = 'INSERT INTO sudo(idsudo, namesudo) VALUES(?,?)'
    try:
        cur.execute(query, (req.id, req.first_name))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (req.id, req.first_name))
    db.commit()
    await c.send_message(chat_id,f'''
**◆ یک کاربر با موفقیت به لیست سودو های ربات اضافه شد !**
◂ نام سودو : **{req.first_name}**
◂ شناسه سودو : `{req.id}`
◂ یوزرنیم سودو : {'ندارد' if req.username==None else req.username}
    ''',reply_to_message_id=message_id)
    await c.send_message(int(sud.text),"**⌯** شما به عنوان سودوی ربات منصوب شدید **!**")

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^❌ حذف سودو$'))
async def delsudopv(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    sud = await c.ask(chat_id,'**⌯** آیدی عددی کاربر مورد نظر را وارد کنید **:**')
    try:
        req = await c.get_chat(int(sud.text))
    except:
        await c.send_message(chat_id,'**⌯** کاربر مورد نظر یافت نشد **!**')
        return
    cur.execute(f'DELETE FROM sudo WHERE idsudo={int(sud.text)}')
    db.commit()
    await c.send_message(chat_id,f'''
**◆ یک کاربر با موفقیت از لیست سودو های ربات حذف شد !**
◂ نام سودو : **{req.first_name}**
◂ شناسه سودو : `{req.id}`
◂ یوزرنیم سودو : {'ندارد' if req.username==None else req.username}
    ''',reply_to_message_id=message_id)
    await c.send_message(int(sud.text),"**⌯** شما از لیست سودو های ربات حذف شدید **!**")

@api.on_message(filters.private & filters.user([mersad,sudo]) & filters.regex(r'^👥 لیست سودو های ربات'))
async def lisu(c:Client,m:Message):
    list_ = ''
    cur.execute('SELECT * FROM sudo')
    if cur.fetchall() != None:
        cur.execute('SELECT * FROM sudo')
        for i in cur.fetchall():
            req2 = await c.get_chat(i[0])
            list_ += f'◂ نام سودو : {req2.first_name}\n◂ شناسه سودو : {req2.id}\n◂ یوزرنیم سودو : @{req2.username}\n\n'
        try:
            await c.send_message(m.chat.id,list_,reply_to_message_id=m.id)
        except MessageEmpty:
            await c.send_message(m.chat.id,'**◂ لیست سودو های ربات خالی میباشد !**')
    else:
        await c.send_message(m.chat.id,'**◂ لیست سودو های ربات خالی میباشد !**')
    list_ =''

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^🗑 حذف گروه موزیک$'))
async def delgp(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    gop = await c.ask(chat_id,'**⌯** شناسه ی گروه مورد نظر را وارد کنید **:**')
    text = gop.text

    try:
        cur.execute(f'DELETE FROM musicadmin WHERE idgp = {int(text)}')
    except:
        pass
    try:
        cur.execute(f'DELETE FROM gp WHERE idgp = {int(text)} AND status=0')
    except:
        pass
    try:
        cur.execute(f'DELETE FROM charge WHERE idgp = {int(text)}')
    except:
        pass
    db.commit()
    await m.reply('• گروه مورد نظر با موفقیت حذف شد !')

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^🗑 حذف گروه ویدیو$'))
async def delwsgp(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    gop = await c.ask(chat_id,'**⌯** شناسه ی گروه مورد نظر را وارد کنید **:**')
    text = gop.text

    try:
        cur.execute(f'DELETE FROM videoadmins WHERE idgp = {int(text)}')
    except:
        pass
    try:
        cur.execute(f'DELETE FROM gp WHERE idgp = {int(text)} AND status=1')
    except:
        pass
    try:
        cur.execute(f'DELETE FROM charge2 WHERE idgp = {int(text)}')
    except:
        pass
    db.commit()
    await m.reply('• گروه مورد نظر با موفقیت حذف شد !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^📬 ارسال به سودو$'))
async def sudosender(c:Client,m:Message):
    payam = await c.ask(m.chat.id,'• پیام خود را به سودو ارسال کنید :')
    await c.send_message(sudo,payam.text,disable_web_page_preview=True)
    await c.send_message(m.chat.id,'• پیام شما به سودو ارسال شد !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^📚 تنظیم درباره ما$'))
async def about(c:Client, m:Message):
    chat_id = m.chat.id
    about = await c.ask(chat_id,'• متن درباره ما را وارد کنید :')
    cur.execute(f'UPDATE information SET about="{about.text}" WHERE id=1')
    db.commit()
    await c.send_message(chat_id, "• متن درباره ما با موفقیت تنظیم شد !", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^✏️ تنظیم استارت$'))
async def setstart(c:Client, m:Message):
    chat_id = m.chat.id
    start = await c.ask(chat_id,'• متن استارت را وارد کنید :')
    start = start.text
    
    cur.execute(f'UPDATE information SET start="{start}" WHERE id=1')
    db.commit()
    await c.send_message(chat_id, "• متن استارت با موفقیت تنظیم شد !", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^✏️ تنظیم استارت هلپر$'))
async def setstart(c:Client, m:Message):
    chat_id = m.chat.id
    start = await c.ask(chat_id,'• متن استارت هلپر را وارد کنید :')
    start = start.text
    
    cur.execute(f'UPDATE startcli SET start="{start}"')
    db.commit()
    await c.send_message(chat_id, "• متن استارت هلپر با موفقیت تنظیم شد !", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^📥 تنظیم پی وی$'))
async def adminpv(c:Client, m:Message):
    chat_id = m.chat.id
    tex = await c.ask(chat_id,'• آیدی را بدون @ وارد کنید :')
    cur.execute(f'UPDATE information SET adminpv="{tex.text}" WHERE id=1')
    db.commit()
    await c.send_message(chat_id, "**◆ آیدی ادمین با موفقیت ست شد ✓**", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^📬 تنظیم پیامرسان$'))
async def payamresan(c:Client, m:Message):
    chat_id = m.chat.id
    tex = await c.ask(chat_id,'**◆ آیدی را بدون @ وارد کنید :**')
    cur.execute(f'UPDATE information SET payamresan="{tex.text}" WHERE id=1')
    db.commit()
    await c.send_message(chat_id, "**◆ آیدی پیامرسان با موفقیت ست شد ✓**", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^👥 تنظیم گروه$'))
async def gp(c:Client, m:Message):
    chat_id = m.chat.id
    tex = await c.ask(chat_id,'**◆ لینک گروه را بدون `https://t.me/` وارد کنید :**')
    cur.execute(f'UPDATE information SET groupp="{tex.text}" WHERE id=1')
    db.commit()
    await c.send_message(chat_id, "**◆ لینک گروه با موفقیت ست شد ✓**", reply_to_message_id = m.id)

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^📢 تنظیم کانال$'))
async def chnl(c:Client, m:Message):
    cur.execute('SELECT * FROM channel')
    wwe = cur.fetchall()
    if wwe != []:
        inpu = await c.ask(m.chat.id,'ایدی عددی کانال را همراه با -100 وارد کنید :')
        req2 = await c.get_chat(int(inpu.text))
        idchannel = req2.id
        namechannel = req2.title
        invite = req2.invite_link
        if invite == None:
            await m.reply('• ربات در کانال ادمین نیست !')
            return
        cur.execute('SELECT * FROM channel')
        idid = cur.fetchall()[0][0]
        cur.execute(f'UPDATE channel SET idchannel={idchannel}, namechannel="{namechannel}", invite="{invite}" WHERE idchannel={idid}')
        db.commit()
        await m.reply(f'• کانال {namechannel} با موفقیت تنظیم شد !')
    else:
        inpu = await c.ask(m.chat.id,'ایدی عددی کانال را همراه با -100 وارد کنید :')
        if '-100' not in str(inpu.text):
            return
        
        req2 = await c.get_chat(int(inpu.text))
        idchannel = req2.id
        namechannel = req2.title
        invite = req2.invite_link
        if invite == None:
            await m.reply('• ربات در کانال ادمین نیست !')
            return
        query = 'INSERT INTO channel(idchannel, namechannel, invite, status) VALUES(?,?,?,?)'
        try:
            cur.execute(query, (idchannel, namechannel, invite, 0))
        except:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(query, (idchannel, namechannel, invite, 0))
        db.commit()
        await m.reply(f'Channel ({namechannel}) Seted !')

@api.on_message(filters.group & (filters.regex(r'^اعتبار$') | filters.regex(r'^[Cc][Rr][Ee][Dd][Ii][Tt]$')))
async def etebargp(c:Client,m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id

    list_admin = []
    async for i in c.get_chat_members(chat_id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
        list_admin.append(i.user.id)

    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        list_admin.append(i[0])
    list_admin.append(mersad)
    list_admin.append(sudo)
    if user_id in list_admin:
        join = await checkjoin(c,m,user_id)
        if join != None:
            return
        c_id = str(chat_id)
        # c_id = int(c_id.replace('-100',''))
        global daygp
        daygp = 0
        etebar_music = 0
        status_music = 0
        etebar_video = 0
        status_video = 0
        cur.execute(f'SELECT * FROM charge WHERE idgp={c_id}')
        if cur.fetchone() != None:
            eteb = []
            cur.execute(f'SELECT * FROM charge WHERE idgp={c_id}')
            for i in cur.fetchall()[0]:
                eteb.append(i)
            if eteb[5] == 0:
                etebar_music = int(int(eteb[4] - time.time()) / 60 / 60 / 24)
                status_music = 0
            elif eteb[5] == 1:
                etebar_music = int(int(eteb[4] - time.time()) / 60 / 60)
                status_music = 1
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={c_id}')
        if cur.fetchone() != None:
            eteb = []
            cur.execute(f'SELECT * FROM charge2 WHERE idgp={c_id}')
            for i in cur.fetchall()[0]:
                eteb.append(i)
            if eteb[5] == 0:
                etebar_video = int(int(eteb[4] - time.time()) / 60 / 60 / 24)
                status_video = 0
            elif eteb[5] == 1:
                etebar_video = int(int(eteb[4] - time.time()) / 60 / 60)
                status_video = 1
        await m.reply(f'**⌯** گروه شما به مدت {etebar_music} {"ساعت" if status_music == 1 else "روز"} اعتبار موزیک و به مدت {etebar_video} {"ساعت" if status_video == 1 else "روز"} اعتبار ویدیو دارد **!**')

@api.on_message(filters.group & (filters.regex(r'^[Ii][Dd]$') | filters.regex(r'^آیدی$') | filters.regex(r'^ایدی$')))
async def id(c:Client, m:Message):
    chat_id = m.chat.id
    message_id = m.id
    user_id = m.from_user.id
    username = m.from_user.username
    first_name = m.from_user.first_name
    sudos = []
    sudos.clear()
    sudos.append(sudo)
    sudos.append(mersad)
    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        sudos.append(i[0])
    if user_id in sudos:
        join = await checkjoin(c,m,user_id)
        if join != None:
            return
        sudos.remove(sudo)
        sudos.remove(mersad)
        if m.reply_to_message:
            try:
                async for i in api.get_chat_photos(m.reply_to_message.from_user.id,limit = 1):
                    prof = i
                await c.send_photo(
                    chat_id,
                    prof.file_id,
                    f'''
┈┅┅━┃**اطلاعات کاربر**┃━┅┅┈
⋆ نام : {m.reply_to_message.from_user.first_name}
⋆ شناسه : `{m.reply_to_message.from_user.id}`
⋆ نام کاربری : @{m.reply_to_message.from_user.username}
⋆ مقام : {'برنامه نویس' if m.reply_to_message.from_user.id ==mersad else 'مالک ربات' if m.reply_to_message.from_user.id == sudo else 'ادمین ربات' if m.reply_to_message.from_user.id in sudos else '--'}
┈┅┅━┃**شناسه گروه**┃━┅┅┈
⋆ شناسه : `{chat_id}`
                    ''',
                    reply_to_message_id=message_id
                )
                return
            except:
                await c.send_message(chat_id,f'''
┈┅┅━┃**اطلاعات کاربر**┃━┅┅┈
⋆ نام : {m.reply_to_message.from_user.first_name}
⋆ شناسه : `{m.reply_to_message.from_user.id}`
⋆ نام کاربری : @{m.reply_to_message.from_user.username}
⋆ مقام : {'برنامه نویس' if m.reply_to_message.from_user.id ==mersad else 'مالک ربات' if m.reply_to_message.from_user.id == sudo else 'ادمین ربات' if m.reply_to_message.from_user.id in sudos else '--'}
┈┅┅━┃**شناسه گروه**┃━┅┅┈
⋆ شناسه : `{chat_id}`
                ''',reply_to_message_id=message_id)
                return
        elif  m.text in ['id','ID','Id','iD','ایدی','آیدی']:
            try:
                async for i in api.get_chat_photos(m.reply_to_message.from_user.id,limit = 1):
                    prof = i
                await c.send_photo(
                    chat_id,
                    prof.file_id,
                    f'''
┈┅┅━┃**اطلاعات کاربر**┃━┅┅┈
⋆ نام : {first_name}
⋆ شناسه : `{user_id}`
⋆ نام کاربری : @{username}
⋆ مقام : {'برنامه نویس' if user_id ==mersad else 'مالک ربات' if user_id == sudo else 'ادمین ربات' if user_id in sudos else '--'}
┈┅┅━┃**شناسه گروه**┃━┅┅┈
⋆ شناسه : `{chat_id}`
                    ''',
                    reply_to_message_id=message_id
                )
                return
            except:
                await c.send_message(chat_id,f'''
┈┅┅━┃**اطلاعات کاربر**┃━┅┅┈
⋆ نام : {first_name}
⋆ شناسه : `{user_id}`
⋆ نام کاربری : @{username}
⋆ مقام : {'برنامه نویس' if user_id ==mersad else 'مالک ربات' if user_id == sudo else 'ادمین ربات' if user_id in sudos else '--'}
┈┅┅━┃**شناسه گروه**┃━┅┅┈
⋆ شناسه : `{chat_id}`
                ''',reply_to_message_id=message_id)
                return

@api.on_message(filters.private & (filters.regex(r'^(آپدیت شارژ ویدیو)') | filters.regex(r'^(اپدیت شارژ ویدیو)')))
async def updatech(c:Client,m:Message):
    chat_id = m.chat.id
    text = m.text
    sudos = []
    cur.execute('SELECT * FROM sudo')
    sudos.clear()
    sudos.append(sudo)
    sudos.append(mersad)
    for i in cur.fetchall():
        sudos.append(i[0])
    if chat_id in sudos:
        text = text.replace('اپدیت شارژ ویدیو ','')
        text = text.replace('آپدیت شارژ ویدیو ','')
        text = text.split(' ')
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={int(text[0])}')
        if cur.fetchone() != None:
            cur.execute(f'UPDATE charge2 SET end={time.time() + float(int(text[1]) * 24 * 60 * 60)} WHERE idgp={int(text[0])}')
            db.commit()
            cur.execute(f'UPDATE charge2 SET day={int(text[1])} WHERE idgp={int(text[0])}')
            db.commit()
            cur.execute(f'UPDATE charge2 SET status=0 WHERE idgp={int(text[0])}')
            db.commit()
            await c.send_message(chat_id,'**⌯** شارژ ویدیو آپدیت شد **!**',reply_to_message_id=m.id)
            hour = jdatetime.datetime.now().strftime("%H:%M:%S")
            dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
            a = hour + dat
            req = await c.get_chat(int('-100'+str(text[0])))
            await c.send_message(sudo,f'''
**⇐ شارژ یک گروه ویدیو توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
            await c.send_message(mersad,f'''
**⇐ شارژ یک گروه ویدیو توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        else:
            await c.send_message(chat_id, '**⌯** گروه مورد نظر یافت نشد **!**',reply_to_message_id=m.id)
    await m.continue_propagation()

@api.on_message(filters.group & (filters.regex(r'^(اپدیت شارژ ویدیو)') | filters.regex(r'^(آپدیت شارژ ویدیو)')))
async def updategp(c:Client,m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    sudos = []
    cur.execute('SELECT * FROM sudo')
    sudos.clear()
    sudos.append(sudo)
    sudos.append(mersad)
    for i in cur.fetchall():
        sudos.append(i[0])
    if user_id in sudos:
        text = text.replace('اپدیت شارژ ویدیو ','')
        text = text.replace('آپدیت شارژ ویدیو ','')
        if not text.isnumeric():
            await c.send_message(chat_id,'**⌯** شارژ گروه باید به صورت عدد باشد **!**',reply_to_message_id=m.id)
            return


        else:
            c_id = str(chat_id)
            try:
                cur.execute(f'SELECT * FROM charge2 WHERE idgp={int(c_id)}')
                db.commit()
                if cur.fetchone() != None:
                    cur.execute(f'UPDATE charge2 SET day={int(text)} WHERE idgp={c_id}')
                    db.commit()
                    cur.execute(f'UPDATE charge2 SET end={time.time() + float(int(text) * 24 * 60 * 60)} WHERE idgp={c_id}')
                    db.commit()
                    cur.execute(f'UPDATE charge2 SET status=0 WHERE idgp={c_id}')
                    db.commit()
                    await c.send_message(chat_id,'**⌯** شارژ گروه آپدیت شد **!**',reply_to_message_id=m.id)
                    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
                    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
                    a = hour + dat
                    req = await c.get_chat(chat_id)


                    await c.send_message(sudo,f'''
**⇐ شارژ یک گروه ویدیو توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
                    await c.send_message(mersad,f'''
**⇐ شارژ یک گروه ویدیو توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
                else:
                    await c.send_message(chat_id,'**⌯** این گروه فاقد اعتبار است لطفا ابتدا آن را شارژ کنید **!**',reply_to_message_id=m.id)
            except:
                pass

@api.on_message(filters.private & (filters.regex(r'^آپدیت شارژ') | filters.regex(r'^اپدیت شارژ')))
async def updatech(c:Client,m:Message):
    chat_id = m.chat.id
    text = m.text
    sudos = []
    cur.execute('SELECT * FROM sudo')
    sudos.clear()
    sudos.append(sudo)
    sudos.append(mersad)
    for i in cur.fetchall():
        sudos.append(i[0])
    if chat_id in sudos:
        text = text.replace('اپدیت شارژ ','')
        text = text.replace('آپدیت شارژ ','')
        text = text.split(' ')
        cur.execute(f'SELECT * FROM charge WHERE idgp={int(text[0])}')
        if cur.fetchone() != None:
            cur.execute(f'UPDATE charge SET end={time.time() + float(int(text[1]) * 24 * 60 * 60)} WHERE idgp={int(text[0])}')
            db.commit()
            cur.execute(f'UPDATE charge SET day={int(text[1])} WHERE idgp={int(text[0])}')
            db.commit()
            cur.execute(f'UPDATE charge SET status=0 WHERE idgp={int(text[0])}')
            db.commit()
            await c.send_message(chat_id,'**⌯** شارژ موزیک آپدیت شد **!**',reply_to_message_id=m.id)
            hour = jdatetime.datetime.now().strftime("%H:%M:%S")
            dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
            a = hour + dat
            req = await c.get_chat(int('-100'+str(text[0])))
            await c.send_message(sudo,f'''
**⇐ شارژ یک گروه توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
            await c.send_message(mersad,f'''
**⇐ شارژ یک گروه توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ اعتبار جدید : {text[1]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        else:
            await c.send_message(chat_id, '**⌯** گروه مورد نظر یافت نشد **!**',reply_to_message_id=m.id)

@api.on_message(filters.group & (filters.regex(r'^اپدیت شارژ') | filters.regex(r'^آپدیت شارژ')))
async def updategp(c:Client,m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    sudos = []
    cur.execute('SELECT * FROM sudo')
    sudos.clear()
    sudos.append(sudo)
    sudos.append(mersad)
    for i in cur.fetchall():
        sudos.append(i[0])
    if user_id in sudos:
        text = text.replace('اپدیت شارژ ','')
        text = text.replace('آپدیت شارژ ','')
        if not text.isnumeric():
            await c.send_message(chat_id,'**⌯** شارژ گروه باید به صورت عدد باشد **!**',reply_to_message_id=m.id)
            return


        else:
            c_id = str(chat_id)
            try:
                cur.execute(f'SELECT * FROM charge WHERE idgp={c_id}')
                db.commit()
                if cur.fetchone() != None:
                    cur.execute(f'UPDATE charge SET day={int(text)} WHERE idgp={c_id}')
                    db.commit()
                    cur.execute(f'UPDATE charge SET end={time.time() + float(int(text) * 24 * 60 * 60)} WHERE idgp={c_id}')
                    db.commit()
                    cur.execute(f'UPDATE charge SET status=0 WHERE idgp={c_id}')
                    db.commit()
                    await c.send_message(chat_id,'**⌯** شارژ گروه آپدیت شد **!**',reply_to_message_id=m.id)
                    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
                    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
                    a = hour + dat
                    req = await c.get_chat(chat_id)


                    await c.send_message(sudo,f'''
**⇐ شارژ یک گروه توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ اعتبار جدید : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
                    await c.send_message(mersad,f'''
**⇐ شارژ یک گروه توسط سودو آپدیت شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ اعتبار جدید : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
                else:
                    await c.send_message(chat_id,'**⌯** این گروه فاقد اعتبار است لطفا ابتدا آن را شارژ کنید **!**',reply_to_message_id=m.id)
            except:
                pass

@api.on_message(filters.private & filters.regex(r'^(تنظیم شارژ ویدیو)'))
async def charge(c:Client, m:Message):
    global cur,db
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    text = m.text
    text = text.replace('تنظیم شارژ ویدیو ','')
    text = text.split(' ')
    if '-100' not in str(text):
        return await m.reply('لطفا ایدی عددی گروه را همراه با -100 وارد کنید !')
    if not text[1].isnumeric() and len(text[1]) < 7:
        await c.send_message(chat_id,"""
**◆ آیدی عددی ادمین باید عدد باشد ×
روش استفاده از این دستور :
تنطیم شارژ (شناسه گروه) (شناسه ادمین) (روز)**
        """,reply_to_message_id=m.id)
    
    elif not text[2].isnumeric():
        await c.send_message(chat_id,"""
**◆ تعداد روز ها باید عدد باشد ×
روش استفاده از این دستور :
تنطیم شارژ (شناسه گروه) (شناسه ادمین) (روز)**
        """,reply_to_message_id=m.id)
    else:
        try:
            try:
                req = await c.get_chat(int(text[0]))
            except:
                await c.send_message(chat_id,'**⌯** گروه یافت نشد **!**',reply_to_message_id=m.id)
                return
            try:
                req2 = await c.get_chat(int(text[1]))
            except:
                await c.send_message(chat_id, '**⌯** کاربر یافت نشد **!**', reply_to_message_id=m.id)
                return
        except:
            return
        start = time.time()
        end = time.time()+float(int(text[2]) * 24 * 60 * 60)
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={text[0]}')
        for i in cur.fetchall():
            if i[0] == int(text[0]):
                await c.send_message(chat_id,
                '**⌯** این گروه از قبل در دیتابیس وجود دارد **!**',
                reply_to_message_id=m.id)
                return
        try:
            await c.get_chat(int(text[1]))
        except:
            await c.send_message(chat_id, '**⌯** گروه یافت نشد **!**')
            return
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={text[0]}')
        if cur.fetchall() != []:
            await m.reply('این گروه از قبل در لیست گروه های ویدیو ثبت شده است !')
            return
        query = '''INSERT INTO
        charge2(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            lin  = await c.export_chat_invite_link(req.id)
        except:
            return await m.reply('لطفا ابتدا ربات را در گروه ادمین کنید !')
        try:
            cur.execute(query, (text[0],text[1],text[2],start,end,0,lin,req.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (text[0],text[1],text[2],start,end,0,lin,req.title))
        db.commit()

        await c.send_message(chat_id,
        f'''
◂ گروه **{req.title}** به مدت **{text[2]}** روز شارژ شد ✅

◂ نام همکار : [{m.from_user.first_name}](tg://openmessage?user_id={chat_id})
◂ مدیر گروه : [{req2.first_name}](tg://openmessage?user_id={text[1]})
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})
#Video
        ''',reply_to_message_id=m.id,
        disable_web_page_preview=True
        )
        await c.send_message(int(text[1]),f'**⌯** گروه به مدت {text[2]} روز شارژ شد **!**')
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await c.send_message(sudo,f'''
**⇐ربات در گروه جدیدی برای ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ مقدار اعتبار : {text[2]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ربات در گروه جدیدی برای ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ مقدار اعتبار : {text[2]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)

@api.on_message(filters.group & filters.regex(r'^(تنظیم شارژ ویدیو)'))
async def chargegp(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    message_id = m.id
    text = m.text
    text = text.replace('تنظیم شارژ ویدیو ','')
    if '-100' not in str(chat_id):
        await c.send_message(chat_id,'**⌯** لطفا ابتدا گروه را به سوپر گروه تبدیل کنید و سپس دوباره سعی کنید **!**',reply_to_message_id=message_id)
        return
    if not text.isnumeric():
        await c.send_message(chat_id, f'**⌯** تعداد روز های شارژ باید به صورت عددی وارد شود **!**',reply_to_message_id=message_id)
    else:
        chat_id_str = chat_id
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={chat_id_str}')
        for i in cur.fetchall():
            if i[0] == chat_id_str:
                await c.send_message(chat_id,
                '**⌯** این گروه از قبل در لیست وجود دارد **!**',
                reply_to_message_id=m.id)
                return
        
        async for i in c.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                x = i.user.id
        end = time.time() + float(int(text) * 24 * 60 * 60)
        req = await c.get_chat(chat_id)
        # req2 = await c.get_chat(x)
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={text[0]}')
        if cur.fetchall() != []:
            await m.reply('• این گروه از قبل در لیست گروه های ویدیو ثبت شده است !')
            return
        query = '''INSERT INTO
        charge2(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (chat_id_str,x,text,time.time(),end,0,req.invite_link,req.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (chat_id_str,x,text,time.time(),end,0,req.invite_link,req.title))
        db.commit()

        await c.send_message(chat_id,
            f'**⌯** گروه به مدت {text} روز شارژ شد **!**',reply_to_message_id=m.id,
            disable_web_page_preview=True
            )
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await c.send_message(sudo,f'''
**⇐ربات در گروه جدیدی برای ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ مقدار اعتبار : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ربات در گروه جدیدی برای ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ مقدار اعتبار : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)

@api.on_message(filters.private & filters.regex(r'^(تنظیم شارژ)'))
async def charge(c:Client, m:Message):
    global cur,db
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    text = m.text
    text = text.replace('تنظیم شارژ ','')
    text = text.split(' ')
    if not text[0].isnumeric() and len(text[0]) < 10: 
        await c.send_message(chat_id,"""
    **◆ آیدی عددی گروه باید عدد باشد ×
    روش استفاده از این دستور :
    تنطیم شارژ (شناسه گروه) (شناسه ادمین) (روز)**
            """,reply_to_message_id=m.id)

    elif not text[1].isnumeric() and len(text[1]) < 7:
        await c.send_message(chat_id,"""
    **◆ آیدی عددی ادمین باید عدد باشد ×
    روش استفاده از این دستور :
    تنطیم شارژ (شناسه گروه) (شناسه ادمین) (روز)**
            """,reply_to_message_id=m.id)
        
    elif not text[2].isnumeric():
        await c.send_message(chat_id,"""
    **◆ تعداد روز ها باید عدد باشد ×
    روش استفاده از این دستور :
    تنطیم شارژ (شناسه گروه) (شناسه ادمین) (روز)**
            """,reply_to_message_id=m.id)

    else:
        try:
            try:
                req = await c.get_chat(text[0])
            except:
                await c.send_message(chat_id,'**⌯** گروه یافت نشد **!**',reply_to_message_id=m.id)
                return
            try:
                req2 = await c.get_chat(int(text[1]))
            except:
                await c.send_message(chat_id, '**⌯** کاربر یافت نشد **!**', reply_to_message_id=m.id)
                return
        except:
            return
        start = time.time()
        end = time.time()+float(int(text[2]) * 24 * 60 * 60)
        cur.execute(f'SELECT * FROM charge WHERE idgp={text[0]}')
        for i in cur.fetchall():
            if i[0] == int(text[0]):
                await c.send_message(chat_id,
                '**⌯** این گروه از قبل در لیست وجود دارد **!**',
                reply_to_message_id=m.id)
                return
        try:
            await c.get_chat(int(text[1]))
        except:
            await c.send_message(chat_id, '**⌯** گروه یافت نشد **!**')
            return
        cur.execute(f'SELECT * FROM charge WHERE idgp={text[0]}')
        if cur.fetchall() != []:
            await m.reply('• این گروه از قبل در لیست گروه های موزیک ثبت شده بود !')
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (text[0],text[1],text[2],start,end,0,req.invite_link,req.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (text[0],text[1],text[2],start,end,0,req.invite_link,req.title))
        db.commit()

        await c.send_message(chat_id,
        f'''
◂ گروه **{req.title}** به مدت **{text[2]}** روز شارژ شد ✅

◂ نام همکار : [{m.from_user.first_name}](tg://openmessage?user_id={chat_id})
◂ مدیر گروه : [{req2.first_name}](tg://openmessage?user_id={text[1]})
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})
            ''',reply_to_message_id=m.id,
            disable_web_page_preview=True
            )
        await c.send_message(int(text[1]),f'**⌯** گروه به مدت {text[2]} روز شارژ شد **!**')
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await c.send_message(sudo,f'''
**⇐ربات در گروه جدیدی اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ مقدار اعتبار : {text[2]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ربات در گروه جدیدی اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ مقدار اعتبار : {text[2]} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
            
        await m.continue_propagation()

@api.on_message(filters.group & filters.regex(r'^(تنظیم شارژ)'))
async def chargegp(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    message_id = m.id
    text = m.text
    text = text.replace('تنظیم شارژ ','')
    if '-100' not in str(chat_id):
        await c.send_message(chat_id,'**⌯** لطفا ابتدا گروه را به سوپر گروه تبدیل کنید و سپس دوباره سعی کنید **!**',reply_to_message_id=message_id)
        return
    if not text.isnumeric():
        await c.send_message(chat_id, '**⌯** تعداد روز های شارژ باید به صورت عدد وارد شود **!**',reply_to_message_id=message_id)
    else:
        cur.execute(f'SELECT * FROM charge WHERE idgp={chat_id}')
        for i in cur.fetchall():
            if i[0] == chat_id:
                await c.send_message(chat_id,
                '• این گروه از قبل در لیست وجود دارد !',
                reply_to_message_id=m.id)
                return
        async for i in c.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                x = i.user.id
        end = time.time() + float(int(text) * 24 * 60 * 60)
        req = await c.get_chat(chat_id)
        # req2 = await c.get_chat(x)
        cur.execute(f'SELECT * FROM charge WHERE idgp={text[0]}')
        if cur.fetchall() != []:
            await m.reply('• این گروه از قبل در لیست گروه های موزیک ثبت شده بود !')
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (chat_id,x,text,time.time(),end,0,req.invite_link,req.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (chat_id,x,text,time.time(),end,0,req.invite_link,req.title))
        db.commit()

        await c.send_message(chat_id,
            f'**⌯** گروه به مدت {text} روز شارژ شد **!**',reply_to_message_id=m.id,
            disable_web_page_preview=True
            )
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await c.send_message(sudo,f'''
**⇐ربات در گروه جدیدی اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ مقدار اعتبار : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ربات در گروه جدیدی اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ مقدار اعتبار : {text} روز
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)

@api.on_message(filters.private & filters.regex(r'^خروج'))
async def leftpv(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    text = m.text
    message_id = m.id
    text = text.replace('خروج ','')
    text = text.replace('-100','')
    try:
        text = int(text)
    except:
        await c.send_message(chat_id,'**⌯** لطفا آیدی عددی گروه را درست وارد کنید **!**',reply_to_message_id=message_id)
        return
    try:
        await c.send_message(int('-100'+str(text)), '**⌯** ربات از این گروه خارج میشود **!**',reply_to_message_id=message_id)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(chat_id)
        await c.send_message(sudo,f'''
**⇐ ربات از گروه زیر خارج شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ ربات از گروه زیر خارج شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
            ''',disable_web_page_preview=True)
        await c.leave_chat(int('-100'+str(text)))
        try:
            await cli.leave_chat(int('-100'+str(text)))
        except:
            pass
        await c.send_message(chat_id,'**⌯** ربات با موفقیت از گروه مورد نظر خارج شد **!**',reply_to_message_id=message_id)
    except:
        await c.send_message(chat_id, '**⌯** گروه یافت نشد **!**',reply_to_message_id=message_id)

@api.on_message(filters.group & filters.regex(r'^خروج$'))
async def leftgp(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    user_id = m.from_user.id
    if user_id not in [mersad,sudo, *idsudos()]:
        return
    await c.send_message(chat_id,'**⌯** ربات از این گروه خارج میشود **!**', reply_to_message_id=message_id)
    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
    a = hour + dat
    req = await c.get_chat(chat_id)
    await c.send_message(sudo,f'''
**⇐ ربات از گروه زیر خارج شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
        ''',disable_web_page_preview=True)
    await c.send_message(mersad,f'''
**⇐ ربات از گروه زیر خارج شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
        ''',disable_web_page_preview=True)
    await c.leave_chat(chat_id)
    try:
        await cli.leave_chat(chat_id)
    except:
        pass

################################################################################

################################################################################

@api.on_message(filters.group & (filters.regex(r'^([Ii][Nn][Ss][Tt][Aa][Ll][Ll])$') | filters.regex(r'^(نصب)$')))
async def install(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    if user_id not in [mersad, sudo, *idsudos(), *idowner()]:
        return
    repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
    repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
    repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
    repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
    repll = InlineKeyboardMarkup([repl, repl2, repl23 ,repl3])
    await m.reply('• یکی از گزینه های زیر را انتخاب کنید :',reply_markup=repll)

@api.on_message(filters.user(mersad) & (filters.regex(r'^(لیست گروه ویدیو)$') | filters.regex(r'^(این گشاد چند تا گروه ویدیو داره)$')))
async def chkvideo(c:Client, m:Message):
    cur.execute('SELECT * FROM gp WHERE status=1')
    x = cur.fetchall()
    if x == []:
        await m.reply('Not Any Group Installed !')
        return
    char = ''
    for i in x:
        char += f'**Group Name** : `{i[0]}`\n**Group ID** : `{i[1]}`\n**Group Link** : {i[2]}\n**─┅━━━━━━━━✥━━━━━━━━┅─**\n'
    await m.reply(char)

@api.on_message(filters.group & filters.user([mersad, sudo]) & (filters.regex(r'^(تنظیم سودو)$') | filters.regex(r'^([Ss][Ee][Tt][Ss][Uu][Dd][Oo])$')))
async def setsudo(c:Client, m:Message):
    if not m.reply_to_message:
        return
    
    cur.execute(f'SELECT * FROM sudo WHERE idsudo={m.reply_to_message.from_user.id}')
    if cur.fetchall() != []:
        await m.reply(f'• کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از قبل در لیست سودو ها بود !')
        return
    query = 'INSERT INTO sudo(idsudo, namesudo) VALUES(?,?)'
    try:
        cur.execute(query, (m.reply_to_message.from_user.id,m.reply_to_message.from_user.first_name))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (m.reply_to_message.from_user.id,m.reply_to_message.from_user.first_name))
    db.commit()
    await m.reply(f'کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} با موفقیت به لیست سودو ها اضافه شد !')

@api.on_message(filters.group & filters.user([mersad, sudo]) & (filters.regex(r'^(حذف سودو)$') | filters.regex(r'^([Dd][Ee][Ll][Ss][Uu][Dd][Oo])$')))
async def delsudo(c:Client, m:Message):
    if not m.reply_to_message:
        return
    list_ = []
    cur.execute(f'SELECT * FROM sudo')
    for i in cur.fetchall():
        list_.append(i[0])
    if m.reply_to_message.from_user.id in list_:
        try:
            cur.execute(f'DELETE FROM sudo WHERE idsudo={m.reply_to_message.from_user.id}')
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(f'DELETE FROM sudo WHERE idsudo={m.reply_to_message.from_user.id}')
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} با موفقیت از لیست سودو ها حذف شد **!**')
        return
    else:
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} در لیست سودو ها یافت نشد **!**')
        return

@api.on_message(filters.private & filters.user(mersad) & (filters.regex(r'^(تنظیم سودو)') | filters.regex(r'^([Ss][Ee][Tt][Ss][Uu][Dd][Oo])')))
async def setsudo(c:Client, m:Message):
    text = m.text
    text = text.replace('تنظیم سودو','')
    try:
        pattern = re.search(r'([Ss][Ee][Tt][Ss][Uu][Dd][Oo])',text)
        text = text.replace(pattern[0],'')
    except:
        pass
    try:
        req = await c.get_chat(int(text))
    except:
        await m.reply('کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM sudo WHERE idsudo={req.id}')
    if cur.fetchall() != []:
        await m.reply(f'• کاربر {req.first_name} از قبل در لیست سودو ها بود !')
        return
    query = 'INSERT INTO sudo(idsudo, namesudo) VALUES(?,?)'
    try:
        cur.execute(query, (req.id, req.first_name))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (req.id, req.first_name))
    db.commit()
    await m.reply(f'• کاربر {req.first_name} با موفقیت به لیست سودو ها اضافه شد !')

@api.on_message(filters.private & filters.user(mersad) & (filters.regex(r'^(حذف سودو)') | filters.regex(r'^([Dd][Ee][Ll][Ss][Uu][Dd][Oo])')))
async def delsudo(c:Client, m:Message):
    text = m.text
    text = text.replace('حذف سودو','')
    try:
        pattern = re.search(r'([Dd][Ee][Ll][Ss][Uu][Dd][Oo])',text)
        text = text.replace(pattern[0],'')
    except:
        pass
    try:
        req = await c.get_chat(int(text))
    except:
        await m.reply('• کاربر یافت نشد !')
    list_ = []
    cur.execute(f'SELECT * FROM sudo')
    for i in cur.fetchall():
        list_.append(i[0])
    if req.id in list_:
        try:
            cur.execute(f'DELETE FROM sudo WHERE idsudo={req.id}')
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(f'DELETE FROM sudo WHERE idsudo={req.id}')
            db.commit()
        await m.reply(f'**⌯** کاربر {req.first_name} با موفقیت از لیست سودو ها حذف شد **!**')
        return
    else:
        await m.reply(f'**⌯** کاربر {req.first_name} در لیست سودو ها یافت نشد **!**')
        return

@api.on_message(filters.user(mersad) & filters.regex(r'^پاکسازی$'))
async def cleardown(c:Client, m:Message):
    os.system('rm -rf downloads/*')
    await m.reply_text('**⌯** پوشه ی "downloads" با موفقیت پاکسازی شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(ربات)$') | filters.regex(r'^([Bb][Oo][Tt])$') | filters.regex(r'^([Rr][Oo][Bb][Oo][Tt])$')))
async def bot(c:Client, m:Message):
    list_ad = []
    async for member in c.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == 'administrator':
            pass
        else:
            list_ad.append(member.user.id)
    access = [*list_ad, *idsudos(), mersad, sudo]
    if m.from_user.id in list_ad:
        ans = random.choice(['◂ ربات آنلاین است 🙃','◂ جونم اَمر بفرما 😢','◂ کاری داشتی 🤔','◂ جانم عشقم 😍','◂ جـانم عزیزم 😄','◂ پر سرعت مثل همیشه 😎','◂ ربات درحال حاضر آنلاین میباشد !','◂ جونم مدیر عزیز 😉','◂ در انتظار دستورات شما 😁','◂ جانم 😅','◂ ربات درحال حاضر آنلاین میباشد !','◂ خوشگل گروه خودتی 😉','◂ بله عزیزم 🙂','◂ ربات درحال حاضر آنلاین میباشد !','◂ ربات درحال حاضر آنلاین میباشد !','◂ ربات درحال حاضر آنلاین میباشد !','◂ ربات درحال حاضر آنلاین میباشد !','◂ ربات درحال حاضر آنلاین میباشد !'])
        await m.reply(f'**{ans}**')

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^📌 تنظیم ادمین$'))
async def addsudopv(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    sud = await c.ask(chat_id,'**⌯** آیدی عددی کاربر مورد نظر را وارد کنید **:**')
    try:
        req = await c.get_chat(int(sud.text))
    except:
        await c.send_message(chat_id,'**⌯** کاربر مورد نظر یافت نشد **!**',reply_to_message_id=message_id)
        return
    cur.execute(f'SELECT * FROM owner WHERE idowner={req.id}')
    if cur.fetchall() != []:
        await m.reply('• این کاربر از قبل در لیست ادمین ها موجود میباشد !')
        return
    query = 'INSERT INTO owner(idowner, nameowner) VALUES(?,?)'
    try:
        cur.execute(query, (req.id, req.first_name))
    except sqlite3.OperationalError:
        os.system('sudo fuser -k database.sqlite')
        cur.execute(query, (req.id, req.first_name))
    db.commit()
    await c.send_message(chat_id,f'''
• یک کاربر با موفقیت به لیست ادمین های ربات اضافه شد !
◂ نام ادمین : **{req.first_name}**
◂ شناسه ادمین : `{req.id}`
◂ یوزرنیم ادمین : {'ندارد' if req.username==None else req.username}
    ''',reply_to_message_id=message_id)
    await c.send_message(int(sud.text),"**⌯** شما به عنوان ادمین ربات منصوب شدید **!**")

@api.on_message(filters.private & filters.user([sudo ,mersad]) & filters.regex(r'^❌ حذف ادمین$'))
async def delsudopv(c:Client,m:Message):
    chat_id = m.chat.id
    message_id = m.id
    sud = await c.ask(chat_id,'**⌯** آیدی عددی کاربر مورد نظر را وارد کنید **:**')
    try:
        req = await c.get_chat(int(sud.text))
    except:
        await c.send_message(chat_id,'**⌯** کاربر مورد نظر یافت نشد **!**')
        return
    cur.execute(f'DELETE FROM owner WHERE idowner={int(sud.text)}')
    db.commit()
    await c.send_message(chat_id,f'''
• یک کاربر با موفقیت از لیست ادمین های ربات حذف شد !
◂ نام ادمین : **{req.first_name}**
◂ شناسه ادمین : `{req.id}`
◂ یوزرنیم ادمین : {'ندارد' if req.username==None else req.username}
    ''',reply_to_message_id=message_id)
    await c.send_message(int(sud.text),"**⌯** شما از لیست ادمین های ربات حذف شدید **!**")

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(همگانی موزیک)$') | filters.regex(r'^([Aa][Ll][Ll][Mm][Uu][Ss][Ii][Cc])$')))
async def alllmusic(c:Client, m:Message):
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return

    cur.execute('SELECT * FROM alll WHERE status=0')
    if cur.fetchall() == []:
        try:
            query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 0))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 0))
            db.commit()
        await m.reply(f'**⌯**کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست پخش کننده های سراسری موزیک اضافه شد **!**')
        return
    ـlist = []
    cur.execute('SELECT * FROM alll WHERE status=0')
    for i in cur.fetchall():
        ـlist.append(i[0])
    if m.reply_to_message.from_user.id in ـlist:
        await m.reply(f'**⌯** کاربر {i[1]} از قبل در لیست سراسری موزیک وجود داشت **!**')
        return
    else:
        query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
        cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 0))
        db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست پخش کننده های سراسری موزیک اضافه شد **!**')
        return

@api.on_message(filters.group & (filters.regex(r'^(حذف همگانی موزیک)$') | filters.regex(r'^([Dd][Ee][Ll][Aa][Ll][Ll][Mm][Uu][Ss][Ii][Cc])$')))
async def delallmusic(c:Client, m:Message):
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return

    _list = []
    cur.execute('SELECT * FROM alll WHERE status=0')
    for i in cur.fetchall():
        _list.append(i[0])
    if m.reply_to_message.from_user.id in _list:
        try:
            cur.execute(f'DELETE FROM alll WHERE idsadmin={m.reply_to_message.from_user.id} AND status=0')
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(f'DELETE FROM alll WHERE idsadmin={m.reply_to_message.from_user.id} AND status=0')
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست پخش کننده های سراسری موزیک حذف شد **!**')
        return
    else:
        await m.reply('**⌯** کاربر مورد نظر در لیست سراسری موزیک یافت نشد **!**')

@api.on_message(filters.group & (filters.regex(r'^(همگانی ویدیو)$') | filters.regex(r'^([Aa][Ll][Ll][Vv][Ii][Dd][Ee][Oo])$')))
async def alllmusic(c:Client, m:Message):
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return

    cur.execute('SELECT * FROM alll WHERE status=1')
    if cur.fetchall() == []:
        try:
            query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 1))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 1))
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست پخش کننده های سراسری ویدیو اضافه شد **!**')
        return
    ـlist = []
    cur.execute('SELECT * FROM alll WHERE status=1')
    for i in cur.fetchall():
        ـlist.append(i[0])
    if m.reply_to_message.from_user.id in ـlist:
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از قبل در لیست سراسری ویدیو وجود داشت **!**')
        return
    else:
        query = 'INSERT INTO alll(idsadmin, namesadmin, status) VALUES(?,?,?)'
        cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name, 1))
        db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست پخش کننده های سراسری ویدیو اضافه شد **!**')
        return

@api.on_message(filters.group & (filters.regex(r'^(حذف همگانی ویدیو)$') | filters.regex(r'^([Dd][Ee][Ll][Aa][Ll][Ll][Vv][Ii][Dd][Ee][Oo])$')))
async def delallmusic(c:Client, m:Message):
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return

    _list = []
    cur.execute('SELECT * FROM alll WHERE status=1')
    for i in cur.fetchall():
        _list.append(i[0])
    if m.reply_to_message.from_user.id in _list:
        try:
            cur.execute(f'DELETE FROM alll WHERE idsadmin={m.reply_to_message.from_user.id} AND status=1')
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(f'DELETE FROM alll WHERE idsadmin={m.reply_to_message.from_user.id} AND status=1')
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست پخش کننده های سراسری ویدیو حذف شد **!**')
        return
    else:
        await m.reply('**⌯** کاربر مورد نظر در لیست سراسری ویدیو یافت نشد **!**')

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(ترفیع مالک)$') | filters.regex(r'^([Ss][Ee][Tt][Cc][Rr][Ee][Aa][Tt][Oo][Rr])$')))
async def setcreator(c:Client, m:Message):
    user_id = m.from_user.id
    chat_id = m.chat.id
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if user_id not in list_:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        await m.reply('• لطفا ابتدا گروه را نصب کنید !')
        return
    else:
        pass
    cur.execute(f'SELECT * FROM creators WHERE creator={m.reply_to_message.from_user.id}')
    if cur.fetchall() != []:
        await m.reply('**⌯** کاربر مورد نظر از قبل در لیست مالک ها بود **!**')
    else:
        query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
        try:
            cur.execute(query, (chat_id, m.reply_to_message.from_user.id))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(query, (chat_id, m.reply_to_message.from_user.id))
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} با موفقیت به لیست مالکین گروه اضافه شد **!**')

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(عزل مالک)$') | filters.regex(r'^([Dd][Ee][Ll][Cc][Rr][Ee][Aa][Tt][Oo][Rr])$')))
async def delcreator(c:Client, m:Message):
    user_id = m.from_user.id
    chat_id = m.chat.id
    list_ = [*idsudos(), *idowner(), mersad, sudo]
    if user_id not in list_:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        await m.reply('• لطفا ابتدا گروه را نصب کنید !')
        return
    else:
        pass
    cur.execute(f'SELECT * FROM creators WHERE creator={m.reply_to_message.from_user.id}')
    if cur.fetchall() == []:
        await m.reply('**⌯** کاربر مورد نظر در لیست مالکان گروه وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM creators WHERE creator={m.reply_to_message.from_user.id}')
        db.commit()
        await m.reply('**⌯** کاربر مورد نظر از لیست مالکان گروه حذف شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(ترفیع مالک)') | filters.regex(r'^([Ss][Ee][Tt][Cc][Rr][Ee][Aa][Tt][Oo][Rr])')))
async def cradd(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('ترفیع مالک','').replace('@','')
    try:
        serch = re.search(r'^([Ss][Ee][Tt][Cc][Rr][Ee][Aa][Tt][Oo][Rr])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('• کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        await m.reply('• لطفا ابتدا گروه را نصب کنید !')
        return
    else:
        pass
    cur.execute(f'SELECT * FROM creators WHERE creator={req.id}')
    if cur.fetchall() != []:
        await m.reply('**⌯** کاربر مورد نظر از قبل در لیست مالک ها بود **!**')
    else:
        query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
        try:
            cur.execute(query, (chat_id, req.id))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(query, (chat_id, req.id))
            db.commit()
        await m.reply(f'**⌯** کاربر {req.first_name} با موفقیت به لیست مالکین گروه اضافه شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(عزل مالک)') | filters.regex(r'^([Dd][Ee][Ll][Cc][Rr][Ee][Aa][Tt][Oo][Rr])')))
async def cradd(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('عزل مالک','').replace('@','')
    try:
        serch = re.search(r'^([Dd][Ee][Ll][Cc][Rr][Ee][Aa][Tt][Oo][Rr])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('• کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        await m.reply('• لطفا ابتدا گروه را نصب کنید !')
        return
    else:
        pass
    cur.execute(f'SELECT * FROM creators WHERE creator={req.id}')
    if cur.fetchall() == []:
        await m.reply('**⌯** کاربر مورد نظر در لیست مالکان گروه وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM creators WHERE creator={req.id}')
        db.commit()
        await m.reply('**⌯** کاربر مورد نظر از لیست مالکان گروه حذف شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(لیست مالکان)$') | filters.regex(r'^([Cc][Rr][Ee][Aa][Tt][Oo][Rr][Ss][Ll][Ii][Ss][Tt])$')))
async def stopvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *creators(chat_id), sudo, mersad]
    if user_id not in access:
        return
    a = creators(chat_id)
    char = ''
    for i in a:
        try:
            req = await cli.get_chat(i)
        except:
            pass
        char += f'-> [{req.first_name}](tg://openmessage?user_id={req.id}) **-** `{req.id}`\n'
    await m.reply(f'**⌯** لیست مالکان گروه :\n┈┅───┤📋├───┅┈\n{char}')

    

###########################################################################################################

###########################################################################################################

@api.on_message(filters.group & (filters.regex(r'^([Yy][Oo][Uu][Tt][Uu][Bb][Ee][Ss][Ee][Aa][Rr][Cc][Hh])') | filters.regex(r'^(سرچ یوتیوب)')))
async def dguiknhikmlutube(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*kir(1), *kir(0)]
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    if user_id not in access:
        return
    if chat_id not in horn:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    text = m.text
    text = text.replace('سرچ یوتیوب','')
    try:
        patt = re.search(r'^([Yy][Oo][Uu][Tt][Uu][Bb][Ee][Ss][Ee][Aa][Rr][Cc][Hh])',text)
        text = text.replace(patt[0], '')
    except:
        pass
    text = text.strip()
    videosSearch = VideosSearch(text, limit = 1)

    try:
        await call_py.leave_group_call(m.chat.id)
    except:
        pass
    ey = videosSearch.result()['result'][0]['link']
    mp3_url = await utub(ey)
    path = mp3_url
    print("Playing {} in {}".format(path, m.chat.title))
    await call_py.join_group_call(chat_id, AudioVideoPiped(path), stream_type = StreamType().live_stream)
    playing.update({m.chat.id: path})
    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
    a = hour + dat
    try:
        await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
        ''',reply_to_message_id=m.id,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
            [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
            [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
            [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
        ]))
    except:
        await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
        ''',reply_to_message_id=m.id,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
            [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
            [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
            [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
        ]))

@api.on_message(filters.group & (filters.regex(r'^(پخش ویدیو)$') | filters.regex(r'^([Pp][Ll][Aa][Yy][Vv][Ii][Dd][Ee][Oo])$')))
async def playvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*kir(1), *kir(0)]
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=1')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if m.reply_to_message and m.reply_to_message.video and user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        resolution = [m.reply_to_message.video.width, m.reply_to_message.video.height]
        path = await c.download_media(m.reply_to_message)
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioVideoPiped(path, video_parameters=VideoParameters(*resolution)))
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.reply_to_message.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.reply_to_message.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))

@api.on_message(filters.group & (filters.regex(r'^(پخش ویدیو )') | filters.regex(r'^([Pp][Ll][Aa][Yy][Vv][Ii][Dd][Ee][Oo])')))
async def playvwefideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*kir(1), *kir(0)]
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    text = m.text
    text = text.replace('پخش ویدیو','')
    try:
        patt = re.search(r'^([Pp][Ll][Aa][Yy][Vv][Ii][Dd][Ee][Oo])',text)
        text = text.replace(patt[0],'')
    except:
        pass
    try:
        if text == '' or text == ' ':
            m.continue_propagation()
        req = await cli.get_chat(text)
    except:
        return await m.reply('کاربر مورد نظر یافت نشد !')
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=1')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if m.reply_to_message and m.reply_to_message.video and user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        resolution = [m.reply_to_message.video.width, m.reply_to_message.video.height]
        path = await c.download_media(m.reply_to_message)
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioVideoPiped(path, video_parameters=VideoParameters(*resolution)))
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
<b>⌯ **ویدیو در حال پخش میباشد** 🔊</b>
<b>⊹</b> از طرف : {m.from_user.mention(m.from_user.first_name)}
<b>⊹</b> تقدیم به :  <a href=tg://user?id={req.id}>{req.first_name}</a>
<b>⊹</b> ساعت : <code>{a}</code> 🕦
            ''',parse_mode=enums.ParseMode.HTML,reply_to_message_id=m.reply_to_message.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
<b>⌯ **ویدیو در حال پخش میباشد** 🔊</b>
<b>⊹</b> از طرف : {m.from_user.mention(m.from_user.first_name)}
<b>⊹</b> تقدیم به :  <a href=tg://user?id={req.id}>{req.first_name}</a>
<b>⊹</b> ساعت : <code>{a}</code> 🕦
            ''',parse_mode=enums.ParseMode.HTML,reply_to_message_id=m.reply_to_message.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(پخش)$') | filters.regex(r'^([Pp][Ll][Aa][Yy])$')))
async def playmuzwewfsic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*moz(1), *moz(0)]
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=0')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if (m.reply_to_message.audio or m.reply_to_message.voice) and user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        path = await m.reply_to_message.download()
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioPiped(path))
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **موزیک در حال پخش میباشد** **🔊**
**⊹** نام موزیک : {m.reply_to_message.audio.file_name.replace('.mp3','') if m.reply_to_message.audio!= None else 'ویس'}
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.reply_to_message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **موزیک در حال پخش میباشد** **🔊**
**⊹** نام موزیک : {m.reply_to_message.audio.file_name.replace('.mp3','') if m.reply_to_message.audio!= None else 'ویس'}
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.reply_to_message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(پخش )') | filters.regex(r'^([Pp][Ll][Aa][Yy])')))
async def playmusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*moz(1), *moz(0)]
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    text = m.text
    text = text.replace('پخش','')
    try:
        patt = re.search(r'^([Pp][Ll][Aa][Yy])',text)
        text = text.replace(patt[0],'')
    except:
        pass
    try:
        req = await cli.get_chat(text)
    except:
        return await m.reply('• کاربر مورد نظر یافت نشد !')
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=0')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if (m.reply_to_message.audio or m.reply_to_message.voice) and user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        path = await m.reply_to_message.download()
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioPiped(path))
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
<b>⌯ موزیک تقدیمی به {req.first_name} در حال پخش میباشد 🔊 </b>
<b>⊹</b> نام موزیک : {m.reply_to_message.audio.file_name.replace('.mp3','') if m.reply_to_message.audio!= None else 'ویس'}
<b>⊹</b> از طرف : {m.from_user.mention(m.from_user.first_name)}
<b>⊹</b> تقدیم به :  <a href=tg://user?id={req.id}>{req.first_name}</a>
<b>⊹</b> ساعت : <code>{a}</code> 🕦
                ''',reply_to_message_id=m.reply_to_message.id,parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
<b>⌯ موزیک تقدیمی به {req.first_name} در حال پخش میباشد 🔊 </b>
<b>⊹</b> نام موزیک : {m.reply_to_message.audio.file_name.replace('.mp3','') if m.reply_to_message.audio!= None else 'ویس'}
<b>⊹</b> از طرف : {m.from_user.mention(m.from_user.first_name)}
<b>⊹</b> تقدیم به :  <a href=tg://user?id={req.id}>{req.first_name}</a>
<b>⊹</b> ساعت : <code>{a}</code> 🕦
                ''',parse_mode=enums.ParseMode.HTML,reply_to_message_id=m.reply_to_message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))

@api.on_message(filters.group &  (filters.regex(r'^(پخش لینک ویدیو)') | filters.regex(r'^([Pp][Ll][Aa][Yy][Ll][Ii][Nn][Kk][Vv][Ii][Dd][Ee][Oo])')))
async def playmuzsdfwewfsic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    text = text.replace('پخش لینک ویدیو','').strip()
    try:
        patt = re.search(r'^([Pp][Ll][Aa][Yy][Ll][Ii][Nn][Kk][Vv][Ii][Dd][Ee][Oo])$',text)
        text = text.replace(patt[0], '').strip()
    except:
        pass
    horn = [*kir(1), *kir(0)]
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    if '.mp4' not in str(text) and '.mkv' not in str(text):
        return await m.reply('این لینک دانلود ویدیو نیست و امکان پخش وجود ندارد !')
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=1')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        path = text
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioVideoPiped(path), stream_type=StreamType().live_stream)
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
                ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
                ]))

@api.on_message(filters.group &  (filters.regex(r'^(پخش لینک)') | filters.regex(r'^([Pp][Ll][Aa][Yy][Ll][Ii][Nn][Kk])')))
async def playmuzsdfwewfsic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    text = text.replace('پخش لینک','').strip()
    try:
        patt = re.search(r'^([Pp][Ll][Aa][Yy][Ll][Ii][Nn][Kk])$',text)
        text = text.replace(patt[0], '').strip()
    except:
        pass
    horn = [*moz(1), *moz(0)]
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    if '.mp3' not in text:
        return await m.reply('• این لینک دانلود موزیک نیست و امکان پخش وجود ندارد !')
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=0')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    if user_id in access and chat_id in Ahur4:
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        path = text
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioPiped(path), stream_type=StreamType().live_stream)
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **موزیک در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **موزیک در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                ''',reply_to_message_id=m.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                    [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                    [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                    [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
                ]))

@api.on_message(filters.group & (filters.regex(r'^(توقف پخش)$') | filters.regex(r'^([Ss][Tt][Oo][Pp][Mm][Uu][Ss][Ii][Cc])$')))
async def stopmusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    if chat_id in playing and user_id in access:
        if os.path.exists(playing[chat_id]):
            os.remove(playing[chat_id])
        del playing[chat_id]
        await call_py.leave_group_call(chat_id)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **موزیک متوقف شد** **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                    ''',reply_to_message_id=m.id)
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **موزیک متوقف شد** **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
                    ''',reply_to_message_id=m.id)

@api.on_message(filters.group & (filters.regex(r'^(توقف ویدیو)$') | filters.regex(r'^([Ss][Tt][Oo][Pp][Vv][Ii][Dd][Ee][Oo])$')))
async def stopvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    if chat_id in playing:
        if os.path.exists(playing[chat_id]):
            os.remove(playing[chat_id])
        del playing[chat_id]
        await call_py.leave_group_call(chat_id)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** ویدیو متوقف شد **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 📅
                ''',reply_to_message_id=m.id)
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** ویدیو متوقف شد **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 📅
                ''',reply_to_message_id=m.id)

@api.on_message(filters.group & (filters.regex(r'^(نصب موزیک)$') | filters.regex(r'^([Aa][Dd][Dd][Mm][Uu][Ss][Ii][Cc])$')))
async def addmusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), mersad, sudo]
    if user_id not in access:
        return
    cur.execute('SELECT * FROM gp WHERE status=0')
    x = cur.fetchall()

    list_ = []
    if x == []:
        req = await c.get_chat(chat_id)
        namegp = req.title
        idgp = req.id
        linkgp = req.invite_link
        status = 0
        if linkgp == None:
            await m.reply('**⌯** لطفا ربات را در گروه فول ادمین کرده و مجددا تلاش کنید **!**')
            return
        try:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        await m.reply('**⌯** گروه به لیست موزیک اضافه شد !')
        return

    for i in x:
        list_.append(int(i[1]))
    if int(chat_id) in list_:
        await m.reply('**⌯** این گروه از قبل نصب شده است **!**')
        return
    else:
        cur.execute('SELECT * FROM limmit')
        xx = cur.fetchall()
        if xx == []:
            pass
        else:
            limitstatus = xx[0][0]
            limitcount = xx[0][1]
            if limitstatus == 0:
                pass
            else:
                if len(x) > limitcount:
                    await m.reply(f'سودو گرامی ظرفیت نصب تکمیل شده است و ظرفیت ربات • {limitcount} ! گروه میباشد')
                    return
        req = await c.get_chat(chat_id)
        namegp = req.title
        idgp = req.id
        linkgp = req.invite_link
        status = 0
        if linkgp == None:
            await m.reply('**⌯** لطفا ربات را در گروه فول ادمین کرده و مجددا تلاش کنید **!**')
            return
        try:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        await m.reply('**⌯** گروه به لیست موزیک اضافه شد **!**')
        return

@api.on_message(filters.group & (filters.regex(r'^(حذف موزیک)$') | filters.regex(r'^([Dd][Ee][Ll][Mm][Uu][Ss][Ii][Cc])$')))
async def delmusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), mersad, sudo]
    
    if user_id not in access:
        return
    
    cur.execute('SELECT * FROM gp WHERE status=0')
    x = cur.fetchall()
    if x == []:
        await m.reply('**⌯**هنوز گروهی برای دسترسی به پخش موزیک ثبت نکرده اید **!**')
        return
    
    try: cur.execute(f'DELETE FROM musicadmin WHERE idgp = {m.chat.id}')
    except: pass
    try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.chat.id} AND status=0')
    except: pass
    try: cur.execute(f'DELETE FROM charge WHERE idgp = {m.chat.id}')
    except: pass
    db.commit()
    await c.send_message(sudo,f'دیتای موزیک گروه {m.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
    await c.send_message(mersad,f'دیتای موزیک گروه {m.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
    await m.reply('دیتای موزیک حذف شد !')

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(ترفیع موزیک)$') | filters.regex(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])$')))
async def promotemusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    reply_id = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    

    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id} AND idadmin={reply_id}')
    if cur.fetchall() !=[]:
        await m.reply('**⌯** کاربر از قبل در لیست مدیران گروه وجود داشت  **!**')
    else:
        try:
            idgp = chat_id
            idadmin = reply_id
            nameadmin = m.reply_to_message.from_user.first_name
            query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(nameadmin)} به لیست مدیران موزیک اضافه شد **!**')
            return
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            idgp = chat_id
            idadmin = reply_id
            nameadmin = m.reply_to_message.from_user.first_name
            query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯**کاربر {m.reply_to_message.from_user.mention(nameadmin)} به لیست مدیران موزیک اضافه شد **!**')
            return

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(عزل موزیک)$') | filters.regex(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])$')))
async def demotemusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    reply_id = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]

    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id} AND idadmin={reply_id}')
    if cur.fetchall()==[]:
        await m.reply('**⌯** کاربر مورد نظر در لیست مدیران موزیک وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM musicadmin WHERE idgp={chat_id} AND idadmin={reply_id}')
        db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست مدیران موزیک حذف شد **!**')

@api.on_message(filters.group & (filters.regex(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])') | filters.regex(r'^(ترفیع موزیک)')))
async def prommus(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('ترفیع موزیک','').replace('@','')
    try:
        serch = re.search(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id} AND idadmin={req.id}')
    if cur.fetchall() !=[]:
        await m.reply('**⌯** کاربر از قبل در لیست مدیران گروه وجود داشت  **!**')
    else:
        try:
            idgp = chat_id
            idadmin = req.id
            nameadmin = req.first_name
            query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯** کاربر {nameadmin} به لیست مدیران موزیک اضافه شد **!**')
            return
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            idgp = chat_id
            idadmin = req.id
            nameadmin = req.first_name
            query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯**کاربر {nameadmin} به لیست مدیران موزیک اضافه شد **!**')
            return

@api.on_message(filters.group & (filters.regex(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])') | filters.regex(r'^(عزل موزیک)')))
async def demmus(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('عزل موزیک','').replace('@','')
    try:
        serch = re.search(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Mm][Uu][Ss][Ii][Cc])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id} AND idadmin={req.id}')
    if cur.fetchall()==[]:
        await m.reply('**⌯** کاربر مورد نظر در لیست مدیران موزیک وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM musicadmin WHERE idgp={chat_id} AND idadmin={req.id}')
        db.commit()
        await m.reply(f'**⌯** کاربر {req.first_name} از لیست مدیران موزیک حذف شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(لیست مدیران موزیک)$') | filters.regex(r'^([Ll][Ii][Ss][Tt][Mm][Uu][Ss][Ii][Cc])$')))
async def listmusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    if user_id not in access:
        return
    
    cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id}')
    koon = cur.fetchall()
    if koon == []:
        await m.reply('**⌯** لیست مدیران موزیک خالی میباشد **!**')
        return
    else:
        counter = 1
        char = ''
        for i in koon:
            char += f'❪{counter}❫ **-** [{i[2]}](tg://openmessage?user_id={i[1]}) **⊹** `{i[1]}`\n'
            counter += 1

        await m.reply('**⌯** لیست مدیران موزیک **:**\n┈┅───┤📋├───┅┈\n'+char)

@api.on_message(filters.group & filters.regex(r'^(پیکربندی موزیک)$') | filters.regex(r'^([Cc][Oo][Nn][Ff][Ii][Gg][Mm][Uu][Ss][Ii][Cc])$'))
async def peykarbandimusic(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    if user_id not in access:
        return
    async for i in c.get_chat_members(chat_id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
        cur.execute(f'SELECT * FROM musicadmin WHERE idgp={chat_id} AND idadmin={i.user.id}')
        if cur.fetchall() == []:
            try:
                query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                cur.execute(query,(chat_id, i.user.id, i.user.first_name))
                db.commit()
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                cur.execute(query,(chat_id, i.user.id, i.user.first_name))
                db.commit()
    await m.reply('**⌯** تمامی مدیران با موفقیت شناسایی و در ربات ترفیع یافتند **!**')

@api.on_message(filters.group & filters.regex(r'^(پاکسازی مدیران موزیک)$') | filters.regex(r'^([Dd][Ee][Ll][Cc][Oo][Nn][Ff][Ii][Gg][Mm][Uu][Ss][Ii][Cc])$'))
async def delconfigmus(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    if user_id not in access:
        return
    cur.execute(f'DELETE FROM musicadmin WHERE idgp={chat_id}')
    db.commit()
    await m.reply('**⌯** تمامی مدیران با موفقیت از لیست مدیران موزیک حذف شدند **!**')

@api.on_message(filters.group & (filters.regex(r'^(نصب ویدیو)$') | filters.regex(r'^([Aa][Dd][Dd][Vv][Ii][Dd][Ee][Oo])$')))
async def addvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), mersad, sudo]
    if user_id not in access:
        return
    cur.execute('SELECT * FROM gp WHERE status=1')
    x = cur.fetchall()

    list_ = []
    if x == []:
        req = await c.get_chat(chat_id)
        namegp = req.title
        idgp = req.id
        linkgp = req.invite_link
        status = 1
        if linkgp == None:
            await m.reply('**⌯** لطفا ربات را در گروه فول ادمین کرده و مجددا تلاش کنید **!**')
            return
        try:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        await m.reply('**⌯** گروه به لیست ویدیو اضافه شد **!**')
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(chat_id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به لیست گروه های ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به لیست گروه های ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        return

    for i in x:
        list_.append(int(i[1]))
    # cur.execute('SELECT * FROM limmit')
    # mameh = cur.fetchall()
    # if mameh[0] == 1:
    #     if len(list_) >= mameh[1]:
    #         await m.reply('ظرفیت نصب شما تکمیل است !')
    #         return
    if int(chat_id) in list_:
        await m.reply('**⌯** این گروه در لیست ویدیو وجود دارد **!**')
        return
    else:
        cur.execute('SELECT * FROM limmit')
        xx = cur.fetchall()
        if xx == []:
            pass
        else:
            limitstatus = xx[0][0]
            limitcount = xx[0][1]
            if limitstatus == 0:
                pass
            else:
                if len(x) > limitcount:
                    await m.reply(f'سودو گرامی ظرفیت نصب تکمیل شده است و ظرفیت ربات • {limitcount} ! گروه میباشد')
                    return
        req = await c.get_chat(chat_id)
        namegp = req.title
        idgp = req.id
        linkgp = req.invite_link
        status = 1
        if linkgp == None:
            await m.reply('**⌯** لطفا ربات را در گروه فول ادمین کرده و مجددا تلاش کنید **!**')
            return
        try:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            cur.execute(query, (namegp, idgp, linkgp, status))
            db.commit()
        await m.reply('**⌯** گروه به لیست ویدیو اضافه شد **!**')
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(chat_id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به لیست گروه های ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به لیست گروه های ویدیو اضافه شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.chat.title}`
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        return

@api.on_message(filters.group & (filters.regex(r'^(حذف ویدیو)$') | filters.regex(r'^([Dd][Ee][Ll][Vv][Ii][Dd][Ee][Oo])$')))
async def delvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), mersad, sudo]
    if user_id not in access:
        return
    
    cur.execute('SELECT * FROM gp WHERE status=1')
    x = cur.fetchall()
    if x == []:
        await m.reply('**⌯** لیست گروه های ویدیو خالی میباشد **!**')
        return
    
    try: cur.execute(f'DELETE FROM videoadmins WHERE idgp = {m.message.chat.id}')
    except: pass
    try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.message.chat.id} AND status=1')
    except: pass
    try: cur.execute(f'DELETE FROM charge2 WHERE idgp = {m.message.chat.id}')
    except: pass
    db.commit()
    await c.send_message(sudo,f'دیتای ویدیو گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
    await c.send_message(mersad,f'دیتای ویدیو گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
    await m.reply('دیتای ویدیو پاک شد !')

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(ترفیع ویدیو)$') | filters.regex(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])$')))
async def promotevideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    reply_id = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]

    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id} AND idadmin={reply_id}')
    if cur.fetchall() !=[]:
        await m.reply('**⌯** کاربر در لیست مدیران ویدیو وجود دارد **!**')
    else:
        try:
            idgp = chat_id
            idadmin = reply_id
            nameadmin = m.reply_to_message.from_user.first_name
            query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(nameadmin)} به لیست مدیران ویدیو اضافه شد **!**')
            return
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            idgp = chat_id
            idadmin = reply_id
            nameadmin = m.reply_to_message.from_user.first_name
            query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(nameadmin)} به لیست مدیران ویدیو اضافه شد **!**')
            return

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(عزل ویدیو)$') | filters.regex(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])$')))
async def demotevideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    reply_id = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]

    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id} AND idadmin={reply_id}')
    if cur.fetchall()==[]:
        await m.reply('**⌯** کاربر در لیست مدیران ویدیو وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM videoadmins WHERE idgp={chat_id} AND idadmin={reply_id}')
        db.commit()
        await m.reply(f'کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست مدیران ویدیو حذف شد !')

@api.on_message(filters.group & (filters.regex(r'^(ترفیع ویدیو)') | filters.regex(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])')))
async def promvid(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('ترفیع ویدیو','').replace('@','')
    try:
        serch = re.search(r'^([Pp][Rr][Oo][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id} AND idadmin={req.id}')
    if cur.fetchall() !=[]:
        await m.reply('**⌯** کاربر از قبل در لیست مدیران گروه وجود داشت  **!**')
    else:
        try:
            idgp = chat_id
            idadmin = req.id
            nameadmin = req.first_name
            query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯** کاربر {nameadmin} به لیست مدیران ویدیو اضافه شد **!**')
            return
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            idgp = chat_id
            idadmin = req.id
            nameadmin = req.first_name
            query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
            cur.execute(query,(idgp, idadmin, nameadmin))
            db.commit()
            await m.reply(f'**⌯**کاربر {nameadmin} به لیست مدیران ویدیو اضافه شد **!**')
            return

@api.on_message(filters.group & (filters.regex(r'^(عزل ویدیو)') | filters.regex(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])')))
async def demvid(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    text = text.replace('عزل ویدیو','').replace('@','')
    try:
        serch = re.search(r'^([Dd][Ee][Mm][Oo][Tt][Ee][Vv][Ii][Dd][Ee][Oo])',text)
        text = text.replace(serch[0], '')
    except:
        pass
    access = [*idsudos(), *idowner(), *creators(chat_id), mersad, sudo]
    user_id = m.from_user.id
    if user_id not in access:
        return
    try:
        req = await c.get_chat(text)
    except:
        await m.reply('کاربر یافت نشد !')
        return
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id} AND idadmin={req.id}')
    if cur.fetchall()==[]:
        await m.reply('**⌯** کاربر مورد نظر در لیست مدیران ویدیو وجود ندارد **!**')
    else:
        cur.execute(f'DELETE FROM videoadmins WHERE idgp={chat_id} AND idadmin={req.id}')
        db.commit()
        await m.reply(f'**⌯** کاربر {req.first_name} از لیست مدیران ویدیو حذف شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(لیست مدیران ویدیو)$') | filters.regex(r'^([Ll][Ii][Ss][Tt][Vv][Ii][Dd][Ee][Oo])$')))
async def listvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = []
    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        access.append(i[0])
    cur.execute('SELECT * FROM owner')
    for ii in cur.fetchall():
        access.append(ii[0])
    cur.execute('SELECT * FROM creators')
    for iii in cur.fetchall():
        access.append(iii[1])
    access.append(mersad)
    if user_id not in access:
        return
    
    cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id}')
    koon = cur.fetchall()
    if koon == []:
        await m.reply('**⌯** لیست مدیران ویدیو خالی میباشد **!**')
        return
    else:
        counter = 1
        char = ''
        for i in koon:
            char += f'❪{counter}❫ **-** [{i[2]}](tg://openmessage?user_id={i[1]}) **⊹** `{i[1]}`\n'
            counter += 1
        await m.reply('**⌯** لیست مدیران ویدیو **:**\n┈┅───┤📋├───┅┈\n'+char)

@api.on_message(filters.group & filters.regex(r'^(پیکربندی ویدیو)$') | filters.regex(r'^([Cc][Oo][Nn][Ff][Ii][Gg][Vv][Ii][Dd][Ee][Oo])$'))
async def peykarbandivideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = []
    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        access.append(i[0])
    cur.execute('SELECT * FROM owner')
    for ii in cur.fetchall():
        access.append(ii[0])
    cur.execute('SELECT * FROM creators')
    for iii in cur.fetchall():
        access.append(iii[1])
    access.append(mersad)
    if user_id not in access:
        return
    
    async for i in c.get_chat_members(chat_id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
        cur.execute(f'SELECT * FROM videoadmins WHERE idgp={chat_id} AND idadmin={i.user.id}')
        if cur.fetchall() == []:
            try:
                query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                cur.execute(query,(chat_id, i.user.id, i.user.first_name))
                db.commit()
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                cur.execute(query,(chat_id, i.user.id, i.user.first_name))
                db.commit()
    await m.reply('**⌯** تمامی مدیران با موفقیت شناسایی و در ربات ترفیع یافتند **!**')

@api.on_message(filters.group & filters.regex(r'^(پاکسازی مدیران ویدیو)$') | filters.regex(r'^([Dd][Ee][Ll][Cc][Oo][Nn][Ff][Ii][Gg][Vv][Ii][Dd][Ee][Oo])$'))
async def delconfigvid(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={chat_id}')
    ahu = cur.fetchall()
    if ahu == []:
        return
    else:
        pass
    access = []
    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        access.append(i[0])
    cur.execute('SELECT * FROM owner')
    for ii in cur.fetchall():
        access.append(ii[0])
    cur.execute('SELECT * FROM creators')
    for iii in cur.fetchall():
        access.append(iii[1])
    access.append(mersad)
    if user_id not in access:
        return
    cur.execute(f'DELETE FROM videoadmins WHERE idgp={chat_id}')
    db.commit()
    await m.reply('**⌯** تمامی مدیران از لیست مدیران ویدیو حذف شدند **!**')

@api.on_message(filters.group & (filters.regex(r'^(پخش خودکار)') | filters.regex(r'^([Aa][Uu][Tt][Oo][Pp][Ll][Aa][Yy])')))
async def autoplay(c:Client, m:Message):
    chat_id = m.chat.id
    text = m.text
    user_id = m.from_user.id
    horn = [*moz(1), *moz(0)]
    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
    a = hour + dat
    if chat_id not in horn:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    text = text.replace('پخش خودکار','')
    try:
        pat = re.search(r'([Aa][Uu][Tt][Oo][Pp][Ll][Aa][Yy])',text)
        text = text.replace(pat,'')
    except:
        pass
    
    reqmusic = json.loads(requests.get(f'https://api.pinigerteam.tk/v1/melobit?type=new=search&query={text}&limit=1').text)
    idmusicc = reqmusic['melobit'][0]['song']['id']
    musicinfo = json.loads(requests.get(f'https://api.pinigerteam.tk/v1/melobit?type=new=info&mode=song&id={idmusicc}').text)
    download128 = musicinfo['melobit']['audio']['medium']['url']
    download320 = musicinfo['melobit']['audio']['high']['url']
    download = ''
    if download320 != '':
        download = download320
    else:
        download = download128
    
    covermusic = musicinfo['melobit']['image']['cover']['url']
    mm = await m.reply('**⌯** درحال جستجوی موزیک مورد نظر **....**\n┈┅───┤🔎├───┅┈')
    try:
        try:
            cur.execute('SELECT * FROM channel')
            channel = cur.fetchall()
            mention_music = '🎧 سراسری : پخش خودکار موزیک 🔍' #edit
            mus = await cli.send_audio('me',download, caption=(mention_music if channel == [] else f'[{mention_music}]({channel[0][2]})'),reply_to_message_id=m.id)
        except:
            return await m.reply('• موزیک مورد نظر یافت نشد !')
    except MediaEmpty:
        return await m.reply('• مشکلی برای دانلود موزیک مورد نظر پیش امده است !')


    try:
        await call_py.leave_group_call(chat_id)
    except:
        pass
    # path = f'./downloads/a{user_id}.mp3'
    try:
        path = await mus.download()
        await mm.delete()
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(m.chat.id, AudioPiped(path))
        playing.update({m.chat.id: download})
        await mus.delete()
        try:
            await c.send_photo(m.chat.id, './mersad.jpg',f'''**⌯** **موزیک در حال پخش میباشد** **🔊**
**⊹** نام موزیک : {mus.audio.file_name.replace('.mp3','')}
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
''',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
            ]))
        except:
            await c.send_video(m.chat.id, './mersad.mp4',f'''**موزیک در حال پخش میباشد** **🔊**
**⊹** نام موزیک : {mus.audio.file_name.replace('.mp3','')}
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
''',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pausee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
            ]))
    except:
        pass

@api.on_message(filters.group & (filters.regex(r'^(سرچ)') | filters.regex(r'^([Ss][Ee][Aa][Rr][Cc][Hh])')))
async def searchmus(c:Client, m:Message):
    chat_id = m.chat.id
    horn = [*moz(1), *moz(0)]
    if chat_id not in horn:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    text = m.text
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    text = text.replace('سرچ','')
    try:
        pat = re.search(r'([Ss][Ee][Aa][Rr][Cc][Hh])',text)
        text = text.replace(pat[0],'')
    except:
        pass
    
    reqmusic = json.loads(requests.get(f'https://api.pinigerteam.tk/v1/melobit?type=new=search&query={text}&limit=1').text)
    idmusicc = reqmusic['melobit'][0]['song']['id']
    musicinfo = json.loads(requests.get(f'https://api.pinigerteam.tk/v1/melobit?type=new=info&mode=song&id={idmusicc}').text)

    covermusic = musicinfo['melobit']['image']['cover']['url']
    # timemusic = str(round(int(musicinfo['melobit']['duration']) / 60 , 1)).replace('.',':')
        
    download128 = musicinfo['melobit']['audio']['medium']['url']
    download320 = musicinfo['melobit']['audio']['high']['url']
    download = ''
    if download320 != '':
        download = download320
    else:
        download = download128
    try:
        try:
            await c.send_photo(chat_id,covermusic,caption=f'♪ کیفیت آهنگ : 320 📀',reply_to_message_id=m.id)
        except:
            pass
        try:
            cur.execute('SELECT * FROM channel')
            channel = cur.fetchall()
            mention_music = '🎧 سراسری : جستجوی موزیک 🔍' #edit
            await c.send_audio(chat_id,download, caption=(mention_music if channel == [] else f'[{mention_music}]({channel[0][2]})'),reply_to_message_id=m.id)
        except:
            await m.reply('• موزیک مورد نظر یافت نشد !')
    except MediaEmpty:
        await m.reply('• مشکلی برای دانلود موزیک مورد نظر پیش امده است !')

@api.on_message(filters.group & (filters.regex(r'^(صدای موزیک)') | filters.regex(r'^([Mm][Uu][Ss][Ii][Cc][Ss][Oo][Uu][Nn][Dd])')))
async def volume(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    if chat_id in playing or chat_id in playlis:
        text = m.text
        text = text.replace('صدای موزیک','')
        try:
            pat = re.search(r'([Mm][Uu][Ss][Ii][Cc][Ss][Oo][Uu][Nn][Dd])',text)
            text = text.replace(pat[0],'')
        except Exception as e:
            pass
        if int(text) < 1 or int(text) > 200:
            await m.reply('• لطفا عددی کوچک تر از 200 و بزرگ تر از 0 وارد کنید !')
            return
        await call_py.change_volume_call(chat_id,int(text))
        await m.reply(f'**⌯** صدای موزیک به{text} تنظیم شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(صدای ویدیو)') | filters.regex(r'^([Vv][Ii][Dd][Ee][Oo][Ss][Oo][Uu][Nn][Dd])')))
async def volume(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    if chat_id in playing:
        text = m.text
        text = text.replace('صدای ویدیو','')
        try:
            pat = re.search(r'([Ss][Ee][Tt][Vv][Oo][Ii][Cc][Ee])',text)
            text = text.replace(pat[0],'')
        except Exception as e:
            pass
        if int(text) < 1 or int(text) > 200:
            await m.reply('• لطفا عددی کوچک تر از 200 و بزرگ تر از 0 وارد کنید !')
            return
        await call_py.change_volume_call(chat_id,int(text))
        await m.reply(f'**⌯** صدای ویدیو به{text} تنظیم شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(مکث)$') | filters.regex(r'^([Pp][Aa][Uu][Ss][Ee])$')))
async def pause(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*allmusic(), *allvideo(), *idsudos(), *idowner(), *creators(chat_id), sudo, mersad]
    if user_id in access and (chat_id in playing or chat_id in playlis):
        await call_py.pause_stream(chat_id)
        await m.reply('__**⌯** پخش متوقف شد **!**__')

@api.on_message(filters.group & (filters.regex(r'^(ازسرگیری)$') | filters.regex(r'^([Rr][Ee][Ss][Uu][Mm][Ee])$')))
async def pause(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*allmusic(), *allvideo(), *idsudos(), *idowner(), *creators(chat_id), sudo, mersad]
    if user_id in access and (chat_id in playing or chat_id in playlis):
        await call_py.resume_stream(chat_id)
        await m.reply('__**⌯** پخش ازسرگیری شد **!**__')

@api.on_message(filters.user(mersad) & filters.regex(r'^(bank)$'))
async def a(c:Client, m:Message):
    await m.reply("**My sepah Bank :**\n➛‌ `5892101325981906`")

@api.on_message(filters.group & (filters.regex(r'^(تنظیم ادمین)$') | filters.regex(r'^([Ss][Ee][Tt][Aa][Dd][Mm][Ii][Nn])$')))
async def setowner(c:Client, m:Message):
    list_ = [mersad, sudo, *idsudos()]
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return
    
    cur.execute('SELECT * FROM owner')
    if cur.fetchall() == []:
        try:
            query = 'INSERT INTO owner(idowner, nameowner) VALUES(?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name))
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            query = 'INSERT INTO owner(idowner, nameowner) VALUES(?,?)'
            cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name))
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست ادمین های ربات اضافه شد **!**')
        return
    ـlist = []
    cur.execute('SELECT * FROM owner')
    for i in cur.fetchall():
        ـlist.append(i[0])
    if m.reply_to_message.from_user.id in ـlist:
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از قبل در لیست ادمین های ربات وجود داشت **!**')
        return
    else:
        query = 'INSERT INTO owner(idowner, nameowner) VALUES(?,?)'
        cur.execute(query, (m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name))
        db.commit()
        await m.reply(f'**⌯**کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} با موفقیت به لیست ادمین های ربات اضافه شد **!**')
        return

@api.on_message(filters.group & (filters.regex(r'^(حذف ادمین)$') | filters.regex(r'^([Rr][Ee][Mm][Aa][Dd][Mm][Ii][Nn])$')))
async def delowner(c:Client, m:Message):
    list_ = []
    cur.execute('SELECT * FROM sudo')
    for i in cur.fetchall():
        list_.append(i[0])
    list_.append(mersad)
    if m.from_user.id not in list_:
        return
    if not m.reply_to_message:
        return
    _list = []
    cur.execute('SELECT * FROM owner')
    for i in cur.fetchall():
        _list.append(i[0])
    if m.reply_to_message.from_user.id in _list:
        try:
            cur.execute(f'DELETE FROM owner WHERE idowner={m.reply_to_message.from_user.id}')
            db.commit()
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(f'DELETE FROM owner WHERE idowner={m.reply_to_message.from_user.id}')
            db.commit()
        await m.reply(f'**⌯** کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست ادمین های ربات حذف شد **!**')
        return
    else:
        await m.reply('**⌯** کاربر مورد نظر در لیست ادمین های ربات یافت نشد **!**')

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(افزودن به لیست)$') | filters.regex(r'^([Aa][Dd][Dd][Tt][Oo][Pp][Ll][Aa][Yy][Ll][Ii][Ss][Tt])$')))
async def addtoplay(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    if not m.reply_to_message.audio:
        return
    cur.execute(f'SELECT * FROM playlist WHERE idgp={chat_id}')
    x = cur.fetchall()
    if len(x) >= 10:
        await m.reply('**⌯** شما نمیتوانید بیشتر از 10 موزیک به لیست پخش اضافه کنید **!**')
        return
    path = await m.reply_to_message.download(f'./downloads/{chat_id}/{m.reply_to_message.audio.title.replace("/","")}.mp3')
    if x != None:
        koos = []
        for i in x:
            koos.append(i[1])
        if path in koos:
            await m.reply('**⌯** موزیک در لیست پخش وجود دارد **!**')
            return
        else:
            query = 'INSERT INTO playlist(idgp, path, duration) VALUES(?,?,?)'
            try:
                cur.execute(query, (chat_id,path,m.reply_to_message.audio.duration))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (chat_id,path,m.reply_to_message.audio.duration))
            db.commit()
            await m.reply(f'**⌯** موزیک **{m.reply_to_message.audio.title}** به لیست پخش اضافه شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(پاکسازی لیست پخش)$') | filters.regex(r'^([Cc][Ll][Ee][Aa][Nn][Pp][Ll][Aa][Yy][Ll][Ii][Ss][Tt])$')))
async def deltoplay(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    cur.execute('SELECT * FROM playlist')
    if cur.fetchall() == []:
        await m.reply('**⌯** لیست پخش خالی میباشد **!**')
        return
    else:
        cur.execute(f'DELETE FROM playlist WHERE idgp={chat_id}')
        await m.reply('**⌯** لیست پخش پاکسازی شد **!**')

@api.on_message(filters.group & (filters.regex(r'^(پخش لیست)$') | filters.regex(r'^([Pp][Ll][Aa][Yy][Ll][Ii][Ss][Tt])$')))
async def playlist(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    cur.execute(f'SELECT * FROM playlist WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        await m.reply('**⌯** لیست پخش خالی میباشد **!**')
        return
    try:
        await call_py.leave_group_call(chat_id)
    except:
        pass
    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
    a = hour + dat
    try:
        await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **لیست پخش در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** `وضعیت : درحال پخش`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
            ]))
    except:
        await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **لیست پخش در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** `وضعیت : درحال پخش`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutemus"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutemus")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'cls')]
            ]))
    
    for i in x:
        playlis.update({m.chat.id: i[1]})
        await call_py.join_group_call(chat_id, AudioPiped(i[1]))
        await asyncio.sleep(i[2]-1)
        await call_py.leave_group_call(chat_id)
        try:
            if playlis[chat_id]:
                del playlis[chat_id]
        except:
            pass

@api.on_message(filters.group & (filters.regex(r'^(توقف لیست)$') | filters.regex(r'^([Ss][Tt][Oo][Pp][Ll][Ii][Ss][Tt])$')))
async def stoplist(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    cur.execute(f'SELECT * FROM playlist WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        await m.reply('**⌯** لیست پخش خالی میباشد **!**')
        return
    try:
        await call_py.leave_group_call(chat_id)
    except:
        pass
    hour = jdatetime.datetime.now().strftime("%H:%M:%S")
    dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
    a = hour + dat
    await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **لیست پخش متوقف شد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 📅
            ''',reply_to_message_id=m.id)
    if playlis[chat_id]:
        del playlis[chat_id]

@api.on_message(filters.group & filters.reply & (filters.regex(r'^(حذف از لیست)$') | filters.regex(r'^([Dd][Ee][Ll][Ff][Rr][Oo][Mm][Pp][Ll][Aa][Yy][Ll][Ii][Ss][Tt])$')))
async def deltoplay(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    cur.execute(f'SELECT * FROM playlist WHERE path="{path85+str(chat_id)}/{m.reply_to_message.audio.title}.mp3"')
    if cur.fetchall() == []:
        await m.reply('• موزیک مورد نظر در لیست پخش موجود نیست !')
        return
    else:
        cur.execute(f'DELETE FROM playlist WHERE path="/home/websploit/Desktop/EveryThink/All/downloads/{chat_id}/{m.reply_to_message.audio.title}.mp3"')
        db.commit()
        await m.reply('• موزیک مورد نظر با موفقیت از لیست پخش حذف شد !')

@api.on_message(filters.group & (filters.regex(r'^(لیست پخش)$') | filters.regex(r'^([Ll][Ii][Ss][Tt][Pp][Ll][Aa][Yy][Ll][Ii][Ss][Tt])$')))
async def deltoplay(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idmusic(chat_id), *creators(chat_id), sudo, mersad, *allmusic()]
    if user_id not in access:
        return
    cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id} AND status=0')
    if cur.fetchall() == []:
        return
    cur.execute(f'SELECT * FROM playlist WHERE idgp={chat_id}')
    x = cur.fetchall()
    if x == []:
        await m.reply('• لیست خالی میباشد !')
        return
    char = ''
    for i in x:
        char += f'**Music Name** : {i[1].replace(f"{path85+str(chat_id)}/","").replace(".mp3","")}\n─┅━━━━━━━━✥━━━━━━━━┅─\n'
    await m.reply(char)

@api.on_message(filters.user(mersad) & filters.regex(r'^(نرخ فروش موزیک)$'))
async def kjfnjndf(c:Client, m:Message):
    textt = await c.ask(m.chat.id, '**نرخ پرداختی گروه ها را برای صاحب گروه ها به ازای هر گروه موزیک وارد کنید :\nبرای مثال (20000) به معنی 20 هزار تومان**')
    cur.execute(f'UPDATE money1 SET nerkh1={int(textt.text)} WHERE kos=1')
    db.commit()
    return await m.reply('• نرخ جدید با موفقیت ثبت شد !')

@api.on_message(filters.user(mersad) & filters.regex(r'^(نرخ فروش ویدیو)$'))
async def dnojndf(c:Client, m:Message):
    textt = await c.ask(m.chat.id, '**نرخ پرداختی گروه ها را برای صاحب گروه ها به ازای هر گروه ویدیو وارد کنید :\nبرای مثال (30000) به معنی 30 هزار تومان**')
    cur.execute(f'UPDATE money1 SET nerkh2={int(textt.text)} WHERE kos=1')
    db.commit()
    return await m.reply('• نرخ جدید با موفقیت ثبت شد !')

@api.on_message(filters.user(mersad) & filters.regex(r'^(تنظیم نرخ موزیک)$'))
async def kjfnjndf(c:Client, m:Message):
    textt = await c.ask(m.chat.id, '**نرخ پرداختی گروه ها را برای سودو ها به ازای هر گروه موزیک وارد کنید :\nبرای مثال (9000) به معنی 9 هزار تومان**')
    cur.execute(f'UPDATE money1 SET nerkh1={int(textt.text)} WHERE kos=2')
    db.commit()
    return await m.reply('• نرخ جدید با موفقیت ثبت شد !')

@api.on_message(filters.user(mersad) & filters.regex(r'^(تنظیم نرخ ویدیو)$'))
async def kjfnjndf(c:Client, m:Message):
    textt = await c.ask(m.chat.id, '**نرخ پرداختی گروه ها را برای سودو ها به ازای هر گروه ویدیو وارد کنید :\nبرای مثال (15000) به معنی 15 هزار تومان**')
    cur.execute(f'UPDATE money1 SET nerkh2={int(textt.text)} WHERE kos=2')
    db.commit()
    return await m.reply('• نرخ جدید با موفقیت ثبت شد !')

@api.on_message(filters.user(mersad) & filters.regex(r'^(تنظیم نرخ پایه)$'))
async def kjfnjndf(c:Client, m:Message):
    textt = await c.ask(m.chat.id, '**نرخ پرداختی پایه ربات را وارد کنید :\nبرای مثال (15000) به معنی 15 هزار تومان**')
    cur.execute(f'UPDATE paye SET nerkh={int(textt.text)} WHERE kos=1')
    db.commit()
    return await m.reply('• نرخ جدید با موفقیت ثبت شد !')

@api.on_message(filters.user([mersad,sudo]) & filters.regex(r'^(📑 دریافت فاکتور)$'))
async def kjfnjndf(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    cur.execute('SELECT * FROM money1')
    x = cur.fetchall()

    botmusic = x[1][1]
    botvideo = x[1][2]
    froshmusic = x[0][1]
    froshvideo = x[0][2]
    cur.execute('SELECT * FROM paye')
    x = cur.fetchall()
    paye = x[0][1]
    gpmus = 0
    cur.execute('SELECT * FROM charge WHERE status=0')
    for i in cur.fetchall():
        gpmus += 1
    cur.execute('SELECT * FROM charge WHERE status=1')
    for i in cur.fetchall():
        gpmus += 1
    gpvid = 0
    cur.execute('SELECT * FROM charge2 WHERE status=0')
    for i in cur.fetchall():
        gpvid += 1
    cur.execute('SELECT * FROM charge2 WHERE status=1')
    for i in cur.fetchall():
        gpvid += 1
    return await m.reply(f'''**◄ وضعیت فاکتور شما به شرح زیر است :**

◂ تعداد کل گروه ها موزیک : {len([*moz(0), *moz(1)])}
◂ تعداد کل گروه ها ویدیو : {len([*kir(0), *kir(1)])}

╕ نرخ هر گروه موزیک {botmusic} تومان است.
╛ نرخ هر گروه ویدیو {botvideo} تومان است.

─━━━━━━━━━━━━━━━━━━━─

▐ نرخ فروش موزیک : {froshmusic}

▐ نرخ فروش ویدیو : {froshvideo}

─━━━━━━━━━━━━━━━━━━━─

▐ مبلغ کل دریافتی شما از موزیک : {froshmusic * len([*moz(0), *moz(1)])}

▐ مبلغ کل دریافتی شما از ویدیو : {froshvideo * len([*kir(0), *kir(1)])}

─━━━━━━━━━━━━━━━━━━━─

**▐ هزینه پایه : {paye} تومان.**

▐** کل هزینه قابل پرداخت : {(botmusic * len([*moz(0), *moz(1)])) + (botvideo * len([*kir(0), *kir(1)])) + paye} تومان.**

• این فاکتور به صورت درخواستی صرفاً جهت اطلاع از هزینه ها ارسال شده است و قابل پرداخت نیست.
    ''')
    
@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^(تنظیم اعتبار)'))
async def etebbot(c:Client, m:Message):
    text = m.text.replace('تنظیم اعتبار','')
    try:
        text = int(text)
    except:
        return await m.reply('لطفا شارژ ربات را به صورت عدد و بر حسب روز وارد کنید !')
    cur.execute('SELECT * FROM etebar')
    if cur.fetchall() ==[]:
        query = 'INSERT INTO etebar(kos,start,end,status) VALUES(?,?,?,?)'
        
        try:
            an = time.time()
            goh1 = float(text * 86400)
            goh = an+goh1
            cur.execute(query,(1,an,goh,0))
        except sqlite3.OperationalError:
            an = time.time()
            goh1 = float(text * 86400)
            goh = an+goh1
            os.system('fuser -k database.sqlite')
            cur.execute(query,(1,an,goh,0))
        db.commit()
        return await m.reply('• ربات به مدت خواسته شده شارژ شد !')
    else:
        return await m.reply('• لطفا از دستور اپدیت اعتبار استفاده کنید !')

@api.on_message(filters.private & filters.user(mersad) & filters.regex(r'^(اپدیت اعتبار)'))
async def etebbot(c:Client, m:Message):
    text = m.text.replace('اپدیت اعتبار','')
    try:
        text = int(text)
    except:
        return await m.reply('• لطفا شارژ ربات را به صورت عدد و بر حسب روز وارد کنید !')
    cur.execute('SELECT * FROM etebar')
    if cur.fetchall() ==[]:
        return await m.reply('• لطفا از دستور تنظیم اعتبار استفاده کنید !')
    else:
        cur.execute(f'UPDATE etebar SET start={time.time()}, end={time.time() + float(text * 86400)} , status=0')
        db.commit()
        return await m.reply('• ربات به مدت خواسته شده شارژ شد !')

@api.on_message(filters.private & filters.user([mersad,sudo]) & filters.regex(r'^(📆 میزان اعتبار)'))
async def etebbot(c:Client, m:Message):
    cur.execute('SELECT * FROM etebar')
    x = cur.fetchall()
    try:
        nowh = round((x[0][2] - time.time()) / 86400, 0)
        nowm = round((x[0][2] - time.time()) / 60 / 60,0)
    except IndexError:
        return await m.reply('• لطفا ابتدا اعتباری برای ربات تنظیم کنید و سپس تلاش کنید !')
    if x[0][3] == 0 or x[0][3] == 1 or x[0][3] == 2:
        await m.reply(f'• ربات شما به مدت {nowh} روز اعتبار دارد !')
    elif x[0][3] == 3:
        await m.reply(f'• ربات شما به مدت {nowm} ساعت اعتبار دارد !')
    else:
        await m.reply('• ربات فاقد اعتبار میباشد !')

@api.on_message(filters.group & (filters.regex(r'^(حذف)$') | filters.regex(r'^([Dd][Ee][Ll][Ee][Tt][Ee])$')))
async def deletee(c:Client, m:Message):
    horn = [*moz(1), *moz(0), *kir(0), *kir(1)]
    if m.chat.id not in horn:
        return await m.reply("• گروه فاقد اعتبار میباشد !")
    access = [*idsudos(), *idowner(), mersad, sudo]
    if m.from_user.id in access:
        await m.reply('• لطفا یکی از گزینه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• حذف موزیک', callback_data = 'delmus'), InlineKeyboardButton(text = '• حذف ویدیو', callback_data = 'delvid')],
            [InlineKeyboardButton(text = '• حذف کلی', callback_data = 'delboth')],
            [InlineKeyboardButton(text = '• خروج ربات', callback_data = 'left')],
            [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closedel')]
        ]))

@api.on_message(filters.group & (filters.regex(r'^(شروع ویس کال)$') | filters.regex(r'^([Ss][Tt][Aa][Rr][Tt][Vv][Oo][Ii][Cc][Ee][Cc][Aa][Ll][Ll])$')))
async def startvoice(c:Client, m:Message):

    access = [*idsudos(), *idowner(), *idmusic(m.chat.id), *idvideo(m.chat.id), *creators(m.chat.id), sudo, mersad, *allmusic(), *allvideo()]
    if m.from_user.id not in access:
        return

    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,m.from_user.id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return

    Ahur4 = []
    cur.execute('SELECT * FROM gp WHERE status=0')
    for i in cur.fetchall():
        Ahur4.append(i[1])
    cur.execute('SELECT * FROM gp WHERE status=1')
    for i in cur.fetchall():
        Ahur4.append(i[1])

    if m.chat.id not in Ahur4:
        return

    try:
        await cli.send(
            CreateGroupCall(peer = await cli.resolve_peer(m.chat.id), random_id = random.randint(1,5000))
        )
        await m.reply('• تماس گروهی با موفقیت راه اندازی شد !')
    except:
        return await m.reply('• راه اندازی تماس گروهی به مشکل خورده است !')

@api.on_message(filters.group & filters.user([mersad,sudo]) & (filters.regex(r'^(بن همگانی)') | filters.regex(r'^([Bb][Aa][Nn][Aa][Ll][Ll])')))
async def kdjfo6(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    try:
        text = text.replace('بن همگانی','')
        patt = re.search(r'^([Bb][Aa][Nn][Aa][Ll][Ll])',text)
        text = text.replace(patt[0],'').strip()
    except: pass
    try: req = await c.get_chat(text)
    except: return await m.reply('• کاربر مورد نظر یافت نشد !')
    gp = [*moz(0), *moz(1), *kir(0), *kir(1)]
    for i in gp:
        try: await c.ban_chat_member(i,text)
        except: pass
    query = 'INSERT INTO banlist(idgp, ban) VALUES(?,?)'
    try:
        cur.execute(query, (m.chat.id, req.id))
    except sqlite3.OperationalError:
        os.system('fuser -k database.sqlite')
        cur.execute(query, (m.chat.id, req.id))
    db.commit()
    await m.reply(f'• کاربر {req.first_name} به لیست مسدود سراسری اضافه شد !')

@api.on_message(filters.group & filters.user([mersad,sudo]) & (filters.regex(r'^(ازاد همگانی)') | filters.regex(r'^([Uu][Nn][Bb][Aa][Nn][Aa][Ll][Ll])')))
async def kdjasfo6(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    text = m.text
    try:
        text = text.replace('ازاد همگانی','')
        patt = re.search(r'^([Uu][Nn][Bb][Aa][Nn][Aa][Ll][Ll])',text)
        text = text.replace(patt[0],'').strip()
    except: pass
    try: req = await c.get_chat(text)
    except: return await m.reply('• کاربر مورد نظر یافت نشد !')
    gp = [*moz(0), *moz(1), *kir(0), *kir(1)]
    for i in gp:
        try: await c.unban_chat_member(i,text)
        except: pass
    cur.execute(f'SELECT * FROM banlist WHERE ban = {req.id}')
    if cur.fetchall() != []:
        cur.execute(f'DELETE FROM banlist WHERE ban = {req.id}')
        db.commit()
    await m.reply(f'• کاربر {req.first_name} از لیست کاربران مسدود سراسری حذف شد !')

@api.on_message(filters.group & (filters.regex(r'^(پینگ)$') | filters.regex(r'^([Pp][Ii][Nn][Gg])$')))
async def kdjkjndjnskjvnksnxcnsdfo6(c:Client, m:Message):
    if m.from_user.id not in [*idsudos(), *idowner(), *creators(m.chat.id), *allmusic(), *allvideo(), *idmusic(m.chat.id), *idvideo(m.chat.id), sudo, mersad]:
        return
    send = random.choice([1, 0.8, 0.2, 0.03, 0.099, 0.6, 0.4, 0.02, 0.09, 0.23, 0.506, 0.19, 0.306, 0.225, 0.009, 0.208, 0.04,0.014,0.13,0.71, 0.29, 0.91, 0.66,0.07 ])
    recive = random.choice([0.012,0.05,0.09,0.06,0.057,0.063,0.091,0.031,0.08,0.07,0.0718,0.0645,0.015,0.042,0.069,0.085])
    await asyncio.sleep(0.5)
    am = await m.reply(f'**⋆ ربات هم اکنون آنلایْن میباشد !**')
    await asyncio.sleep(0.2)
    await am.edit('**⋆ ربات هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**')
    await asyncio.sleep(0.2)
    await am.edit(f'**⋆ ربات هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**\n↓ دریافت ·۰• {recive} ثانیه')
    await asyncio.sleep(0.2)
    await am.edit(f'**⋆ ربات هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**\n↓ دریافت ·۰• {recive} ثانیه\n↑ ارسال ·۰•  {send} ثانیه')

@api.on_message(filters.regex(r'^(تنظیم مدیای پاسخ)$') & filters.reply & filters.user([mersad, sudo]))
async def dmnaavuifkdmndafhjil652(c:Client, m:Message):
    media = 'photo' if m.reply_to_message.photo else 'gif' if m.reply_to_message.media else 'nothing'
    if media=='photo' and m.reply_to_message.photo:
        try:
            os.system('rm ./*.jpg')
            os.system('rm ./*.mp4')
        except:
            pass
        await m.reply_to_message.download('./mersad.jpg')
        await m.reply('• تصویر به عنوان مدیای پاسخ قرار گرفت !')
    elif media=='gif' and m.reply_to_message.media:
        try:
            os.system('rm ./*.jpg')
            os.system('rm ./*.mp4')
        except:
            pass
        await m.reply_to_message.download('./mersad.mp4')
        await m.reply('• گیف به عنوان مدیای پاسخ قرار گرفت !')

@api.on_message((filters.regex(r'^(پخش تیوی)$') | filters.regex(r'^([Pp][Ll][Aa][Yy][Tt][Vv])$')) & filters.group )
async def dmnaavdafhjil652(c:Client, m:Message):
    access = [*idsudos(), *idowner(), mersad, sudo, *creators(m.chat.id), *idvideo(m.chat.id), *allvideo()]
    if m.from_user.id in access:
        horn = [*kir(1), *kir(0)]
        if m.chat.id not in horn:
            return await m.reply("• گروه فاقد اعتبار میباشد !")
        await m.reply('• لطفا یکی از گزینه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• ماهواره', callback_data = 'mahvare'), InlineKeyboardButton(text = '• تلویزیون', callback_data = 'telev')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv')]
    ]))
    
@api.on_message(filters.group & (filters.regex(r'^(توقف تیوی)$') | filters.regex(r'^([Ss][Tt][Oo][Pp][Tt][Vv])$')))
async def stopvideo(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    if chat_id in playing:
        if os.path.exists(playing[chat_id]):
            os.remove(playing[chat_id])
        del playing[chat_id]
        await call_py.leave_group_call(chat_id)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **پخش تیوی متوقف شد** **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 📅
                ''',reply_to_message_id=m.id)
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **پخش تیوی متوقف شد** **🔇**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 📅
                ''',reply_to_message_id=m.id)

@api.on_message(filters.group & filters.reply & filters.regex(r'^(معاف اجبار)$'))
async def moafejbar(c:Client, m:Message):
    user_id = m.from_user.id
    if user_id not in [*idsudos(), *idowner(), *creators(m.chat.id), mersad, sudo]:
        return
    idgp = m.chat.id
    idadmin = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM ejbar WHERE idgp={idgp} AND idadmin={idadmin}')
    if cur.fetchall() != []:
        return await m.reply('• کاربر مورد نظر از قبل در لیست معافیت وجود داشت !')

    query = 'INSERT INTO ejbar(idgp, idadmin) VALUES(?,?)'
    try:
        cur.execute(query, (idgp, idadmin))
    except sqlite3.OperationalError:
        os.system('fuser -k database.sqlite')
        cur.execute(query, (idgp, idadmin))
    db.commit()
    return await m.reply(f'• کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} به لیست معافیت اضافه شد !')

@api.on_message(filters.group & filters.reply & filters.regex(r'^(تنظیم اجبار)$'))
async def moafejbar(c:Client, m:Message):
    user_id = m.from_user.id
    if user_id not in [*idsudos(), *idowner(), *creators(m.chat.id), mersad, sudo]:
        return
    idgp = m.chat.id
    idadmin = m.reply_to_message.from_user.id
    cur.execute(f'SELECT * FROM ejbar WHERE idgp={idgp} AND idadmin={idadmin}')
    if cur.fetchall() == []:
        return await m.reply('• کاربر مورد نظر در لیست معافیت وجود نداشت !')
    cur.execute(f'DELETE FROM ejbar WHERE idgp={idgp} AND idadmin={idadmin}')
    db.commit()
    return await m.reply(f'کاربر {m.reply_to_message.from_user.mention(m.reply_to_message.from_user.first_name)} از لیست معافیت حذف شد !')

@api.on_message(filters.group &  filters.regex(r'^(لیست معافیت)$'))
async def moafejbar(c:Client, m:Message):
    user_id = m.from_user.id
    if user_id not in [*idsudos(), *idowner(), *creators(m.chat.id), mersad, sudo]:
        return
    idgp = m.chat.id
    cur.execute(f'SELECT * FROM ejbar WHERE idgp = {idgp}')
    x = cur.fetchall()
    if x == []:
        return await m.reply('• لیست معافیت خالی میباشد !')
    else:
        charlist = ''
        for i in x:
            req = await cli.get_chat(i[1])
            charlist += f'{req.first_name} -> {req.id}\n'
        return await m.reply(f'**⌯** لیست معافیت **:**\n┈┅───┤📋├───┅┈\n{charlist}')

@cli.on_message(filters.group & filters.user([sudo, mersad]) & (filters.regex(r'^(پینگ)$') | filters.regex(r'^([Pp][Ii][Nn][Gg])$')))
async def kdjkjndjnsksssjvnksnxcnsdfo6(c:Client, m:Message):
    send = random.choice([1, 0.8, 0.2, 0.03,0.026,0.142,0.68,0.092, 0.099, 0.6, 0.4, 0.02, 0.09, 0.23, 0.506, 0.19, 0.306, 0.225, 0.009, 0.208, 0.04,0.014,0.13,0.71, 0.29, 0.91, 0.66,0.07 ])
    recive = random.choice([0.012,0.05,0.021,0.032,0.066,0.011,0.09,0.06,0.057,0.063,0.091,0.031,0.08,0.07,0.0718,0.0645,0.015,0.042,0.069,0.085])
    await asyncio.sleep(0.5)
    am = await m.reply(f'**⋆ هلپر هم اکنون آنلایْن میباشد !**')
    await asyncio.sleep(0.2)
    await am.edit('**⋆ هلپر هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**')
    await asyncio.sleep(0.2)
    await am.edit(f'**⋆ هلپر هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**\n↓ دریافت ·۰• {recive} ثانیه')
    await asyncio.sleep(0.2)
    await am.edit(f'**⋆ هلپر هم اکنون آنلایْن میباشد !**\n◍ زمان های سپری شده **:**\n↓ دریافت ·۰• {recive} ثانیه\n↑ ارسال ·۰•  {send} ثانیه')

@api.on_message(filters.group & (filters.regex(r'^([Yy][Oo][Uu][Tt][Uu][Bb][Ee][Pp][Ll][Aa][Yy])') | filters.regex(r'^(پخش یوتیوب)')))
async def dlutube(c:Client, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    horn = [*kir(1), *kir(0)]
    access = [*idsudos(), *idowner(), *idvideo(chat_id), *creators(chat_id), sudo, mersad, *allvideo()]
    if chat_id not in horn and user_id in access:
        await m.reply("• گروه فاقد اعتبار میباشد !")
        return
    if user_id not in access:
        return
    cur.execute('SELECT * FROM channel')
    ch = cur.fetchall()
    if ch == []:
        pass
    elif ch[0][3] == 0:
        pass
    else:
        wx = await checkjoin(c,m,user_id)
        if wx == None:
            pass
        elif wx == 'kir':
            return
        elif wx == 'kos':
            return
    text = m.text
    text = text.replace('پخش یوتیوب','')
    try:
        patt = re.search(r'^([Yy][Oo][Uu][Tt][Uu][Bb][Ee][Pp][Ll][Aa][Yy])',text)
        text = text.replace(patt[0], '')
    except:
        pass
    text = text.strip()
    if 'https://www.youtube.com/watch?v=' not in text:
        return await m.reply('''لینک وارد شده معتبر نیست !
لینک باید به صورت زیر باشد :
`https://www.youtube.com/watch?v=Ss5S5S5`
''')

    mp3_url = await utub(text)

    if 'googlevideo.com' not in mp3_url:
        return await m.reply('عملیات دانلود با شکست مواجه شد !')
    else:
        path = mp3_url
        print("Playing {} in {}".format(path, m.chat.title))
        await call_py.join_group_call(chat_id, AudioVideoPiped(path), stream_type = StreamType().live_stream)
        playing.update({m.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        try:
            await c.send_photo(chat_id, './mersad.jpg',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))
        except:
            await c.send_video(chat_id, './mersad.mp4',f'''
**⌯** **ویدیو در حال پخش میباشد** **🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** شناسه گروه : `{chat_id}`
**⊹** ساعت : `{a}` 🕦
            ''',reply_to_message_id=m.id,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text = '• در حال پخش',callback_data = 'a')],
                [InlineKeyboardButton(text='⏸ مکث',callback_data="pauseeee"), InlineKeyboardButton(text='⏹ توقف',callback_data="closeeee"), InlineKeyboardButton(text='▶️ ازسرگیری',callback_data="resumeeee")],
                [InlineKeyboardButton(text='🔇 بیصدا',callback_data="mutevid"), InlineKeyboardButton(text='🔊 باصدا',callback_data="unmutevid")],
                [InlineKeyboardButton(text = '• بستن', callback_data = 'clls')]
            ]))

@api.on_message(filters.group & (filters.regex(r'^([Hh][Ee][Ll][Pp])$') | filters.regex(r'^(راهنما)$')))
async def help(c:Client, m:Message):
    access = [*idmusic(m.chat.id), *allmusic(), *idvideo(m.chat.id), *allvideo(), *creators(m.chat.id), *idsudos(), *idowner(), sudo, mersad]
    if m.from_user.id in access:
        await m.reply('• یکی از گزینه های زیر را انتخاب نمایید : \n┈┅┅━┃صفحه اصلی┃━┅┅┈',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• سرچ و پخش خودکار', callback_data = 'helpvideo')],
            [InlineKeyboardButton(text = '• ارتقا و عزل', callback_data = 'helpmusic')],
            [InlineKeyboardButton(text = '• پخش ها', callback_data = 'inlinefun'),InlineKeyboardButton(text = '• کاربردی', callback_data = 'karbordi')],
            [InlineKeyboardButton(text = '• تیوی و لیست پخش', callback_data = 'inlinemanage')],
            [InlineKeyboardButton(text = '• بستن', callback_data = 'closehelp')],
        ]))

@api.on_message(filters.new_chat_members & filters.group )
async def banallchecker(c:Client, m:Message):
    cur.execute(f'SELECT * FROM banlist WHERE ban = {m.from_user.id}')
    if cur.fetchall() != []:
        await c.ban_chat_member(m.chat.id,m.from_user.id)
    sudo_list = [*idsudos(), *idowner(), sudo, mersad]
    if m.from_user.id in sudo_list:
        await api.promote_chat_member(chat_id = m.chat.id, user_id = m.from_user.id,privileges = ChatPrivileges(
            can_pin_messages=True,
            can_restrict_members=True,
            can_promote_members=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_manage_video_chats=True
            ))
        if m.from_user.id == mersad:
            toxt = '⋆ برنامه نویس ⋆'
            await api.set_administrator_title(m.chat.id,m.from_user.id,toxt)
        else:
            text = '⋆ پشتیبان ربات ⋆'
            await api.set_administrator_title(m.chat.id,m.from_user.id,text)
        if m.from_user.id != mersad:
                    await api.send_message(sudo,f'''
◄ یک سودو پس از وارد شدن به گپ **{m.chat.title}** ادمین شد !

┈┅━─━| **اطلاعات گروه** |━─━┅┈
◂ نام گروه : **{m.chat.title}**
◂ شناسه گروه : `{m.chat.id}`
◂ لینک گروه : [برای ورود کلیک کنید.]({m.chat.invite_link})

┈┅━─━| **اطلاعات سودو** |━─━┅┈
◂ نام سودو : **{m.from_user.first_name}**
◂ شناسه سودو : `{m.from_user.id}`
◂ یوزر نیم سودو :‌ @{m.from_user.username}
                    ''')
    


###################################################################################################
##########################################
###############################################################################################3

async def check(c:Client,m:Message):
    
    cur.execute('SELECT * FROM charge WHERE status=0')
    for i in cur.fetchall():
        now = time.time()
        end = i[4]
        h48 = end - 172800.1
        cur.execute('SELECT * FROM information WHERE id=1')
        information_tuple = []
        for ii in cur.fetchone():
            information_tuple.append(ii)
        if now > h48:
            cha = int(str(i[0]))
            try:
                global req
                req = await api.get_chat(chat_id = cha)
                global req2
                req2 = await api.get_chat(chat_id = i[1])
                cur.execute(f'UPDATE charge SET status=1 WHERE idgp={i[0]}')
                db.commit()
                cur.execute(f'SELECT * FROM charge WHERE idgp={i[0]}')
                for i in cur.fetchall():
                    saat = int(int(i[4] - time.time()) / 60 / 60)
                await api.send_message(sudo,
                    f'''
◄ تاریخ تمدید این گروه فرا رسید !

┈┅━─━| **اطلاعات گروه** |━─━┅┈
◂ نام گروه : **{req.title}**
◂ شناسه گروه : `{req.id}`
◂ اعتبار گروه : کمتر از {saat} ساعت
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})

┈┅━─━| **اطلاعات مالک گروه** |━─━┅┈
◂ نام مالک : **{req2.first_name}**
◂ شناسه مالک : `{req2.id}`
◂ یوزر نیم مالک : [کلیک کنید.](tg://openmessage?user_id={req2.id})
                    ''',disable_web_page_preview=True
                    )

                
                mp = [InlineKeyboardButton(text='☜ شارژ گروه توسط مدیر ربات ☞',url=f'https://t.me/{information_tuple[5]}')]
                mo = InlineKeyboardMarkup([mp])
                xs = await api.send_message(cha,f'''
⚠️ اعتبار گروه شما کمتر از {saat} ساعت میباشد !

◂ لطفاً جهت جلوگیری از خارج شدن ربات ، هرچه سریعتر به پشتیبانی‌ ربات مراجعه نمایید.
                ''',reply_markup=mo)
                try:
                    await xs.pin()
                except:
                    pass
            except Exception as e:
                print(e)
            try:
                await api.send_message(req2.id,f'''
**⚠️ مدیر گرامی اعتبار گروه شما رو به اتمام است !**

◂ لطفاً جهت جلوگیری از خارج شدن ربات ، هرچه سریعتر به پشتیبانی‌ ربات مراجعه نمایید.
**
🪧 نام گروه : {req.title}
⏳ زمان باقی مانده : {saat} ساعت**
                ''',reply_markup=mo)
            except:
                pass
            await asyncio.sleep(1)
        await asyncio.sleep(0.4)
    cur.execute('SELECT * FROM charge WHERE status=1')
    for i in cur.fetchall():
        now = time.time()
        end = i[4]
        if now > end:
            cha = int(str(i[0]))
            req = await api.get_chat(cha)
            req2 = await api.get_chat(i[1])
            cur.execute(f'UPDATE charge SET status=2 WHERE idgp={i[0]}')
            db.commit()
            await api.send_message(
                sudo,f'''
**◄ تاریخ تمدید این گروه فرا رسید !**

┈┅┅━━| **اطلاعات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})
┈┅┅━━| **صاحب گروه** |━━┅┅┈
◂ نام : `{req2.first_name}`
◂ شناسه : `{req2.id}`
◂ یوزرنیم :‌ @{req2.username}
                ''',disable_web_page_preview=True
            )
            mp = [InlineKeyboardButton(text='☜ شارژ گروه توسط مدیر ربات ☞',url=f'https://t.me/{information_tuple[5]}')]
            mo = InlineKeyboardMarkup([mp])
            try:
                await api.send_message(i[1],f'**◂ اعتبار گروه شما با نام {req.title} به پایان رسید !**',reply_markup=mo)
            except: pass
            xs = await api.send_message(cha,'**◂ اعتبار این گروه به پایان رسیده است، جهت شارژ مجدد به پشتیبانی مراجعه کنید !**',reply_markup=mo)
            try:
                await xs.pin()
            except: pass
            await asyncio.sleep(1)
            cur.execute('SELECT * FROM autoleft')
            if cur.fetchall()[0][0] == 1:
                try:
                    cur.execute(f'DELETE FROM musicadmin WHERE idgp = {req.id}')
                except:
                    pass
                try:
                    cur.execute(f'DELETE FROM gp WHERE idgp = {req.id} AND status=0')
                except:
                    pass
                try:
                    cur.execute(f'DELETE FROM charge WHERE idgp = {req.id}')
                except:
                    pass
                db.commit()
                try:
                    if req.id not in [*kir(0), kir(1)]:
                        try:
                            await api.leave_chat(req.id)
                        except: pass
                        try:
                            await cli.leave_chat(req.id)
                        except: pass
                except Exception as e:
                    print(e) 
                
        await asyncio.sleep(0.4)

async def check2(c:Client,m:Message):
    
    cur.execute('SELECT * FROM charge2 WHERE status=0')
    for i in cur.fetchall():
        cur.execute('SELECT * FROM information WHERE id=1')
        information_tuple = []
        for ii in cur.fetchone():
            information_tuple.append(ii)
        now = time.time()
        end = i[4]
        h48 = end - 172800.1
        if now > h48:
            cha = int(str(i[0]))
            try:
                global req
                req = await api.get_chat(chat_id = cha)
                global req2
                req2 = await api.get_chat(chat_id = i[1])
                cur.execute(f'UPDATE charge2 SET status=1 WHERE idgp={i[0]}')
                db.commit()
                cur.execute(f'SELECT * FROM charge2 WHERE idgp={i[0]}')
                for i in cur.fetchall():
                    saat = int(int(i[4] - time.time()) / 60 / 60)
                await api.send_message(sudo,
                    f'''
◄ تاریخ تمدید این گروه برای ویدیو فرا رسید !

┈┅━─━| **اطلاعات گروه** |━─━┅┈
◂ نام گروه : **{req.title}**
◂ شناسه گروه : `{req.id}`
◂ اعتبار گروه : کمتر از {saat} ساعت
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})

┈┅━─━| **اطلاعات مالک گروه** |━─━┅┈
◂ نام مالک : **{req2.first_name}**
◂ شناسه مالک : `{req2.id}`
◂ یوزر نیم مالک : [کلیک کنید.](tg://openmessage?user_id={req2.id})
                    ''',disable_web_page_preview=True
                    )

                cur.execute('SELECT * FROM information WHERE id=1')
                mp = [InlineKeyboardButton(text='☜ شارژ گروه توسط مدیر ربات ☞',url=f'https://t.me/{information_tuple[5]}')]
                mo = InlineKeyboardMarkup([mp])
                xs = await api.send_message(cha,f'''
⚠️ اعتبار گروه شما کمتر از {saat} ساعت میباشد !

◂ لطفاً جهت جلوگیری از خارج شدن ربات ، هرچه سریعتر به پشتیبانی‌ ربات مراجعه نمایید.
#Video
                ''',reply_markup=mo)
                try:
                    await xs.pin()
                except:
                    pass
            except Exception as e:
                print(e)
            try:
                await api.send_message(req2.id,f'''
**⚠️ مدیر گرامی اعتبار گروه ویدیو شما رو به اتمام است !**

◂ لطفاً جهت جلوگیری از خارج شدن ربات ، هرچه سریعتر به پشتیبانی‌ ربات مراجعه نمایید.
**
🪧 نام گروه : {req.title}
⏳ زمان باقی مانده : {saat} ساعت**
                ''',reply_markup=mo)
            except:
                pass
        await asyncio.sleep(0.5)
    cur.execute('SELECT * FROM charge2 WHERE status=1')
    for i in cur.fetchall():
        now = time.time()
        end = i[4]
        if now > end:
            cha = int(str(i[0]))
            req = await api.get_chat(cha)
            req2 = await api.get_chat(i[1])
            cur.execute(f'UPDATE charge2 SET status=2 WHERE idgp={i[0]}')
            db.commit()
            await api.send_message(
                sudo,f'''
**◄ تاریخ تمدید این گروه ویدیو فرا رسید !**

┈┅┅━━| **اطلاعات گروه** |━━┅┅┈
◂ نام گروه : `{req.title}`
◂ شناسه گروه : `{req.id}`
◂ لینک گروه : [برای ورود کلیک کنید.]({req.invite_link})
┈┅┅━━| **صاحب گروه** |━━┅┅┈
◂ نام : `{req2.first_name}`
◂ شناسه : `{req2.id}`
◂ یوزرنیم :‌ @{req2.username}
                '''
            )
            mp = [InlineKeyboardButton(text='☜ شارژ گروه توسط مدیر ربات ☞',url=f'https://t.me/{information_tuple[5]}')]
            mo = InlineKeyboardMarkup([mp])
            try:
                await api.send_message(i[1],f'**◂ اعتبار گروه شما با نام {req.title} به پایان رسید !**',reply_markup=mo)
            except:
                pass
            xs = await api.send_message(cha,'**◂ اعتبار ویدیو این گروه به پایان رسیده است، جهت شارژ مجدد به پشتیبانی مراجعه کنید !**',reply_markup=mo)
            try:
                await xs.pin()
            except:
                pass
            cur.execute('SELECT * FROM autoleft')
            if cur.fetchall()[0][0] == 1:
                try:
                    cur.execute(f'DELETE FROM videoadmins WHERE idgp = {req.id}')
                except:
                    pass
                try:
                    cur.execute(f'DELETE FROM gp WHERE idgp = {req.id} AND status=1')
                except:
                    pass
                try:
                    cur.execute(f'DELETE FROM charge2 WHERE idgp = {req.id}')
                except:
                    pass
                db.commit()
                try:
                    if req.id not in [*moz(0), moz(1)]:
                        try:
                            await api.leave_chat(req.id)
                        except: pass
                        try:
                            await cli.leave_chat(req.id)
                        except: pass
                except Exception as e:
                    return 
        await asyncio.sleep(0.4)

async def etebar(c:Client, m:Message):
    cur.execute('SELECT * FROM etebar')
    x = cur.fetchall()
    try:
        start = x[0][1]
        end = x[0][2]
        status = x[0][3]
    except IndexError:
        return

    cur.execute('SELECT * FROM money1')
    x = cur.fetchall()

    botmusic = x[0][1]
    botvideo = x[1][1]
    froshmusic = x[0][2]
    froshvideo = x[1][2]
    cur.execute('SELECT * FROM paye')
    x = cur.fetchall()
    paye = x[0][1]

    d5 = end - 432000.0
    d3 = end - 259200.0
    d1 = end - 86400.0
    if time.time() >= d5 and status == 0:
        a = await api.send_message(sudo, '• تنها پنج روز به اتمام اشتراک ربات شما باقی مانده است ، بعد از اتمام اشتراک ربات به صورت خودکار افلاین خواهد شد !')
        await a.pin(both_sides=True)
        b = await api.send_message(mersad, '• برنامه نویس عزیز تنها 5 روز به اتمام اشتراک این ربات باقی مانده است !')
        await b.pin(both_sides=True)
        cur.execute('UPDATE etebar SET status=1')
        db.commit()
    elif time.time() >= d3 and status == 1:
        a = await api.send_message(sudo, '• تنها سه روز به اتمام اعتبار ربات شما باقی مانده است ، بعد از اتمام اشتراک ربات به صورت خودکار افلاین خواهد شد !')
        await a.pin(both_sides=True)
        b = await api.send_message(mersad, '• برنامه نویس عزیز تنها سه روز به اتمام اشتراک این ربات باقی مانده است !')
        await b.pin(both_sides=True)
        cur.execute('UPDATE etebar SET status=2')
        db.commit()
    elif time.time() >= d1 and status == 2:
        a = await api.send_message(sudo, '• تنها یک روز به اتمام اعتبار ربات شما باقی مانده است ، بعد از اتمام اشتراک ربات به صورت خودکار افلاین خواهد شد !')
        await a.pin(both_sides=True)
        b = await api.send_message(mersad, '• برنامه نویس عزیز تنها یک روز به اتمام اشتراک این ربات باقی مانده است !')
        await b.pin(both_sides=True)
        cur.execute('UPDATE etebar SET status=3')
        db.commit()
    elif time.time() >= end and status == 3:
        a = await api.send_message(sudo, f'''
اعتبار ربات شما به اتمام رسید لطفا قبل از حذف دیتا جهت تسویه اقدام کنید !

◄ وضعیت فاکتور شما به شرح زیر است :

◂ تعداد کل گروه ها موزیک : {len([*moz(0), *moz(1)])}
◂ تعداد کل گروه ها ویدیو : {len([*kir(0), *kir(1)])}

╕ نرخ هر گروه موزیک {botmusic} تومان است.
╛ نرخ هر گروه ویدیو {botvideo} تومان است.

─━━━━━━━━━━━━━━━━━━━─

▐ نرخ فروش موزیک : {froshmusic}

▐ نرخ فروش ویدیو : {froshvideo}

─━━━━━━━━━━━━━━━━━━━─

▐ مبلغ کل دریافتی شما از موزیک : {froshmusic * len([*moz(0), *moz(1)])}

▐ مبلغ کل دریافتی شما از ویدیو : {froshvideo * len([*kir(0), *kir(1)])}

─━━━━━━━━━━━━━━━━━━━─

▐ هزینه پایه : {paye} تومان.

▐ کل هزینه قابل پرداخت : {(botmusic * len([*moz(0), *moz(1)])) + (botvideo * len([*kir(0), *kir(1)])) + paye} تومان.

• این فاکتور به صورت درخواستی صرفاً جهت اطلاع از هزینه ها ارسال شده است و قابل پرداخت نیست.
''')
        await a.pin(both_sides=True)
        b = await api.send_message(mersad, '• برنامه نویس عزیز اعتبار این ربات به پایان رسیده میتوانید از بخش پیام به سودو درخواست تسویه ربات بدهید ! !')
        await b.pin(both_sides=True)
        cur.execute('UPDATE etebar SET status=4')
        db.commit()

async def checkinfo(c:Client,m:Message):
    cur.execute('SELECT * FROM charge WHERE status=0 OR status=1 OR status=2')
    for i in cur.fetchall():
        try:
            req = await cli.get_chat(chat_id = int(i[0]))
            cur.execute(f'UPDATE charge SET name="{req.title}",link="{req.invite_link}" WHERE idgp={i[0]}')
            db.commit()
            await asyncio.sleep(0.5)
        except:
            pass

async def checkinfo2(c:Client,m:Message):
    cur.execute('SELECT * FROM charge2 WHERE status=0 OR status=1 OR status=2')
    for i in cur.fetchall():
        try:
            req = await cli.get_chat(chat_id = int(i[0]))
            cur.execute(f'UPDATE charge2 SET name="{req.title}",link="{req.invite_link}" WHERE idgp={i[0]}')
            db.commit()
            await asyncio.sleep(0.5)
        except:
            pass

@api.on_callback_query()
async def callback(c:Client, m:CallbackQuery):
    user_di = m.from_user.id
    kirsag = ""
    cur.execute('SELECT * FROM channel')
    kirsag = cur.fetchall()
    if kirsag == []:
        kirsag = 'https://t.me/fnvhfdmnfhjkc'
    else:
        kirsag = kirsag[0][2]
    information_tuple = []
    cur.execute('SELECT * FROM information WHERE id=1')
    for i in cur.fetchone():
        information_tuple.append(i)
    a = [InlineKeyboardButton(text='📚 اطلاعات بیشتر',callback_data='aboutus')]
    b = [InlineKeyboardButton(text='💻 خرید مستقیم از سازنده',url=f"https://t.me/{information_tuple[4]}")]
    d = [InlineKeyboardButton(text='▪️ کانال ربات',url=f"{kirsag}"),InlineKeyboardButton(text='▪️ گروه پشتیبانی',url=f"https://t.me/{information_tuple[3]}")]
    k = [InlineKeyboardButton(text='📮 خرید غیر مستقیم',url=f"https://t.me/{information_tuple[5]}")]
    global ab
    ab = InlineKeyboardMarkup([a,b,d,k])
    e = [InlineKeyboardButton(text='بازگشت 🔙',callback_data='back')]
    global back
    back = InlineKeyboardMarkup([e])
    data = m.data
    if data == 'aboutus':
        await m.edit_message_text(information_tuple[2],reply_markup=back)
        return
    if data == 'back':
        start = information_tuple[1]
        if 'MENTION' in start:
            start = start.replace('MENTION',m.from_user.mention(m.from_user.first_name))
        if 'BOLD' in start:
            start = start.replace('BOLD','**')
        if 'USERID' in start:
            start = start.replace('USERID',m.from_user.id)
        await m.edit_message_text(start,reply_markup=ab)
        return
    if user_di not in [mersad, sudo, *idsudos(), *idowner(), *idmusic(m.message.chat.id), *idvideo(m.message.chat.id), *allmusic(), *allmusic(), *creators(m.message.chat.id)]:
        return await m.answer('شما درخواست ندادی ! :)',show_alert = True)
    if data == 'closepannel':
        await m.edit_message_text('• پنل با موفقیت بسته شد !')
        return
    elif data == 'chargevideo' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        repl = [InlineKeyboardButton(text='• 1 ماه',callback_data="1mah1"),InlineKeyboardButton(text='•  2 ماه',callback_data="2mah1")]
        repl2 = [InlineKeyboardButton(text='• 3 ماه',callback_data="3mah1"),InlineKeyboardButton(text='• 4 ماه',callback_data="4mah1")]
        repl5 = [InlineKeyboardButton(text='• بازگشت',callback_data="back2")]
        repll = InlineKeyboardMarkup([repl, repl2, repl5])
        await m.edit_message_text('• مدت زمان اشتراک مورد نظر ربات را برای قابلیت پخش ویدیو انتخاب نمایید :', reply_markup=repll)
    elif data == 'chargemusic' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        repl = [InlineKeyboardButton(text='• 1 ماه',callback_data="1mah2"),InlineKeyboardButton(text='• 2 ماه',callback_data="2mah2")]
        repl2 = [InlineKeyboardButton(text='• 3 ماه',callback_data="3mah2"),InlineKeyboardButton(text='• 4 ماه',callback_data="4mah2")]
        repl5 = [InlineKeyboardButton(text='• بازگشت',callback_data="back2")]
        repll = InlineKeyboardMarkup([repl, repl2, repl5])
        await m.edit_message_text('• مدت زمان اشتراک مورد نظر ربات را برای قابلیت پخش موزیک انتخاب نمایید :', reply_markup=repll)
        return
    elif data == 'config' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        await m.edit_message_text('• یکی از گزینه های زیر را برای پیکربندی انتخاب نمایید :',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• پیکربندی ویدیو', callback_data = 'configvid'),InlineKeyboardButton(text = '• پیکربندی موزیک', callback_data = 'configmus')],
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'back1')]
        ]))
    elif data == 'back1' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• یکی از گزینه های زیر را انتخاب نمایید :',reply_markup=repll)
        return
    elif data == '1mah1' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return
        cur.execute(f'SELECT * FROM charge2 WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup=repll)
            return
        req = await c.get_chat(m.message.chat.id)
        query = '''INSERT INTO
        charge2(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (m.message.chat.id,lis[0],30,time.time(),(time.time() + float(int(30) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0],30,time.time(),(time.time() + float(int(30) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))

        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
        try:
            cur.execute(query, (m.message.chat.id,lis[0]))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0]))
        db.commit()

        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=1 ')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای یک ماه استفاده از قابلیت پخش ویدیو شارژ شد !',reply_markup=repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت یک ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت یک ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        return
    elif data == '2mah1' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge2 WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup=repll)
            return
        else:
            query = '''INSERT INTO
            charge2(idgp,idadmin,day,start,end,status,link,name)
            VALUES(?,?,?,?,?,?,?,?)
            '''
            try:
                cur.execute(query, (m.message.chat.id,lis[0],60,time.time(),(time.time() + float(int(60) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0],60,time.time(),(time.time() + float(int(60) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            db.commit()
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()

        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=1 ')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای دو ماه استفاده از قابلیت پخش ویدیو شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت دو ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت دو ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    elif data == '3mah1' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge2 WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup=repll)
            return
        else:
            query = '''INSERT INTO
            charge2(idgp,idadmin,day,start,end,status,link,name)
            VALUES(?,?,?,?,?,?,?,?)
            '''
            try:
                cur.execute(query, (m.message.chat.id,lis[0],90,time.time(),(time.time() + float(int(90) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0],90,time.time(),(time.time() + float(int(90) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            db.commit()
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=1 ')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای سه ماه استفاده از قابلیت پخش ویدیو شارژ شد !',reply_markup=repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت سه ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت سه ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    elif data == '4mah1' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge2 WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup = repll)
            return
        else:
            query = '''INSERT INTO
            charge2(idgp,idadmin,day,start,end,status,link,name)
            VALUES(?,?,?,?,?,?,?,?)
            '''
            try:
                cur.execute(query, (m.message.chat.id,lis[0],120,time.time(),(time.time() + float(int(120) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0],120,time.time(),(time.time() + float(int(120) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
            db.commit()
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=1 ')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 1))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای چهار ماه استفاده از قابلیت پخش ویدیو شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت چهار ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت چهار ماه برای قابلیت ویدیو شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    #------------------------------------------------------------------------------------------------------------------------------------#
    elif data == '1mah2' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup = repll)
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (m.message.chat.id,lis[0],30,time.time(),(time.time() + float(int(30) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0],30,time.time(),(time.time() + float(int(30) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        db.commit()

        
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=0')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای یک ماه استفاده از قابلیت پخش موزیک شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت یک ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت یک ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    elif data == '2mah2' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup = repll)
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (m.message.chat.id,lis[0],60,time.time(),(time.time() + float(int(60) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0],60,time.time(),(time.time() + float(int(60) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        db.commit()

        
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=0')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای دو ماه استفاده از قابلیت پخش موزیک شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت دو ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت دو ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    elif data == '3mah2' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب نمایید !')
            return

        cur.execute(f'SELECT * FROM charge WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup = repll)
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (m.message.chat.id,lis[0],90,time.time(),(time.time() + float(int(90) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0],90,time.time(),(time.time() + float(int(90) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        db.commit()

        
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=0')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای سه ماه استفاده از قابلیت پخش موزیک شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت سه ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت سه ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    elif data == '4mah2' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        req = await c.get_chat(m.message.chat.id)
        
        lis = []
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if i.status == enums.ChatMemberStatus.OWNER:
                lis.append(i.user.id)
        if lis == []:
            await m.edit_message_text('• مالک گروه یافت نشد لطفا گروه را بصورت دستوری از طریق پی وی ربات نصب کنید !')
            return

        cur.execute(f'SELECT * FROM charge WHERE idgp={m.message.chat.id}')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• این گروه از قبل در لیست گروه های نصب شده موجود میباشد !',reply_markup = repll)
            return
        query = '''INSERT INTO
        charge(idgp,idadmin,day,start,end,status,link,name)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        try:
            cur.execute(query, (m.message.chat.id,lis[0],120,time.time(),(time.time() + float(int(120) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k database.sqlite')
            cur.execute(query, (m.message.chat.id,lis[0],120,time.time(),(time.time() + float(int(120) * 24 * 60 * 60)),0,req.invite_link,m.message.chat.title))
        db.commit()

        
        cur.execute(f'SELECT * FROM creators WHERE idgp={m.message.chat.id} AND creator={lis[0]}')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO creators(idgp, creator) VALUES(?,?)'
            try:
                cur.execute(query, (m.message.chat.id,lis[0]))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k database.sqlite')
                cur.execute(query, (m.message.chat.id,lis[0]))
            db.commit()
        
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=0')
        if cur.fetchall() != []:
            pass
        else:
            query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
            try:
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            except sqlite3.OperationalError:
                os.system('sudo fuser -k cli.sqlite')
                cur.execute(query, (m.message.chat.title, m.message.chat.id, req.invite_link, 0))
            db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• ربات با موفقیت برای چهار ماه استفاده از قابلیت پخش موزیک شارژ شد !',reply_markup = repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه به مدت چهار ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه به مدت چهار ماه برای قابلیت موزیک شارژ شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
    #---------------------------------------------------------------------------------------------------------------------------------------#
    elif data == 'charge' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        repl = [InlineKeyboardButton(text='• شارژ ویدیو',callback_data="chargevideo"), InlineKeyboardButton(text='• شارژ موزیک',callback_data="chargemusic")]
        repl23 = [InlineKeyboardButton(text='• بازگشت',callback_data="back1")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl23, repl3])
        await m.edit_message_text('• یکی از گزینه های زیر را انتخاب نمایید :',reply_markup=repll)
    elif data == 'back2' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        repl = [InlineKeyboardButton(text='• شارژ ویدیو',callback_data="chargevideo"), InlineKeyboardButton(text='• شارژ موزیک',callback_data="chargemusic")]
        repl23 = [InlineKeyboardButton(text='• بازگشت',callback_data="back1")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl23, repl3])
        await m.edit_message_text('• یکی از گزینه های زیر را انتخاب نمایید :',reply_markup=repll)
    elif data == 'installvideo' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        if m.message.chat.invite_link == '' and m.message.chat.username == '':
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• لطفا ابتدا ربات ها را در گروه ادمین کنید :',reply_markup = repll)
            return
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=1')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• گروه شما از قبل در لیست گروه های ویدیو وجود داشت !',reply_markup=repll)
            return
        cur.execute('SELECT * FROM gp WHERE status=1')
        x = cur.fetchall()
        cur.execute('SELECT * FROM limmit')
        xx = cur.fetchall()
        if xx == []:
            pass
        else:
            limitstatus = xx[0][0]
            limitcount = xx[0][1]
            if limitstatus == 0:
                pass
            else:
                if len(x) > limitcount:
                    await m.edit_message_text(f'شما ظرفیت {limitcount} عددی خود را تکمیل کرده اید، لطفا یکی از گروه های قبلی را حذف کنید و دوباره تلاش کنید !')
                    return
        query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
        try:
            cur.execute(query, (m.message.chat.title, m.message.chat.id, m.message.chat.invite_link if m.message.chat.invite_link != '' else m.message.chat.username, 1))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(query, (m.message.chat.title, m.message.chat.id, m.message.chat.invite_link if m.message.chat.invite_link != '' else m.message.chat.username, 1))
        db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• گروه شما با موفقیت به لیست گروه های ویدیو اضافه شد !',reply_markup=repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه ویدیو نصب شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه ویدیو نصب شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        return
    elif data == 'installmusic' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        if m.message.chat.invite_link == '' and m.message.chat.username == '':
            await m.edit_message_text('• لطفا ابتدا ربات ها را در گروه ادمین نمایید !')
            return
        cur.execute(f'SELECT * FROM gp WHERE idgp={m.message.chat.id} AND status=0')
        if cur.fetchall() != []:
            repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
            repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
            repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
            repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
            repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
            await m.edit_message_text('• گروه شما از قبل در لیست گروه های موزیک وجود داشت !',reply_markup=repll)
            return
        cur.execute('SELECT * FROM gp WHERE status=0')
        x = cur.fetchall()
        cur.execute('SELECT * FROM limmit')
        xx = cur.fetchall()
        if xx == []:
            pass
        else:
            limitstatus = xx[0][0]
            limitcount = xx[0][1]
            if limitstatus == 0:
                pass
            else:
                if len(x) > limitcount:
                    await m.edit_message_text(f'شما ظرفیت {limitcount} عددی خود را تکمیل کرده اید، لطفا یکی از گروه های قبلی را حذف کنید و دوباره تلاش کنید !')
                    return
        query = 'INSERT INTO gp(namegp, idgp, linkgp, status) VALUES(?,?,?,?)'
        try:
            cur.execute(query, (m.message.chat.title, m.message.chat.id, m.message.chat.invite_link if m.message.chat.invite_link != '' else m.message.chat.username, 0))
        except sqlite3.OperationalError:
            os.system('sudo fuser -k cli.sqlite')
            cur.execute(query, (m.message.chat.title, m.message.chat.id, m.message.chat.invite_link if m.message.chat.invite_link != '' else m.message.chat.username, 0))
        db.commit()
        repl = [InlineKeyboardButton(text='• نصب ویدیو',callback_data="installvideo"), InlineKeyboardButton(text='• نصب موزیک',callback_data="installmusic")]
        repl2 = [InlineKeyboardButton(text='• پیکربندی',callback_data="config")]
        repl23 = [InlineKeyboardButton(text='• تنظیم شارژ',callback_data="charge"),InlineKeyboardButton(text='• افزودن هلپر',callback_data="addcli")]
        repl3 = [InlineKeyboardButton(text='• بستن پنل',callback_data="closepannel")]
        repll = InlineKeyboardMarkup([repl, repl2, repl23, repl3])
        await m.edit_message_text('• گروه شما با موفقیت به لیست گروه های موزیک اضافه شد !',reply_markup=repll)
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        reqme = await c.get_me()
        await c.send_message(mersad,f'''
**⇐یک گروه موزیک نصب شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        await c.send_message(sudo,f'''
**⇐یک گروه موزیک نصب شد !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
┈┅┅━━| **مشخصات ربات** |━━┅┅┈
◂ نام ربات : {reqme.first_name}
◂ شناسه : `{reqme.id}`
◂ نام کاربری : {"@"+reqme.username if reqme.username != None else 'ندارد !'}
    ''',disable_web_page_preview=True)
        return
    elif data == 'pausee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if user_id in access and chat_id in playing:
            await call_py.pause_stream(chat_id)
            await m.answer('• پخش با موفقیت مکث شد !',show_alert=True)
            return
    elif data == 'resumee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if user_id in access and chat_id in playing:
            await call_py.resume_stream(chat_id)
            await m.answer('• پخش با موفقیت از سرگیری شد !',show_alert=True)
            return
    elif data == 'closee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if chat_id in playing and user_id in access:
            if os.path.exists(playing[chat_id]):
                os.remove(playing[chat_id])
            del playing[chat_id]
            await call_py.leave_group_call(chat_id)
            await m.answer('• پخش با موفقیت متوقف شد !', show_alert=True)
            await m.message.delete()
            return
    elif data == 'pauseeee' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if user_id in access and chat_id in playing:
            await call_py.pause_stream(chat_id)
            await m.answer('• پخش با موفقیت مکث شد !',show_alert=True)
            return
    elif data == 'resumeeee' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if user_id in access and chat_id in playing:
            await call_py.resume_stream(chat_id)
            await m.answer('• پخش با موفقیت از سرگیری شد !',show_alert=True)
            return
    elif data == 'closeeee' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if chat_id in playing and user_id in access:
            if os.path.exists(playing[chat_id]):
                os.remove(playing[chat_id])
            del playing[chat_id]
            await call_py.leave_group_call(chat_id)
            await m.answer('• پخش با موفقیت متوقف شد !', show_alert=True)
            await m.message.delete()
            return
    elif data == 'clls' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if os.path.exists(playing[chat_id]) and user_id in access:
            await m.message.delete()
            await m.answer('• پنل با موفقیت بسته شد !', show_alert=True)
    elif data == 'pauseee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), sudo, mersad]
        if user_id in access and chat_id in playlis:
            await call_py.pause_stream(chat_id)
            await m.answer('• پخش با موفقیت مکث شد !',show_alert=True)
            return
    elif data == 'resumeee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), sudo, mersad]
        if user_id in access and chat_id in playlis:
            await call_py.resume_stream(chat_id)
            await m.answer('• پخش با موفقیت از سرگیری شد !',show_alert=True)
            return
    elif data == 'closeee' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if chat_id in playlis and user_id in access:
            if playlis[chat_id]:
                del playlis[chat_id]
            await call_py.leave_group_call(chat_id)
            await m.answer('• پخش با موفقیت متوقف شد !', show_alert=True)
            await m.message.delete()
            return
    elif data == 'cls' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*allvideo(), *allmusic(), *idsudos(), *idowner(), *creators(chat_id), *idmusic(chat_id), *idvideo(chat_id), sudo, mersad]
        if os.path.exists(playing[chat_id]) and user_id in access:
            await m.message.delete()
            await m.answer('• پنل با موفقیت بسته شد !', show_alert=True)
    elif data == 'clzz':
        chat_id = m.message.chat.id
        user_id = m.from_user.id
        access = [*idsudos(), *idowner(), sudo, mersad]
        if user_id in access:
            await m.message.delete()
            await m.answer('• پنل با موفقیت بسته شد !', show_alert=True)
    elif data == 'addcli' and user_di in [*idsudos(), *idowner(), mersad, sudo,*creators(m.message.chat.id)]:
        chat_id = m.message.chat.id
        cur.execute(f'SELECT * FROM gp WHERE idgp={chat_id}')
        if cur.fetchall() == []:
            return await m.edit_message_text('• لطفا ابتدا گروه را نصب کنید !')
        else:
            try:
                await cli.send_message(chat_id,'• ربات هلپر عضو گروه میباشد !')
                return
            except:
                pass
            try:
                linkgp = await c.export_chat_invite_link(chat_id)
            except:
                return await m.message.reply('• لطفا ربات را در گروه ادمین کنید !')

            await cli.join_chat(linkgp)
            
            reqme = await cli.get_me()
            try:
                await api.promote_chat_member(chat_id = m.message.chat.id, user_id = reqme.id, privileges = ChatPrivileges(
                            can_delete_messages=True,
                            can_pin_messages=True,
                            can_invite_users=True,
                            can_manage_video_chats=True))
                await cli.send_message(m.message.chat.id, '• هلپر با موفقیت جوین شد !')
            except:
                return await cli.send_message(m.message.chat.id,'لطفا ربات را در گروه ادمین کنید !')   
    elif data == 'delmus' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        try: cur.execute(f'DELETE FROM musicadmin WHERE idgp = {m.message.chat.id}')
        except: pass
        try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.message.chat.id} AND status=0')
        except: pass
        try: cur.execute(f'DELETE FROM charge WHERE idgp = {m.message.chat.id}')
        except: pass
        db.commit()
        await c.send_message(sudo,f'دیتای موزیک گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        await c.send_message(mersad,f'دیتای موزیک گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        return await m.edit_message_text(f'• تمام دیتاهای مربوط به موزیک گروه {m.message.chat.title} حذف شد ! ',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• حذف موزیک', callback_data = 'delmus'), InlineKeyboardButton(text = '• حذف ویدیو', callback_data = 'delvid')],
            [InlineKeyboardButton(text = '• حذف کلی', callback_data = 'delboth')],
            [InlineKeyboardButton(text = '• خروج ربات', callback_data = 'left')],
            [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closedel')]
        ]))
    elif data == 'delvid' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        try: cur.execute(f'DELETE FROM videoadmins WHERE idgp = {m.message.chat.id}')
        except: pass
        try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.message.chat.id} AND status=1')
        except: pass
        try: cur.execute(f'DELETE FROM charge2 WHERE idgp = {m.message.chat.id}')
        except: pass
        db.commit()
        await c.send_message(sudo,f'دیتای ویدیو گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        await c.send_message(mersad,f'دیتای ویدیو گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        return await m.edit_message_text(f'• تمام دیتاهای مربوط به ویدیو گروه {m.message.chat.title} حذف شد ! ',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• حذف موزیک', callback_data = 'delmus'), InlineKeyboardButton(text = '• حذف ویدیو', callback_data = 'delvid')],
            [InlineKeyboardButton(text = '• حذف کلی', callback_data = 'delboth')],
            [InlineKeyboardButton(text = '• خروج ربات', callback_data = 'left')],
            [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closedel')]
        ]))
    elif data == 'delboth' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        try: cur.execute(f'DELETE FROM musicadmin WHERE idgp = {m.message.chat.id}')
        except: pass
        try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.message.chat.id} AND status=0')
        except: pass
        try: cur.execute(f'DELETE FROM charge WHERE idgp = {m.message.chat.id}')
        except: pass
        try: cur.execute(f'DELETE FROM videoadmins WHERE idgp = {m.message.chat.id}')
        except: pass
        try: cur.execute(f'DELETE FROM gp WHERE idgp = {m.message.chat.id} AND status=1')
        except: pass
        try: cur.execute(f'DELETE FROM charge2 WHERE idgp = {m.message.chat.id}')
        except: pass
        db.commit()
        await c.send_message(sudo,f'دیتای موزیک و ویدیوی گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        await c.send_message(mersad,f'دیتای موزیک و ویدیوی گروه {m.message.chat.title} توسط {m.from_user.mention(m.from_user.first_name)} کاملا حذف شد !')
        await m.edit_message_text(f'• تمام دیتاهای مربوط به ویدیو و موزیک گروه {m.message.chat.title} حذف شد ! ',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• حذف موزیک', callback_data = 'delmus'), InlineKeyboardButton(text = '• حذف ویدیو', callback_data = 'delvid')],
            [InlineKeyboardButton(text = '• حذف کلی', callback_data = 'delboth')],
            [InlineKeyboardButton(text = '• خروج ربات', callback_data = 'left')],
            [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closedel')]
        ]))
    elif data == 'left' and user_di in [*idsudos(),  mersad, sudo]:
        await m.edit_message_text('**⌯** ربات از این گروه خارج میشود **!**')
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        req = await c.get_chat(m.message.chat.id)
        await c.send_message(sudo,f'''
**⇐ یکی از سودو ها دستور لفت را استفاده کرد ! !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
        ''',disable_web_page_preview=True)
        await c.send_message(mersad,f'''
**⇐ یکی از سودو ها دستور لفت را استفاده کرد ! !**

◂ تاریخ : {a}
┈┅┅━━| **مشخصات گروه** |━━┅┅┈
◂ نام گروه : `{m.message.chat.title}`
◂ شناسه گروه : `{m.message.chat.id}`
◂ لینک گروه : [برای ورود به گروه کلیک کنید.]({req.invite_link})
┈┅┅━━| **مشخصات همکار** |━━┅┅┈
◂ نام : `{m.from_user.first_name}`
◂ یوزرنیم : @{m.from_user.username}
◂ آیدی عددی : `{m.from_user.id}`
        ''',disable_web_page_preview=True)
        await c.leave_chat(m.message.chat.id)
        try:
            await cli.leave_chat(m.message.chat.id)
        except:
            pass
    elif data == 'closedel' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        await m.message.delete()
        await m.answer('پنل با موفقیت بسته شد !',show_alert = True)
    elif data == 'configmus' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        cur.execute(f'SELECT * FROM gp WHERE status=0 AND idgp={m.message.chat.id}')
        ahu = cur.fetchall()
        if ahu == []:
            return
        else:
            pass
        async for i in c.get_chat_members(m.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            cur.execute(f'SELECT * FROM musicadmin WHERE idadmin={i.user.id}')
            if cur.fetchall() == []:
                try:
                    query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                    cur.execute(query,(m.message.chat.id, i.user.id, i.user.first_name))
                    db.commit()
                except sqlite3.OperationalError:
                    os.system('sudo fuser -k cli.sqlite')
                    query = 'INSERT INTO musicadmin(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                    cur.execute(query,(m.message.chat.id, i.user.id, i.user.first_name))
                    db.commit()
        await m.edit_message_text('**⌯** تمامی مدیران با موفقیت شناسایی و در بخش موزیک ربات ترفیع یافتند **!**',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• پیکربندی ویدیو', callback_data = 'configvid'),InlineKeyboardButton(text = '• پیکربندی موزیک', callback_data = 'configmus')],
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'back1')]
        ]))
    elif data == 'configvid' and user_di in [*idsudos(), *idowner(), mersad, sudo]:
        cur.execute(f'SELECT * FROM gp WHERE status=1 AND idgp={m.message.chat.id}')
        ahu = cur.fetchall()
        if ahu == []:
            return
        else:
            pass
        
        async for i in c.get_chat_members(m.message.chat.id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
            cur.execute(f'SELECT * FROM videoadmins WHERE idadmin={i.user.id}')
            if cur.fetchall() == []:
                try:
                    query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                    cur.execute(query,(m.message.chat.id, i.user.id, i.user.first_name))
                    db.commit()
                except sqlite3.OperationalError:
                    os.system('sudo fuser -k cli.sqlite')
                    query = 'INSERT INTO videoadmins(idgp, idadmin, nameadmin) VALUES(?,?,?)'
                    cur.execute(query,(m.message.chat.id, i.user.id, i.user.first_name))
                    db.commit()
        await m.edit_message_text('**⌯** تمامی مدیران با موفقیت شناسایی و در بخش ویدیو ربات ترفیع یافتند **!**',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• پیکربندی ویدیو', callback_data = 'configvid'),InlineKeyboardButton(text = '• پیکربندی موزیک', callback_data = 'configmus')],
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'back1')]
        ]))
    elif data == 'telev' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.edit_message_text('• جهت پخش، یکی از شبکه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• شبکه 2', callback_data = 'tv2'), InlineKeyboardButton(text = '• شبکه 1', callback_data = 'tv1')],
        [InlineKeyboardButton(text = '• شبکه 5', callback_data = 'tv5'), InlineKeyboardButton(text = '• شبکه 3', callback_data = 'tv3')],
        [InlineKeyboardButton(text = '• شبکه آی‌فیلم', callback_data = 'ifilm'), InlineKeyboardButton(text = '• شبکه خبر', callback_data = 'news')],
        [InlineKeyboardButton(text = '• شبکه نمایش', callback_data = 'namayesh'), InlineKeyboardButton(text = '• شبکه نسیم', callback_data = 'nasim')],
        [InlineKeyboardButton(text = '• شبکه تماشا', callback_data = 'hdtest'), InlineKeyboardButton(text = '• شبکه ورزش', callback_data = 'varzesh')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv'), InlineKeyboardButton(text = '• بازگشت', callback_data = 'backahura')]
        ]))
    elif data == 'closetv' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.answer('• پنل بسته شد !',show_alert = True)
        await m.message.delete()
    elif data == 'tv1' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try: await call_py.leave_group_call(m.message.chat.id)
        except: pass
        path = 'https://cdn.telewebion.com/tv1/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه یک در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه یک در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'tv2' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/tv2/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه دو در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه دو در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'tv3' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/tv3/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه سه در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه سه در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'tv5' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/tehran/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه پنج در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه پنج در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'news' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try: await call_py.leave_group_call(m.message.chat.id)
        except: pass
        path = 'https://cdn.telewebion.com/irinn/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه خبر در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه خبر در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'ifilm' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/ifilm/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه آی‌ فیلم در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه آی‌ فیلم در حال پخش میباشد ! 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'nasim' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/nasim/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه نسیم در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه نسیم در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'namayesh' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try: await call_py.leave_group_call(m.message.chat.id)
        except: pass
        path = 'https://cdn.telewebion.com/namayesh/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه نمایش در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه نمایش در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'varzesh' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://cdn.telewebion.com/varzesh/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه ورزش در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه ورزش در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'hdtest' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try: await call_py.leave_group_call(m.message.chat.id)
        except: pass
        path = 'https://cdn.telewebion.com/hdtest/live/720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه تماشا در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه تماشا در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'backtv' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.message.delete()
        await m.message.reply('• جهت پخش، یکی از شبکه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• شبکه 2', callback_data = 'tv2'), InlineKeyboardButton(text = '• شبکه 1', callback_data = 'tv1')],
        [InlineKeyboardButton(text = '• شبکه 5', callback_data = 'tv5'), InlineKeyboardButton(text = '• شبکه 3', callback_data = 'tv3')],
        [InlineKeyboardButton(text = '• شبکه آی‌فیلم', callback_data = 'ifilm'), InlineKeyboardButton(text = '• شبکه خبر', callback_data = 'news')],
        [InlineKeyboardButton(text = '• شبکه نمایش', callback_data = 'namayesh'), InlineKeyboardButton(text = '• شبکه نسیم', callback_data = 'nasim')],
        [InlineKeyboardButton(text = '• شبکه تماشا', callback_data = 'hdtest'), InlineKeyboardButton(text = '• شبکه ورزش', callback_data = 'varzesh')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv'), InlineKeyboardButton(text = '• بازگشت', callback_data = 'backahura')]
        ]))
    elif data == 'mahvare' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.edit_message_text('• جهت پخش، یکی از شبکه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• BBC', callback_data = 'bbc'), InlineKeyboardButton(text = '• ManotoTv', callback_data = 'manoto')],
        [InlineKeyboardButton(text = '• AvaFamily', callback_data = 'avafamily'), InlineKeyboardButton(text = '• AvaSeries', callback_data = 'avaseries')],
        [InlineKeyboardButton(text = '• FarsiTv', callback_data = 'farsitv'), InlineKeyboardButton(text = '• PMC', callback_data = 'pmc')],
        [InlineKeyboardButton(text = '• Vox 2', callback_data = 'vox2'), InlineKeyboardButton(text = '• Vox 1', callback_data = 'vox1')],
        [InlineKeyboardButton(text = '• NavahangMusic', callback_data = 'navahang'), InlineKeyboardButton(text = '• RadioJavan', callback_data = 'radiojavan')],
        [InlineKeyboardButton(text = '• IranInternational', callback_data = 'iraninternational'), InlineKeyboardButton(text = '• ITN', callback_data = 'itn')],
        [InlineKeyboardButton(text = '• GemTv', callback_data = 'gemtv'), InlineKeyboardButton(text = '• OxirTv', callback_data = 'owirtv')],
        [InlineKeyboardButton(text = '• GemRubix', callback_data = 'gemrubix'), InlineKeyboardButton(text = '• GemRiver', callback_data = 'gemriver')],
        [InlineKeyboardButton(text = '• GemBollywood', callback_data = 'gembollywood'), InlineKeyboardButton(text = '• GemSeries', callback_data = 'gemseries')],
        [InlineKeyboardButton(text = '• GemJunior', callback_data = 'gemjunior'), InlineKeyboardButton(text = '• GemDrama', callback_data = 'gemdrama')],
        [InlineKeyboardButton(text = '• GemFilm', callback_data = 'gemfilm'), InlineKeyboardButton(text = '• GemMaxx', callback_data = 'gemmaxx')],
        [InlineKeyboardButton(text = '• BBC Persian', callback_data = 'bbcpersian'), InlineKeyboardButton(text = '• MBC Persia', callback_data = 'mbcpersia')],
        [InlineKeyboardButton(text = '• Tapesh 1', callback_data = 'tapesh1'), InlineKeyboardButton(text = '• Tapesh 2', callback_data = 'tapesh2')],
        [InlineKeyboardButton(text = '• PersianaTv', callback_data = 'persiana'), InlineKeyboardButton(text = '• PMC Royale', callback_data = 'pmcr')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv'), InlineKeyboardButton(text = '• بازگشت', callback_data = 'backahura')]
        ]))
    elif data == 'pmcr' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.29/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه PMC Royale در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه PMC Royale در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'persiana' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.22/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه  PersianaTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه PersianaTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'tapesh2' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://208.113.204.104:8123/live/tapesh-live-stream/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه Tapesh 2 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه Tapesh 2 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'mbcpersia' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://shls-mbcpersia-prod-dub.shahid.net/out/v1/bdc7cd0d990e4c54808632a52c396946/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه MBC Persia در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه  MBC Persia در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'tapesh1' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://iptv.tapesh.tv/tapesh/playlist.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه Tapesh 1 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه Tapesh 1 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'bbcpersian' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://vs-hls-pushb-ww-live.akamaized.net/x=3/i=urn:bbc:pips:service:bbc_persian_tv/pc_hd_abr_v2_akamai_hls_live.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه BBC Persian در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه BBC Persian در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemriver' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/river/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemRiver در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemRiver در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemrubix' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/rubix/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemRubix در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemRubix در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemseries' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gemseries/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemSeries در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemSeries در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gembollywood' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gembollywood/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemBollywood در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemBollywood در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemdrama' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gemdrama/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemDrama در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemDrama در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemjunior' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gemjunior/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemJunior در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemJunior در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemmaxx' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gemmaxx/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemMaxx در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemMaxx در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemfilm' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gemfilm/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemFilm در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemFilm در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'manoto' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://d2rwmwucnr0d10.cloudfront.net/live_750.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه ManotoTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه ManotoTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'bbc' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://vs-hls-pushb-ww-live.akamaized.net/x=3/i=urn:bbc:pips:service:bbc_persian_tv/t=3840/v=pv5/b=437056/main.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه BBC در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه BBC در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'avaseries' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.4/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه AvaSeries در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه AvaSeries در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'avafamily' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.5/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه AvaFamily در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه AvaFamily در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'pmc' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://hls.pmchd.live/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه PMC در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه PMC در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'farsitv' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://live.farsitv.de/live/stream_720p/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه FarsiTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه FarsiTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'vox1' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.8/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه Vox 1 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه Vox 1 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'vox2' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.199.9/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه Vox 2 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه Vox 2 در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'radiojavan' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream.rjtv.stream/live/smil:rjtv.smil/playlist.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه RadioJavan در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه RadioJavan در حال پخش میباشد🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'navahang' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.210.227.130/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه NavahangMusic در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه NavahangMusic در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'itn' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://livestream.5centscdn.com/itnapp/4e0ea63032b868402b61d3a35e7ca168.sdp/chunks.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه ITN در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه ITN در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'iraninternational' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://live.playstop.me/1816184091/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه IranInternational در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه IranInternational در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'owirtv' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'http://51.254.225.26/hls/stream.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه OxirTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه OxirTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'gemtv' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        try:
            await call_py.leave_group_call(m.message.chat.id)
        except:
            pass
        path = 'https://stream-live.gemonline.tv/live/gem/index.m3u8'
        print("Playing {} in {}".format(path, m.message.chat.title))
        await call_py.join_group_call(m.message.chat.id, AudioVideoPiped(path),stream_type=StreamType().live_stream)
        playing.update({m.message.chat.id: path})
        hour = jdatetime.datetime.now().strftime("%H:%M:%S")
        dat = jdatetime.datetime.now().strftime("\n%a %d %b %Y")
        a = hour + dat
        await m.message.delete()
        try:
            await c.send_photo(m.message.chat.id,'./mersad.jpg',f'''
**⌯ شبکه GemTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backtv'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
        except:
            await c.send_video(m.message.chat.id, './mersad.mp4',f'''
**⌯ شبکه GemTv در حال پخش میباشد 🔊**
**⊹** نام درخواست کننده : {m.from_user.mention(m.from_user.first_name)}
**⊹** ساعت : `{a}` 📅
                ''',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت', callback_data = 'backma'),InlineKeyboardButton(text = '• توقف', callback_data = 'closee')]
        ]))
    elif data == 'backma' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.message.delete()
        await m.message.text('• جهت پخش، یکی از شبکه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• BBC', callback_data = 'bbc'), InlineKeyboardButton(text = '• ManotoTv', callback_data = 'manoto')],
        [InlineKeyboardButton(text = '• AvaFamily', callback_data = 'avafamily'), InlineKeyboardButton(text = '• AvaSeries', callback_data = 'avaseries')],
        [InlineKeyboardButton(text = '• FarsiTv', callback_data = 'farsitv'), InlineKeyboardButton(text = '• PMC', callback_data = 'pmc')],
        [InlineKeyboardButton(text = '• Vox 2', callback_data = 'vox2'), InlineKeyboardButton(text = '• Vox 1', callback_data = 'vox1')],
        [InlineKeyboardButton(text = '• NavahangMusic', callback_data = 'navahang'), InlineKeyboardButton(text = '• RadioJavan', callback_data = 'radiojavan')],
        [InlineKeyboardButton(text = '• IranInternational', callback_data = 'iraninternational'), InlineKeyboardButton(text = '• ITN', callback_data = 'itn')],
        [InlineKeyboardButton(text = '• GemTv', callback_data = 'gemtv'), InlineKeyboardButton(text = '• OxirTv', callback_data = 'owirtv')],
        [InlineKeyboardButton(text = '• GemRubix', callback_data = 'gemrubix'), InlineKeyboardButton(text = '• GemRiver', callback_data = 'gemriver')],
        [InlineKeyboardButton(text = '• GemBollywood', callback_data = 'gembollywood'), InlineKeyboardButton(text = '• GemSeries', callback_data = 'gemseries')],
        [InlineKeyboardButton(text = '• GemJunior', callback_data = 'gemjunior'), InlineKeyboardButton(text = '• GemDrama', callback_data = 'gemdrama')],
        [InlineKeyboardButton(text = '• GemFilm', callback_data = 'gemfilm'), InlineKeyboardButton(text = '• GemMaxx', callback_data = 'gemmaxx')],
        [InlineKeyboardButton(text = '• BBC Persian', callback_data = 'bbcpersian'), InlineKeyboardButton(text = '• MBC Persia', callback_data = 'mbcpersia')],
        [InlineKeyboardButton(text = '• Tapesh 1', callback_data = 'tapesh1'), InlineKeyboardButton(text = '• Tapesh 2', callback_data = 'tapesh2')],
        [InlineKeyboardButton(text = '• PersianaTv', callback_data = 'persiana'), InlineKeyboardButton(text = '• PMC Royale', callback_data = 'pmcr')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv'), InlineKeyboardButton(text = '• بازگشت', callback_data = 'backahura')]
        ]))
    elif data == 'backahura' and user_di in [*idsudos(), *idowner(), mersad, sudo, *creators(m.message.chat.id), *idvideo(m.message.chat.id), *allvideo()]:
        await m.edit_message_text('• لطفا یکی از گزینه های زیر را انتخاب کنید :',reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text = '• ماهواره', callback_data = 'mahvare'), InlineKeyboardButton(text = '• تلویزیون', callback_data = 'telev')],
        [InlineKeyboardButton(text = '• بستن پنل', callback_data = 'closetv')]
        ]))
    elif data == 'mutemus' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        await call_py.mute_stream(m.message.chat.id)
        await m.answer('• پخش بیصدا شد !')
    elif data == 'mutevid' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        await call_py.mute_stream(m.message.chat.id)
        await m.answer('• پخش بیصدا شد !')
    elif data == 'unmutemus' and user_di in [*idmusic(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allmusic(),*idsudos(),*idowner()]:
        await call_py.unmute_stream(m.message.chat.id)
        await m.answer('• پخش با صدا شد !')
    elif data == 'unmutevid' and user_di in [*idvideo(m.message.chat.id), *creators(m.message.chat.id), sudo,mersad, *allvideo(),*idsudos(),*idowner()]:
        await call_py.unmute_stream(m.message.chat.id)
        await m.answer('• پخش با صدا شد !')
    elif data == 'helpvideo':
        helpvid = '''
⊹ با این دستور میتوانید موزیک مورد نظر خود را دریافت نمایید.
 
**📌 به فارسی :**

 ✧ سرچ` { نام موزیک و خواننده }`

**📌 To English :**

 ✧ `search` { نام موزیک و خواننده }

⊹ مثال : سرچ حمید هیراد نیمه جانم

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید موزیک مورد نظر خود را به صورت خودکار پخش نمایید.

**📌 به فارسی :**

 ✧ پخش خودکار` { نام موزیک و خواننده }`

**📌 To English :**

 ✧ `AutoPlay` { نام موزیک و خواننده }

⊹ مثال : پخش خودکار حمید هیراد نیمه جانم

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید ویدئو مورد نظر خود را از یوتیوب جستجو و به صورت خودکار در ویس کال پخش نمایید.

**📌 به فارسی :**

 ✧ سرچ یوتیوب` { نام ویدئو مورد نظر }`

**📌 To English :**

 ✧ `PromotMusic` { نام ویدئو مورد نظر }

⊹ مثال : سرچ یوتیوب آموزش گیتار

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید با استفاده از لینک یوتیوب ، ویدئو مورد نظر خود را به صورت خودکار پخش نمایید.

**📌 به فارسی :**

 ✧ پخش یوتیوب` { لینک یوتیوب }`

**📌 To English :**

 ✧ `YoutubePlay` { لینک یوتیوب }

⊹ مثال : پخش یوتیوب https://www.youtube.com/watch?v=DLly1iiNY

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید با استفاده از لینک دانلود موزیک ، موزیک مورد نظر خود را به صورت خودکار پخش نمایید.

⊹ از تمامی سایت های معتبر ، پخش موزیک امکان پذیر میباشد.

**📌 به فارسی :**

 ✧ پخش لینک` { لینک }`

**📌 To English :**

 ✧ `PlayLink` { لینک }

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید با استفاده از لینک دانلود ویدیو ، ویدیو مورد نظر خود را به صورت خودکار پخش نمایید.

⊹ از تمامی سایت های معتبر ، پخش ویدیو امکان پذیر میباشد.

**📌 به فارسی :**

✧ پخش لینک ویدیو` { لینک }`

**📌 To English :**

  ✧ `PlayLinkVideo` { لینک }
'''
        await m.edit_message_text(helpvid,reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت',callback_data = 'backhelp')]
        ]))
    elif data == 'helpmusic':
        helpvid = '''
⊹ با این دستور میتوانید فرد مورد نظر را به لیست مدیران ویدیو اضافه نمایید.
⊹ فقط دسترسی به بخش ویدیو را دارا میباشد.

❪ ریپلای ، یوزرنیم ، آیدی عددی ❫

**📌 به فارسی :**

 ✧ `ترفیع ویدیو`
 ✧ `عزل ویدیو`

**📌 To English :**

 ✧ `PromotVideo`
 ✧ `demoteVideo`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈
⊹ با این دستور میتوانید کاربر مورد نظر خود را به لیست مدیران موزیک اضافه نمایید.
⊹ فقط دسترسی به بخش موزیک را دارا می‌باشد.

❪ ریپلای ، یوزرنیم ، آیدی عددی ❫

**📌 به فارسی :**

 ✧ `ترفیع موزیک`
 ✧ `عزل موزیک`

**📌 To English :**

 ✧ `PromotMusic`
 ✧ `DemoteMisuc`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈
⊹ با این دستور میتوانید تمامی مدیران گروه  را به لیست مدیران موزیک اضافه نمایید.

**📌 به فارسی :**

 ✧ `پیکربندی موزیک`
 ✧ `پاکسازی مدیران موزیک`
 ✧ `لیست مدیران موزیک`

**📌 To English :**

 ✧ `ConfigMusic`
 ✧ `DelConfigMusic`
 ✧ `ListMusic`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈
⊹ با این دستور میتوانید تمامی مدیران گروه را به لیست مدیران ویدیو اضافه نمایید.

**📌 به فارسی :**

 ✧ `پیکربندی ویدیو`
 ✧ `پاکسازی مدیران ویدیو`
 ✧ `لیست مدیران ویدیو`

**📌 To English :**

 ✧ `ConfigVideo`
 ✧ `DelConfigVideo`
 ✧ `ListVideo`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید فرد مورد نظر را به مالک ربات ترفیع دهید.

**📌 به فارسی :**

 ✧ `ترفیع مالک`
 ✧ `عزل مالک`
 ✧ `لیست مالکان`

**📌 To English :**

 ✧ `SetCreator`
 ✧ `DelCreator`
 ✧ `CreatorsList`
'''
        await m.edit_message_text(helpvid,reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت',callback_data = 'backhelp')]
        ]))
    elif data == 'inlinefun':
        helpvid = '''
⊹ با این دستور میتوانید موزیک مورد نظر خود را در ویس کال پخش نمایید.

⊹ این دستور به صورت ریپلای میباشد.

**📌 به فارسی :**

 ✧ `پخش`
 ✧ `توقف پخش`

**📌 To English :**

 ✧ `Play`
 ✧ `StopMusic`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈


⊹ با این دستور میتوانید ویدیو مورد نظر خود را پخش نمایید.

⊹ این دستور به صورت ریپلای میباشد.

**📌 به فارسی :**

 ✧ `پخش ویدیو`
 ✧ `توقف ویدیو`

**📌 To English :**

 ✧ `PlayVideo`
 ✧ `StopVideo`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید موزیک خود را به کاربر مورد نظر تقدیم کنید.

**📌 به فارسی :**

 ✧ پخش` { یوزرنیم ، آیدی عددی }`

**📌 To English :**

 ✧ `Play` { یوزرنیم ، آیدی عددی }

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید ویدیو خود را به کاربر مورد نظر تقدیم نمایید.

**📌 به فارسی :**

✧ پخش ویدیو` { یوزرنیم ، آیدی عددی }`

**📌 To English :**

 ✧ `PlayVideo` { یوزرنیم ، آیدی عددی }

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دو دستور میتوانید فرایند پخش خود را مکث و مجدد ازسرگیری نمایید.

**📌 به فارسی :**

 ✧ `مکث`
 ✧ `ازسرگیری`

**📌 To English :**

 ✧ `Pause`
 ✧ `Resume`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این قابلیت میتوانید فرایند پخش را بیصدا و مجدد باصدا نمایید.

**📌 به فارسی :**

 ✧ `بیصدا`
 ✧ `باصدا`

**📌 To English :**

 ✧ `silent`
 ✧ `unsilent`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید مقدار صدای موزیک را تنظیم کنید.

**📌 به فارسی :**

✧ صدای موزیک` { مقدار }`

**📌 To English :**

✧ `MusicSound` { مقدار }

⊹ مثال : صدای موزیک 160

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید مقدار صدای ویدیو را تنظیم کنید.

**📌 به فارسی :**

✧ صدای ویدیو` { مقدار }`

**📌 To English :**

✧ `VideoSound` { مقدار }

⊹ مثال : صدای ویدیو 160
'''
        await m.edit_message_text(helpvid,reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت',callback_data = 'backhelp')]
        ]))
    elif data == 'inlinemanage':
        helpvid = '''
⊹ با این قابلیت میتوانید موزیک های مورد نظر خود را به لیست پخش اضافه نمایید.

**📌 به فارسی :**

 ✧ `افزودن به لیست`

 ✧ `پخش لیست`

 ✧ `توقف لیست`

 ✧ `لیست پخش`

 ✧ `حذف از لیست`

 ✧ `پاکسازی لیست پخش`

**📌 ToEnglish :**

 ✧ `AddToPlayList`

 ✧ `PlayList`

 ✧ `StopList`

 ✧ `ListPlatList`

 ✧ `delfromPlaylist`

 ✧ `CleanPlayList`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید شبکه های داخلی ( تلویزیون ) و شبکه های بیرون مرزی ( ماهواره ) را تماشا کنید.

⊹ میتوانید شبکه های اصلی صدا سیما یا همان دیجیتال را مانند شبکه های یک ، دو ، سه ، خبر ، ورزش ، تماشا ، نسیم و... به صورت زنده در ویس کال تماشا کنید.

**📌 به فارسی :**

 ✧ `پخش تیوی`

 ✧ `توقف تیوی`

**📌 To English :**

 ✧ `PlayTv`

 ✧ `StopTv`
'''
        await m.edit_message_text(helpvid,reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت',callback_data = 'backhelp')]
        ]))
    elif data == 'karbordi':
        helpvid = '''
⊹ با این دستور میتوانید از آنلاینی ربات های خود اطلاع داشته باشید.

**📌 به فارسی :**

✧ `پینگ`

**📌 To English :**

 ✧ `Ping`

┈┅━─━─━─━─•◈•─━─━─━─━┅┈

⊹ با این دستور میتوانید از آنلاینی ربات ها مطلع شوید.

**📌 به فارسی :**

 ✧ `ربات`

**📌 To English :**

 ✧ `bot`

 ✧ `robot`
'''
        await m.edit_message_text(helpvid,reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• بازگشت',callback_data = 'backhelp')]
        ]))
    elif data == 'backhelp':
        await m.edit_message_text('• یکی از گزینه های زیر را انتخاب نمایید : \n┈┅┅━┃صفحه اصلی┃━┅┅┈',reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = '• سرچ و پخش خودکار', callback_data = 'helpvideo')],
            [InlineKeyboardButton(text = '• ارتقا و عزل', callback_data = 'helpmusic')],
            [InlineKeyboardButton(text = '• پخش ها', callback_data = 'inlinefun'),InlineKeyboardButton(text = '• کاربردی', callback_data = 'karbordi')],
            [InlineKeyboardButton(text = '• تیوی و لیست پخش', callback_data = 'inlinemanage')],
            [InlineKeyboardButton(text = '• بستن', callback_data = 'closehelp')],
        ]))
    elif data == 'closehelp':
        await m.edit_message_text('• پنل راهنما با موفقیت بسته شد !')



@call_py.on_stream_end()
async def stop(client: PyTgCalls, update: Update):
    if update.chat_id in playing:
        if os.path.exists(playing[update.chat_id]):
            os.remove(playing[update.chat_id])
        del playing[update.chat_id]
    if update.chat_id in playlis:
        if os.path.exists(playlis[update.chat_id]):
            os.remove(playlis[update.chat_id])
        del playlis[update.chat_id]
    await client.leave_group_call(update.chat_id)
    
@api.on_message(filters.user(mersad) & (filters.regex(r'^(کارت)') | filters.regex(r'^([Cc][Aa][Rr][Dd])')))
async def a(c:Client, m:Message):
    await m.reply("👉 `6037998240935196` 👈\n**💳 #بانک_ملی\n\nبه نام : محمدامین داوری 🔖\n\n❌ اسکرین از فیش الزامی میباشد‌ 📸**")
    
@api.on_message(filters.user(mersad) & (filters.regex(r'^(من کیم)') | filters.regex(r'^([Mm][Aa][Nn])')))
async def a(c:Client, m:Message):
    await m.reply("شما مرصاد **برنامه نویس** ربات هستی")
    
# @cli.on_message(filters.private)
# async def stcli(c:Client, m:Message):
#     cur.execute('SELECT * FROM startcli')
#     for i in cur.fetchall():
#         information_tuple = i
#     start = information_tuple[0]
#     if 'MENTION' in start:
#         start = start.replace('MENTION',m.from_user.mention(m.from_user.first_name))
#     if 'BOLD' in start:
#         start = start.replace('BOLD','**')
#     if 'USERID' in start:
#         start = start.replace('USERID',m.from_user.id)
#     await m.reply(start)


# @api.on_message(filters.new_chat_members)
# async def aaasss(c:Client, m:Message):
#     if m.chat.id == (await c.get_me()).id:
#         return
#     await asyncio.sleep(300)
#     cur.execute('SELECT * FROM autoleft')
#     x = cur.fetchall()
#     if x == []:
#         return
#     else:
#         if x[0][0] == 1:
#             cur.execute(f'SELECT * FROM gp WHERE idgp={m.chat.id}')
#             if cur.fetchall() == []:
#                 try:
#                     await api.leave_chat(m.chat.id)
#                 except: pass
#                 try:
#                     await cli.leave_chat(m.chat.id)
#                 except: pass


cron1 = aiocron.crontab('*/13 * * * *', func=check,args=(Client,Message))
cron2 = aiocron.crontab('*/18 * * * *', func=check2,args=(Client,Message))
cron3 = aiocron.crontab('*/10 * * * *', func=etebar, args=(Client,Message))
cron4 = aiocron.crontab('*/20 * * * *', func=checkinfo, args=(Client,Message))
cron5 = aiocron.crontab('*/25 * * * *', func=checkinfo2, args=(Client,Message))

idle()
api.stop()
