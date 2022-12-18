import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5377834462:AAFr_4q9Sw3RtGPoMtgkxy-w4A6TE8oN_0w")

API_ID = int(os.environ.get("API_ID", "13384432"))

API_HASH = os.environ.get("API_HASH", "ea9db4503ed7088b788e06dfd818e00e")

STRING = os.environ.get("STRING", "AQAhvqqzDxOxM-GHPtjy2z1iZDJmqoi0H_R5V46S9D2nUT3kkfbQP1p89u9fnPK6T8jPvpJ7IMtfI4GM7D2OJjVI2WUjN3epcdrYuTf5wtsyhKUrioL9xigNzqzZV6T32jcAlgVbaBv_ioepOU-AlB9Omo-ulGR4yrXHBYHlx1OMNneYzH-8BLZO45-4oAApOAYBxvunvwSOn-bIyWchSv-XigLCOTFrsvd5frYpYQD00KUsk7T80boHOzPNI1a4jmK2vLyyZ-tb75xXeZDaYguQQV23QldgCxXsXz657XUkhslljkAJk7ar4cJsPNXs310ALXRD7Av0CE3xdV9K9bpKAAAAAUHleTIA")


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
