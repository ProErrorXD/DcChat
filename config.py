import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "1714588"))
API_HASH = os.environ.get("API_HASH", "78c27bf90c81f15a8af4aa0aeeadfc42")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "2126972604:AAEyb_v4qJptARMzyyIxNhWR1UaALl_FR6w")
ARQ_API_KEY = "XQYJAL-HTSZIK-YALWDS-TJPWMO-ARQ" 
LANGUAGE = "hi"
ARQ_API_BASE_URL = "https://thearq.tech"


class Config(object):
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "PATRICIA_ROBOT")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Evil:NRb0LXgSBdao6tHB@cluster0.phtr6.mongodb.net/EvilretryWrites=true&w=majority")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", "dontsellme_iamfreeapi")
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
    SUDO_USERS.append(1204927413)
    SUDO_USERS = list(set(SUDO_USERS))

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
