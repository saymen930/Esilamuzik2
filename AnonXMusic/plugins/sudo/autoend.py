from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Örnek :</b>\n\n/autoend [Enable | Disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» Akışı Otomatik Sonlandırma Etkinleştirildi..\n\nAsistan, Kimse Dinlemediğinde Birkaç Dakika Sonra Otomatik Olarak Görüntülü Sohbetten Ayrılacak."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» Akışı Otomatik Sonlandırma Devre Dışı Bırakıldı.")
    else:
        await message.reply_text(usage)
