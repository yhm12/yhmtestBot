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
BOT_TOKEN = config("5635031675:AAErZp0Hkk2eu_Z8AEfJZOleBuJilTVrVVg", default=None)
SESSION = config("BQDDhYxK91XCEBwseT0vbkqwTF1AeOoNxB_VR80roF4HLEN7K-kDrBMSxOEVSkOAZfpRwXXEVMiNooZMdLvlX61atfMFahh5IFG8o3Z8KZzaLbYuxLnu7d2Qk4SVhuWonjQhghRuRc9zF-wgNIj7Jf6_dkVBdoEV_GwXQHdETECIvIt3gsik0odr4jnF9yVNXy1LuZ2yLE9CWlzghGvAILcQ-Le8Ppex0An2kB7kIn7HDAi5RKxfI8uRjOaqN3tRHeNL0RSpN7ZUk_PUZQF9DETHpdzmD8wfKcnAZ6GfJ0ey2gEECsiMNafrcmLqAobY-RHxieZHJxHekNU9rzDXO28fNpAVpQA", default=None)
FORCESUB = config("Spotify/Netflix/HBO", default=None)
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
