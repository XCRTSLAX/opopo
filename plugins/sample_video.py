
import logging
logger = logging.getLogger(__name__)

import math
import time
import asyncio
from ..config import Config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup











############################# Time Formating ⏰ #############################

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
        ((str(hours) + " hrs, ") if hours else "") + \
        ((str(minutes) + " min, ") if minutes else "") + \
        ((str(seconds) + " sec, ") if seconds else "") + \
        ((str(milliseconds) + " millisec, ") if milliseconds else "")
    tmp = tmp[:-2] if tmp[:-2] != "" else 0
    return tmp


############################# END 🌋 #############################
