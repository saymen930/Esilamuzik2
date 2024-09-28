import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "20824282"))
API_HASH = getenv("API_HASH", "5c49d99b5bb9e41c9b8ada4f826989ef")
BOT_TOKEN = getenv("BOT_TOKEN", "7164261117:AAFs8YEB0MIHpgXaNAeiAa8AgEgYrzEldnE")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002065943011"))
OWNER_ID = int(getenv("OWNER_ID", "6604501109"))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalmuzikk")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "BAE9wNoABsvrn-JLcw318pdnglE4LTjyzNwl7Qo0XekijQ0PeNMWNl0YUFaXpG7D5dz-g5EsQ0n_07sBurZiluwoLY4xbxr3ERb_uFe_X_wOAh9kj3U3utLKCr00ojp9AePMCYZGPwf3LE7OkAikgKn8ML3a_aR4Pa_sfmC0RVJMlPhv0N771eZ3cg59VOjN98W_xnYSKZbeWCyIEMwy0WILzLGEzDRJXCPZagYRHKRVRfqP2sbMkctjHlv_fIhsKpYb14geNlAn2MVfQ5AcfaGpx8VuhdpRMVoZe-BVU9KkftLW5L3N7XEOA54fhJW1Bg2oVtDz0lO5NS6dfedolG3UothaLAAAAAGJqLB1AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/SGJ.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/SGJ.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/SGJ.jpg"
STATS_IMG_URL = "https://envs.sh/SGJ.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/SGJ.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/SGJ.jpg"
STREAM_IMG_URL = "https://envs.sh/SGJ.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/SGJ.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/SGJ.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/SGJ.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/SGJ.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/esila-09-28"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
