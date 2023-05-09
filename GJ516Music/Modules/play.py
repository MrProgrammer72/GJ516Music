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
import os

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, UnMuteNeeded
from pytgcalls.types import AudioPiped, HighQualityAudio
from youtube_search import YoutubeSearch

from config import DURATION_LIMIT
from GJ516Music import (
    ASS_ID,
    ASS_MENTION,
    ASS_NAME,
    ASS_USERNAME,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    app,
    app2,
    GJ516db,
    pytgcalls,
)
from GJ516Music.Helpers.active import add_active_chat, is_active_chat, stream_on
from GJ516Music.Helpers.downloaders import audio_dl
from GJ516Music.Helpers.errors import DurationLimitError
from GJ516Music.Helpers.gets import get_file_name, get_url
from GJ516Music.Helpers.inline import buttons
from GJ516Music.Helpers.queue import put
from GJ516Music.Helpers.thumbnails import gen_qthumb, gen_thumb


@app.on_message(
    filters.command(["play", "vplay", "p"])
    & filters.group
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    GJ516 = await message.reply_text("𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 ........")
    try:
        await message.delete()
    except:
        pass

    try:
        try:
            get = await app.get_chat_member(message.chat.id, ASS_ID)
        except ChatAdminRequired:
            return await GJ516.edit_text(
                f"   𝙄 𝙙𝙤𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 𝙐𝙨𝙚𝙧𝙨 𝙑𝙞𝙖 𝙇𝙞𝙣𝙠 𝙁𝙤𝙧 𝙄𝙣𝙫𝙞𝙩𝙞𝙣𝙜  {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙏𝙤 {message.chat.title}."
            )
        if get.status == ChatMemberStatus.BANNED:
            unban_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"𝙐𝙣𝙗𝙖𝙣 {ASS_NAME}",
                            callback_data=f"unban_assistant {message.chat.id}|{ASS_ID}",
                        ),
                    ]
                ]
            )
            return await GJ516.edit_text(
                text=f" {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙄𝙨 𝘽𝙖𝙣 𝙄𝙣  {message.chat.title}\n\n☍ 𝙄𝙙 : `{ASS_ID}`\n☍ 𝙉𝙖𝙢𝙚 : {ASS_MENTION}\n☍ 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : @{ASS_USERNAME}\n\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙐𝙣𝙗𝙖𝙣 𝙏𝙝𝙚 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘼𝙣𝙙 𝙋𝙡𝙖𝙮𝙞𝙣𝙜 𝘼𝙜𝙖𝙞𝙣.....",
                reply_markup=unban_butt,
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await app2.resolve_peer(invitelink)
            except Exception as ex:
                LOGGER.error(ex)
        else:
            try:
                invitelink = await app.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await GJ516.edit_text(
                    f"𝙄 𝙙𝙤𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 𝙐𝙨𝙚𝙧𝙨 𝙑𝙞𝙖 𝙇𝙞𝙣𝙠 𝙁𝙤𝙧 𝙄𝙣𝙫𝙞𝙩𝙞𝙣𝙜 {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙏𝙤 {message.chat.title}."
                )
            except Exception as ex:
                return await GJ516.edit_text(
                    f"𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙏𝙤 {message.chat.title}.\n\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{ex}`"
                )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        anon = await GJ516.edit_text(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩....\n\n𝙄𝙣𝙫𝙞𝙩𝙞𝙣𝙜 {ASS_NAME} ᴛᴏ {message.chat.title}."
        )
        try:
            await app2.join_chat(invitelink)
            await asyncio.sleep(2)
            await GJ516.edit_text(
                f"{ASS_NAME} 𝙅𝙤𝙞𝙣𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 ,\n\n𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙎𝙩𝙧𝙚𝙖𝙢..."
            )
        except UserAlreadyParticipant:
            pass
        except Exception as ex:
            return await GJ516.edit_text(
                f"𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝙄𝙣𝙫𝙞𝙩𝙚 {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙏𝙤 {message.chat.title}.\n\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{ex}`"
            )
        try:
            await app2.resolve_peer(invitelink)
        except:
            pass

    ruser = message.from_user.first_name
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"𝙎𝙤𝙧𝙧𝙮, 𝙏𝙧𝙖𝙘𝙠 𝙇𝙤𝙣𝙜𝙚𝙧 𝙏𝙝𝙖𝙣  {DURATION_LIMIT} 𝙈𝙞𝙣 𝘼𝙧𝙚 𝙉𝙤𝙩 𝘼𝙡𝙡𝙤𝙬𝙚𝙙 𝙏𝙤 𝙥𝙡𝙖𝙮 𝙤𝙣  {BOT_NAME}."
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        file_path = (
            await message.reply_to_message.download(file_name)
            if not os.path.isfile(os.path.join("downloads", file_name))
            else f"downloads/{file_name}"
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            title = results[0]["title"]
            duration = results[0]["duration"]
            videoid = results[0]["id"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            return await GJ516.edit_text(f"𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙒𝙚𝙣𝙩 𝙒𝙧𝙤𝙣𝙜 \n\n**𝙀𝙧𝙧𝙤𝙧 :** `{e}`")

        if (dur / 60) > DURATION_LIMIT:
            return await GJ516.edit_text(
                f"𝙎𝙤𝙧𝙧𝙮, 𝙏𝙧𝙖𝙘𝙠 𝙇𝙤𝙣𝙜𝙚𝙧 𝙏𝙝𝙖𝙣   {DURATION_LIMIT} 𝙈𝙞𝙣 𝘼𝙧𝙚 𝙉𝙤𝙩 𝘼𝙡𝙡𝙤𝙬𝙚𝙙 𝙏𝙤 𝙥𝙡𝙖𝙮 𝙤𝙣  {BOT_NAME}."
            )
        file_path = audio_dl(url)
    else:
        if len(message.command) < 2:
            return await GJ516.edit_text("𝙒𝙝𝙖𝙩  𝘿𝙤 𝙔𝙤𝙪 𝙬𝙖𝙣𝙣𝙖 𝙋𝙡𝙖𝙮 ?")
        await GJ516.edit_text("💸")
        query = message.text.split(None, 1)[1]
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            videoid = results[0]["id"]
            duration = results[0]["duration"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            LOGGER.error(str(e))
            return await GJ516.edit("𝙁𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝙋𝙧𝙤𝙘𝙚𝙨𝙨 𝙦𝙪𝙚𝙧𝙮, 𝙏𝙧𝙮 𝙋𝙡𝙖𝙮𝙞𝙣𝙜 𝙖𝙜𝙖𝙞𝙣...")

        if (dur / 60) > DURATION_LIMIT:
            return await GJ516.edit(
                f"𝙎𝙤𝙧𝙧𝙮, 𝙏𝙧𝙖𝙘𝙠 𝙇𝙤𝙣𝙜𝙚𝙧 𝙏𝙝𝙖𝙣  ᴛʜᴀɴ  {DURATION_LIMIT} 𝙈𝙞𝙣 𝘼𝙧𝙚 𝙉𝙤𝙩 𝘼𝙡𝙡𝙤𝙬𝙚𝙙 𝙏𝙤 𝙥𝙡𝙖𝙮 𝙤𝙣  {BOT_NAME}."
            )
        file_path = audio_dl(url)

    try:
        videoid = videoid
    except:
        videoid = "fuckitstgaudio"
    if await is_active_chat(message.chat.id):
        await put(
            message.chat.id,
            title,
            duration,
            videoid,
            file_path,
            ruser,
            message.from_user.id,
        )
        position = len(GJ516db.get(message.chat.id))
        qimg = await gen_qthumb(videoid, message.from_user.id)
        await message.reply_photo(
            photo=qimg,
            caption=f"**⏳ 𝘼𝙙𝙙𝙚𝙙 𝙩𝙤 𝙌𝙪𝙚𝙪𝙚 𝙖𝙩 #{position}**\n\n**💡𝙏𝙞𝙩𝙡𝙚:** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n**⏱𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣:** `{duration}`\n**👤𝘼𝙙𝙙𝙚𝙙 𝘽𝙮:** {ruser}",
            reply_markup=buttons,
        )
    else:
        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.join_group_call(
                message.chat.id,
                stream,
                stream_type=StreamType().pulse_stream,
            )

        except NoActiveGroupCall:
            return await GJ516.edit_text(
                "**𝙉𝙤 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩 𝙁𝙤𝙪𝙣𝙙.**\n\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙏𝙝𝙚 𝙑𝙤𝙞𝙘𝙚𝘾𝙝𝙖𝙩 ."
            )
        except TelegramServerError:
            return await GJ516.edit_text(
                "𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙞𝙨 𝙝𝙖𝙫𝙞𝙣𝙜 𝙎𝙤𝙢𝙚 𝙄𝙣𝙩𝙚𝙧𝙣𝙖𝙡 𝙋𝙧𝙤𝙗𝙡𝙚𝙢, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙨𝙩𝙖𝙧𝙩 𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩 𝘼𝙣𝙙 𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣."
            )
        except UnMuteNeeded:
            return await GJ516.edit_text(
                f"» {BOT_NAME} 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙞𝙨 𝙈𝙪𝙩𝙚𝙙 𝙊𝙣 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩,\n\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙐𝙣𝙢𝙪𝙩𝙚  {ASS_MENTION} 𝙊𝙣 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩 𝘼𝙣𝙙 𝙏𝙧𝙮 𝙋𝙡𝙖𝙮𝙞𝙣𝙜 𝘼𝙜𝙖𝙞𝙣."
            )

        imgt = await gen_thumb(videoid, message.from_user.id)
        await stream_on(message.chat.id)
        await add_active_chat(message.chat.id)
        await message.reply_photo(
            photo=imgt,
            caption=f"**📡 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 💡**\n\n**💡𝙏𝙞𝙩𝙡𝙚:** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n**👤𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝘽𝙮:** {ruser}",
            reply_markup=buttons,
        )

    return await GJ516.delete()
