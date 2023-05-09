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

import asyncio
import importlib
import os

from pyrogram import idle

from GJ516Music import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from GJ516Music.Modules import ALL_MODULES


async def GJ516_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("GJ516Music.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"❇ 𝗚𝗝𝟱𝟭𝟲 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 ❇\n\n⎋ 𝙄𝙙 : `{BOT_ID}`\n⎋ 𝙉𝙖𝙢𝙚 : {BOT_NAME}\n⎋ 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"❇ 𝗚𝗝𝟱𝟭𝟲 𝗠𝗨𝗦𝗜𝗖 𝗔𝗦𝗦 ❇\n\n⎋ 𝙄𝙙 : `{ASS_ID}`\n⎋ 𝙉𝙖𝙢𝙚 : {ASS_NAME}\n⎋ 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Jay Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] Jay Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] jay music loaded "
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(GJ516_startup())
    LOGGER.error("GJ516 Music Bot Stopped.")
