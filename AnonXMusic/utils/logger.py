from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} LOG BAŞLATTI.</b>

<b>SOHBET İD :</b> <code>{message.chat.id}</code>
<b>SOHBET ADI :</b> {message.chat.title}
<b>SOHBET NİCK :</b> @{message.chat.username}

<b>KULLANICI İD :</b> <code>{message.from_user.id}</code>
<b>KULLANICI :</b> {message.from_user.mention}
<b>KULLANICI ADI :</b> @{message.from_user.username}

<b>SORGU :</b> {message.text.split(None, 1)[1]}
<b>YAYIN TÜRÜ :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
