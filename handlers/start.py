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

I am Music Player, an bot BY @VKPROJECTS that lets you play music in your Telegram groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Share♐️", url="tg://msg?text=Hai%20Friend+❤️,+Today%20i+just+found+out+an+intresting+and+Powerful+**Music+BOT**+for+Free🥰.+**Bot+Link**+:+@AR_MUSIC_STREAMER_BOT+🔥"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/VKP_BOTS"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/VKPROJECTS"
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
