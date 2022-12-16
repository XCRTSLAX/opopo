"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply, CallbackQuery)
from pyrogram import Client , filters
from helper.txt import kr


@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgrade(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	**VIP3**
	Daily Upload limit 100GB
	Price Rs 150  🇮🇳/🌎 1.81$  per Month
	
	
	Pay Using Upi I'd ```tamildub@ybl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mr_Tamil_KiD")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Mr_Tamil_KiD"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/1icxtwpo")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
