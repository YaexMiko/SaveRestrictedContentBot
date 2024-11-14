#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "27692015")
API_HASH = config("API_HASH", "25278a8394b5914ee1b8d6a6c79d572d")
BOT_TOKEN = config("BOT_TOKEN", "7716433955:AAFyRm41MWU-K0MslxcRWvE5tOYFMCS3pO8")
SESSION = config("SESSION", "BQGmi-8Arhpi93k8Wiu0OXxhtgevxtH6iVAm7f3fZPiCKXZphoes5UeXwl4dvU-l_ph5Fk3WtcvgVHPA_Xmdv2JYnKxkEEyL40Sjlxnd2wuB13pJNSmC_I4t0WzLAOnqt804pKw8Tudfp03aPD-KFRURp8HZ71KDChX0Ou3RHca7wkazr8HKhRRIudb4hl80OWTUnfToDKOU_2egdIQQYBsnea1yC2JgEsJL6yY7EVgFcAVn0a_sAUwCYpOmyCnk9teaCPLYxGMM21HF5GuRU751Dpsr9MHzgNB8Xu00YSbgIv7qOQSMBVOhG96Du_8VtgVAZNjEzId1vlD0-8y5jX6k6vnAAAAAGmvyK6AA")
FORCESUB = config("FORCESUB", "-1002019186374")
AUTH = config("AUTH", "8108281129")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
