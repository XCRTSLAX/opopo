"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply, CallbackQuery)
from pyrogram import Client , filters
from helper.txt import kr


@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
        await query.message.edit_text(
	    text=kr.PAID_TXT,
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
            text=kr.PAID_TXT,
            reply_markup=InlineKeyboardMarkup([[ 
                InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mr_Tamil_KiD")], 
        	[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Mr_Tamil_KiD"),
        	InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/1icxtwpo")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	
