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
Hi ð {}!
        
__A sÉªá´á´Êá´ á´á´sÉªá´ á´á´Êá´á´á´á´Ê Êá´á´. Éªá´ á´á´É´ á´á´Êá´á´á´ ÊÉªÉ´á´ á´á´ á´á´Éªsá´.

sá´É´á´ á´á´ á´É´Ê á´ÊÉªá´á´ ÊÉªÉ´á´ á´Ê Êá´á´á´á´Êá´ á´Ê á´ Éªá´á´á´ ÊÉªÉ´Ê I á´¡ÉªÊÊ á´á´Êá´á´á´ á´á´ á´á´Éªsá´ á´É´á´ É¢Éªá´ á´ á´ÊÉªá´á´á´ á´á´Éªsá´ ÊÉªÉ´á´

> ÑÏÏÏÏÑÑ Â¢ÏÑÑÏÐ¼ ÑÐ½ÏÐ¼Ð²Î·Î±Î¹â

> ÑÏÏÏÏÑÑ Â¢ÏÑÑÏÐ¼ ÑÎ¹ÑÑâÑ Î·Î±Ð¼Ñ

ð¥ððð /help ðð®ð¿ð²ð³ðð¹ð¹ð & ðð¢ððð¢ðª ððð ð§ðð ð¥ð¨ððð¦... __

âª Â» **ð£ð¢ðªðð¥ ðð¬ : @KOT_BOTS ðð¡ð¬  ð£ð¥ð¢ðððð  ð¢ð¥ ð¥ðð£ð¢ð¥ð§ : @KOT_REPORS** â¤µï¸
"""

HELP = """
*ðð¢ðª ð§ð¢ ð¨ð¦ð ð ð...**

â¦¿ Its Easy to Use me 
âª Â» Send me Any Direct Link or YouTube Link
âª Â» i will upload to PDisk & Give Link

â  If you want Upload Telegram file,Videos to PDisk
âª Â» First Send any File to @Link4Filesbot to generate Direct Link
âª Â» Copy Generated Link and Paste here...
âª Â» Violaaaa.... Done

â  If You Want add Custom Tittle & Thumbnail Follow These Steps

âª Â» link | Title

Or

âª Â» Video link | Title | Thumbnail link
        (generate Thumbnail Link with Telegraph bot[@TGraphXbot])

NOTE:
â¢ Do Not Spam, Send Link One By One, 
â¢ The Video File is Available on Your LINK ones Upload Process is Complete, it Take Time Depend on Your File Size & My Server Upload Speed
So,be Patient ð´ð´ð´ð´"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¿KOT BOTS ð¿', url='https://t.me/KOT_BOTS')
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
