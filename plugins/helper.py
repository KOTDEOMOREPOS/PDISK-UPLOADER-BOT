# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Hi 👋 {}!
        
__A sɪᴍᴘʟᴇ ᴘᴅsɪᴋ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ. ɪᴛ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ʟɪɴᴋ ᴛᴏ ᴘᴅɪsᴋ.

sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅʀɪᴄᴛ ʟɪɴᴋ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴏʀ ᴠɪᴅᴇᴏ ʟɪɴʟ I ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴘᴅɪsᴅ ᴀɴᴅ ɢɪᴠᴇ ᴅʀɪᴄᴇᴛ ᴘᴅɪsᴋ ʟɪɴᴋ

> ѕυρρσят ¢υѕтσм тнυмвηαιℓ

> ѕυρρσят ¢υѕтσм тιттℓє ηαмє

𝗥𝗘𝗔𝗗 /help 𝗖𝗮𝗿𝗲𝗳𝘂𝗹𝗹𝘆 & 𝗙𝗢𝗟𝗟𝗢𝗪 𝗔𝗟𝗟 𝗧𝗛𝗘 𝗥𝗨𝗟𝗘𝗦... __

✪ » **𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 : @KOT_BOTS 𝗔𝗡𝗬  𝗣𝗥𝗢𝗕𝗟𝗘𝗠 𝗢𝗥 𝗥𝗘𝗣𝗢𝗥𝗧 : @KOT_REPORS** ⤵️
"""

HELP = """
*𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘...**

⦿ Its Easy to Use me 
✪ » Send me Any Direct Link or YouTube Link
✪ » i will upload to PDisk & Give Link

➠ If you want Upload Telegram file,Videos to PDisk
✪ » First Send any File to @Link4Filesbot to generate Direct Link
✪ » Copy Generated Link and Paste here...
✪ » Violaaaa.... Done

➠ If You Want add Custom Tittle & Thumbnail Follow These Steps

✪ » link | Title

Or

✪ » Video link | Title | Thumbnail link
        (generate Thumbnail Link with Telegraph bot[@TGraphXbot])

NOTE:
➢ Do Not Spam, Send Link One By One, 
➢ The Video File is Available on Your LINK ones Upload Process is Complete, it Take Time Depend on Your File Size & My Server Upload Speed
So,be Patient 😴😴😴😴"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🍿KOT BOTS 🍿', url='https://t.me/KOT_BOTS')
        ],[
        InlineKeyboardButton('SUPPORT', url='https://telegram.me/KOT_REPORS'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
