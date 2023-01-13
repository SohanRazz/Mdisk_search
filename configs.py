import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "15756731"))
    API_HASH = os.environ.get("API_HASH", "28d775d8c5aecbfc149bb7ae99bbf8aa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5837036557:AAGJ-samJLemOjaikiCoOSg15yMWau2v1U8")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQB6IjTSRGYAhrOLTN_TdV_pn7dHNCOcPfnw_1Z5bWtKyE4kyeAsGzx64wpSef7x7rosXBwoeB6U83StTRQgqcYNWlWILm_gm5LfABJwX6vxqB9ZcCt4By11AC3uzHCMUbPa5upXBDx8avPF_ZxeGsYvd_F9INyOSSqAk8l_Wq6Y5SzFY4CUBvSP5dN57xWVKI98H25ACM7JRozz-S_S7CdVBSD1bA7fWx2B8gCtOk_rHI-Yj01SwfvkopTkem-EugZbXgOZrEJ1tqDhFFdrO0RlfMT_h3dpMltbXifn-sdePnN-T76m0td2Az6CYm1VqF3tLAeVsf0wvPkzFTDdjIiUAAAAAUvlWeUA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001836945914"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "mdisk_NETFLIX_SEARCH_BOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5897793065"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Sohanrazz:Sohanrazz@cluster0.3ru2c4f.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001836945914")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

