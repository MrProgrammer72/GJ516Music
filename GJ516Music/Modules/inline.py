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

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from GJ516Music import BOT_NAME, app


@app.on_inline_query()
async def inline_query_handler(_, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await app.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="𝙏𝙮𝙥𝙚 𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙏𝙤 𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜 𝙊𝙣 𝙔𝙤𝙪𝙏𝙪𝙗𝙚 ♪",
                cache_time=10,
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝙔𝙤𝙪𝙏𝙪𝙗𝙚",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
✨ **𝙏𝙞𝙩𝙡𝙚 :** [{title}]({link})

⏳ **𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣 :** `{duration}`𝙈𝙞𝙣𝙨
👀 **𝙑𝙞𝙚𝙬𝙨 :** `{views}`
⏰ **𝙋𝙪𝙗𝙡𝙞𝙨𝙝𝙚𝙙 𝙊𝙣 :** {published}
🎥 **𝘾𝙝𝙖𝙣𝙣𝙚𝙡:** [{channel}]({channellink})

<u>💖 **𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗣𝗼𝘄𝗲𝗿𝗱 𝗯𝘆 {BOT_NAME}**</u>"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await app.answer_inline_query(query.id, results=answers)
        except:
            return
