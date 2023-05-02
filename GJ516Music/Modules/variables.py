# MIT License
#
# Copyright (c) 2023 AnonymousX1025
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

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from GJ516Music import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀 :**</u>

**𝘼𝙥𝙞_𝙄𝙙 :** `{config.API_ID}`
**𝘼𝙥𝙞_𝙃𝙖𝙨𝙝 :** `{config.API_HASH}`

**𝘽𝙤𝙩_𝙏𝙤𝙠𝙚𝙣 :** `{config.BOT_TOKEN}`
**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣_𝙇𝙞𝙢𝙞𝙩𝙨 :** `{config.DURATION_LIMIT}`

**𝙊𝙬𝙣𝙚𝙧_𝙄𝙙 :** `{config.OWNER_ID}`
**𝙎𝙪𝙙𝙤_𝙐𝙨𝙚𝙧𝙨 :** `{config.SUDO_USERS}`

**𝙋𝙞𝙣𝙜_𝙄𝙢𝙜 :** `{config.PING_IMG}`
**𝙎𝙩𝙖𝙧𝙩_𝙞𝙢𝙜 :** `{config.START_IMG}`
**𝙎𝙪𝙥𝙥𝙤𝙧𝙩_𝘾𝙝𝙖𝙩 :** `{config.SUPPORT_CHAT}`

**𝙎𝙚𝙨𝙨𝙞𝙤𝙣 :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝙎𝙚𝙣𝙙 𝙩𝙝𝙚 𝘾𝙤𝙣𝙛𝙞𝙜 𝙑𝙖𝙧𝙞𝙖𝙗𝙡𝙚𝙨.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "𝙋𝙡𝙚𝙖𝙨𝙚 𝘾𝙝𝙚𝙘𝙠 𝙔𝙤𝙪𝙧 𝙋𝙢, 𝙄'𝙫𝙚 𝙎𝙚𝙣𝙩 𝙏𝙝𝙚 𝙘𝙤𝙣𝙛𝙞𝙜 𝙑𝙖𝙧𝙞𝙖𝙗𝙡𝙚𝙨."
        )
