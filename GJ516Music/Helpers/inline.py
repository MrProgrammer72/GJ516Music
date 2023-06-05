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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from GJ516Music import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="❰𝗖𝗹𝗼𝘀𝗲❱", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT),
            
        ]
    ]
)


jaybuttons = InlineKeyboardMarkup(
    [
         [

InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/export_gabbar"),

InlineKeyboardButton (text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT),

         ]
    ]
)



pm_buttons = [
    [
        InlineKeyboardButton(
            text="❰𝘼𝘿𝘿𝙈𝙀❱",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true" ),
   
        InlineKeyboardButton(text="❰𝙃𝙀𝙇𝙋❱", callback_data="GJ516_help"),
    ],
 [ 
InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=config.OWNER_ID),
     ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="➕ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ➕ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true" ),
        InlineKeyboardButton(text="❰𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧❱", url=f"https://t.me/export_gabbar"),
     ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="𝘽𝙤𝙩 𝙪𝙨𝙚𝙧",
            callback_data="GJ516_cb help",
        ),
    
        InlineKeyboardButton(text="𝙎𝙪𝙙𝙤 𝙪𝙨𝙚𝙧", callback_data="GJ516_cb sudo"),
   ],

    [
        InlineKeyboardButton(text="◁", callback_data="GJ516_home"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="◁",
callback_data="GJ516_home"),
    InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),

    ],
]
