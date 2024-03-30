from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ ๛ʏ ᴜ ᴋ ɪ ᴋ ᴏ ༗ ᴍ ᴜ s ɪ ᴄ

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ʏ ᴜ ᴋ ɪ ᴋ ᴏ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Honey_World_Support"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/MRGLAXIER4260"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/463f32cce014e30f13165.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
