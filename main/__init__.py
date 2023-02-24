#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config(14463612, default=None, cast=int)
API_HASH = config("814bb504e6bfed51001693a8e1ae59da", default=None)
BOT_TOKEN = config("6093536506:AAHzt_T7dsFWNg5Frr8Ikurj7RDJJ-Gk79Q", default=None)
SESSION = config("BQBfWYDhUtZItSoTPyWQsTaHOLWWFA8M0A3q9Wxpv4LzE5dHf51JQrveNV0LXhBC8xC4Z63U309t8tdimZ4zvLXWVpe9__8j3pawnPTp_MeAw9Ch9mEKIL-FHpJ06MakXZaO0_ufswccs2RXuS-TbCxMV0Ub21hoMw7QTprXxkquQF3YbsKty5rRgQhzd0mQflCv7KiHwiP5334Uz8sD2w0Z1kMV44EMHCICU89opsX8K9Z4cR6qM0GplrxuHjAiuQOGHLJ_KctXdu4MYRUEyeXvymFUIMXnt6_qQS9lkLoOkPbpJ2Tsc6tVqJziC7IBURGBdL6hQENjdi0A1RPM0GK9NpAVpQA", default=None)
FORCESUB = config("MDS1242", default=None)
AUTH = config("915412389", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
