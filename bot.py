import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5377834462:AAFr_4q9Sw3RtGPoMtgkxy-w4A6TE8oN_0w")

API_ID = int(os.environ.get("API_ID", "13384432"))

API_HASH = os.environ.get("API_HASH", "ea9db4503ed7088b788e06dfd818e00e")

STRING = os.environ.get("STRING", "BQDdVvcABsNvLN1U5d5lYsZN5RrHEpOPKjZOcGxqgGB4CqA50wD4Oh30moXekjc13A6zAxz7rGyBOssmJV-wAgLoqFf_JQuSTtlxHIN57NyjoNfP6hr8BFmA4avFe9yN3ixywyBYk69YqXji7Myu_F3bdyy3xzJpp1Hyx5SAI5yBgDecAFZeF1ytYaBpCGZsR_wPXjwQwsIGvLYSWL92LUxiSgsVWInGcjvxloM6EdVl5Z19bvT4uLoTTrP2PSXfDHYdSWyDpeejdisI2ugxqKJVT78wrrXgJY1eFtI7DHlyclf4koJhn36ntY_y6D2ZHbjnHNsNvYystmFVqy6834Jb3DWBpwAAAAE7Z4AQAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
