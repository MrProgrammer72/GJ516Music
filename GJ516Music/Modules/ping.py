# MIT License
#
# Copyright (c) 2023 MrProgrammer72 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from datetime import datetime
import random

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from GJ516Music import BOT_NAME, StartTime, app
from GJ516Music.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=random.choice(PING_IMG), caption=f"{BOT_NAME} 𝙄𝙨 𝙋𝙞𝙣𝙜𝙞𝙣𝙜...."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""𝙋𝙤𝙣𝙜 : `{resp}𝙈𝙨`

<b><u>{BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨 :</u></b>

✾ **𝙐𝙥𝙩𝙞𝙢𝙚 :** {uptime}
✾ **𝙍𝙖𝙢 :** {mem}
✾ **𝘾𝙥𝙪 :** {cpu}
✾ **𝘿𝙞𝙨𝙠 :** {disk}

||𝙈𝙖𝙙𝙚 𝘽𝙮 : [ــ٨ﮩﮩ𝗝♡𝗬💸](https://t.me/export_gabbar) || """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT)
                ],
            ]
        ),
    )
