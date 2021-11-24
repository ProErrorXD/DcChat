import os

from heroku3 import from_key
from pyrogram import Client


API_ID = int(os.environ.get("API_ID", "1714588"))
API_HASH = os.environ.get("API_HASH", "78c27bf90c81f15a8af4aa0aeeadfc42")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "2126972604:AAEyb_v4qJptARMzyyIxNhWR1UaALl_FR6w")
ARQ_API_KEY = "XQYJAL-HTSZIK-YALWDS-TJPWMO-ARQ" 
LANGUAGE = "hi"
ARQ_API_BASE_URL = "https://thearq.tech"

  
bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
