from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am AR Music Player, I Can Stream Music In Voice Chat Newely Introduced By Telegram

Use The Buttons Below To Know More About Me..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡️ My. Creater", url="https://t.me/ARCretionGroup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AR_Malayalam_Songs"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/Malayalam_Dj_Songs_AR"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
