import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# API Credentials
API_ID = getenv("API_ID", "")
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Owner & Bot Info
OWNER_ID = int(getenv("OWNER_ID", "7918103039"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
BOT_NAME = getenv("BOT_NAME", "AdamMusic_Bot")
ASSUSERNAME = getenv("ASSUSERNAME", "")

# Database
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# Logging
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "17000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Music APIs
YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com')
YT_API_KEY = getenv("YT_API_KEY", "")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Git & Updates
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/MrZyro/ZyroMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LoverCodes")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LoverCodesChat")

# Assistant Settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# String Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/zeexhx.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/l6ekqj.jpg")
NOW_PLAYING_IMG_URL = getenv("NOW_PLAYING_IMG_URL", "https://images8.alphacoders.com/135/thumb-1920-1351572.jpeg")

# Filters & Variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ===== FIXES FOR RENDER =====
EVAL = True  # ← MISSING था यह!
OWNER_ID = int(getenv("OWNER_ID", "8546535996"))  # Duplicate fix

# Duration function
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL Validation
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL wrong!")
if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT URL wrong!")
