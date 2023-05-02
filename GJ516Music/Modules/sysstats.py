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

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from GJ516Music import BOT_NAME, SUDOERS, app
from GJ516Music.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"𝙂𝙚𝙩𝙩𝙞𝙣𝙜 {BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨, 𝙄𝙩'𝙡𝙡 𝙏𝙖𝙠𝙚 𝘼 𝙒𝙝𝙞𝙡𝙚..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " 𝙂𝘽"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}𝙂𝙃𝙕"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}𝙈𝙃𝙕"
    except:
        cpu_freq = "𝗙𝗮𝗶𝗹𝗲𝗱 𝗧𝗼 𝗙𝗲𝘁𝗰𝗵"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➜ <u>**{BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨**</u>

**𝙋𝙮𝙩𝙝𝙤𝙣 :** {pyver.split()[0]}
**𝙋𝙧𝙤𝙜𝙧𝙖𝙢 :** {pyrover}
**𝙋𝙮-𝙏𝙜𝙘𝙖𝙡𝙡𝙨 :** {pytgver}
**𝙎𝙪𝙙𝙤𝙚𝙧𝙨 :** `{sudoers}`
**𝙈𝙤𝙙𝙪𝙡𝙚𝙨 :** `{mod}`

**𝙄𝙋 :** {ip_address}
**𝙈𝙖𝙘 :** {mac_address}
**𝙃𝙤𝙨𝙩𝙣𝙖𝙢𝙚 :** {hostname}
**𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 :** {sp}
**𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙤𝙧 :** {processor}
**𝘼𝙧𝙘𝙝𝙞𝙩𝙚𝙘𝙩𝙪𝙧𝙚 :** {architecture}
**𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 𝙍𝙚𝙡𝙚𝙖𝙨𝙚 :** {platform_release}
**𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** {platform_version}

        <b><u>𝗦𝘁𝗼𝗿𝗮𝗴𝗲</b><u/>
**𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 :** {total[:4]} 𝙂𝙞𝙗
**𝙐𝙨𝙚𝙙 :** {used[:4]} 𝙂𝙞𝙗
**𝙁𝙧𝙚𝙚 :** {free[:4]} 𝙂𝙞𝙗

**𝙍𝙖𝙢 :** {ram}
**𝙋𝙝𝙮𝙨𝙞𝙘𝙖𝙡 𝘾𝙤𝙧𝙚𝙨 :** {p_core}
**𝙏𝙤𝙩𝙖𝙡 𝘾𝙤𝙧𝙚𝙨 :** {t_core}
**𝘾𝙥𝙪 𝙁𝙧𝙚𝙦𝙪𝙚𝙣𝙘𝙮  :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❰𝘾𝙡𝙤𝙨𝙚❱",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
