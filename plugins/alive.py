import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4298e8422293161c45b53.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴀᴅɪᴛʏᴀ ʜᴀʟᴅᴇʀ](https://t.me/adityahalder)
┣★ ᴜᴘᴅᴀᴛᴇs : [ᴀᴅɪᴛʏᴀ sᴇʀᴠᴇʀ](https://t.me/adityaserver)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴀᴅɪᴛʏᴀ ᴅɪsᴄᴜs](https://t.me/adityadiscus)
┣★ sᴏᴜʀᴄᴇ › : [ɢᴇᴛ ʀᴇᴘᴏ ʜᴇʀᴇ](https://github.com/mradityaxd/adityaplayer)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/adityahalder) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/cfc_bots")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥  𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗴𝗿𝗽❣️", url=f"https://t.me/cfc_bot_support")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://github.com/Kiraxophunter/kiraxmuisc")
                ]
            ]
        ),
    )
