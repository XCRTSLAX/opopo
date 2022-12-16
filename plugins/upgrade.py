"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply, CallbackQuery)
from pyrogram import Client , filters
from helper.txt import kr


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "upgrade":
        await query.message.edit_text(
	    text=kr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup([[ 
                InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mr_Tamil_KiD") 
                ],[
                InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Mr_Tamil_KiD"),
                InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/1icxtwpo")
                ],[
                InlineKeyboardButton("Cancel",callback_data = "cancel")]])
	
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	await message.reply_text(
            text=kr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup([[ 
                InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mr_Tamil_KiD")], 
        	[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Mr_Tamil_KiD"),
        	InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/1icxtwpo")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	
