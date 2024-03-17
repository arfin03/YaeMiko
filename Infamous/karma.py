# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/255a4d983cbcb6f2714c3.jpg",   
    "https://telegra.ph/file/e1e68e5a1c1899997ce7f.jpg",
    "https://telegra.ph/file/4734d09fa1937300e8aba.jpg",
    "https://telegra.ph/file/255a4d983cbcb6f2714c3.jpg",
    "https://telegra.ph/file/e1e68e5a1c1899997ce7f.jpg",
    "https://telegra.ph/file/4734d09fa1937300e8aba.jpg",
]

HEY_IMG = "https://telegra.ph/file/02e11123253d1882d9ed2.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/255a4d983cbcb6f2714c3.jpg",
    "https://telegra.ph/file/e1e68e5a1c1899997ce7f.jpg",
    "https://telegra.ph/file/ed4385c26dcf6de70543f.jpg",
    "https://telegra.ph/file/4734d09fa1937300e8aba.jpg",
    "https://telegra.ph/file/255a4d983cbcb6f2714c3.jpg",
    "https://telegra.ph/file/e1e68e5a1c1899997ce7f.jpg",
    "https://telegra.ph/file/4734d09fa1937300e8aba.jpg",
]

FIRST_PART_TEXT = "✨ *Hey* `{}` . . ."

PM_START_TEXT = "✨ *im Fubuki, A new generation group manager bot with extreme futures*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ ADD ME ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        
    ],
    [
        InlineKeyboardButton(text="OWNER", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="OWNER", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/fubuki_supports"),
        ib(text="SUPPORT", url="https://t.me/rg_anime_group"),
    ],
    [
        ib(
            text="➕ ADD ME ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
