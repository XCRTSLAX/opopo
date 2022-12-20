import os

class Config:
    ACTIVE_DOWNLOADS = {}
    API_ID = int(os.environ.get("API_ID", '6795023'))
    API_HASH = os.environ.get("API_HASH", '48eb04ae416967495ba9930f87d4f4da')
    PAID_BOT = os.environ.get("PAID_BOT", "YES")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQDMOvAACtNs-VchfumyK9k5-nCNC07ktlBNprSCibT8v6TlKUld6ZCdmSweiwaB9dYKGUGUDJoVmwk76Di47l9KaeEfBO_6ly7autQqKVoaV0t51FOqxtQQ5sm1zKT4qfvV0zUnw-2nY4yUEzCJJ-2OADSkzQXUDWq_0R1WEDvDOrwUVu6Q92Yliu3yOvUe-yYF9Cd9aiUZO8oOl2Lr5ljVBOQXD1s-acZV_80Ltf20fTkuYym6Bv1zrdvyXuyiBBaQKv_cwHaXcjmAlxvmQaBE-N75q8C_TazXigo0Uflhpqj7MzZoLJZQWw15Tci7RITeErIKtRFC7u6JhnbLDIEZ_uuWYgAAAABZsWSfAA")
    AUTH_USERS =  [int(i) for i in os.environ.get("AUTH_USERS", "5400525106 1504797855").split(" ")]
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5028427286:AAGggDShZZwX7lnfkeaH9i0FalwBBkh2cGU")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    DB_CHANNEL_ID = -1001769216579
    RESTART_TIME = []
    TIME_GAP1 = {}
    TIME_GAP2 = {}
    timegap_message = {}
