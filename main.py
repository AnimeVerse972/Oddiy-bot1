from aiogram import Bot, Dispatcher, types from aiogram.types import Message from aiogram.utils import executor import os

TOKEN is loaded from environment variables

TOKEN = os.getenv("BOT_TOKEN")

Initialize bot and dispatcher

bot = Bot(token=TOKEN) dp = Dispatcher(bot)

Dictionary of anime post links by code

anime_posts = { "1": [10, 23, 35, 49, 76, 104, 851, 127, 131, 135, 148, 200, 216], "2": [222, 235, 260, 309, 343, 360, 379, 392, 405, 430, 462, 501, 514] # Add more codes and message_id lists as needed }

CHANNEL_USERNAME = "@AniVerseClip"  # Channel username

@dp.message_handler() async def send_anime(message: types.Message): code = message.text.strip() if code in anime_posts: await message.answer(f"🔎 Kod: {code}. Siz uchun {len(anime_posts[code])} ta xabar yuborilmoqda...") for msg_id in anime_posts[code]: await bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_USERNAME, message_id=msg_id) else: await message.answer("❌ Bunday kod topilmadi. Iltimos, 1 yoki 2 kabi mavjud kod yuboring.")

if name == 'main': executor.start_polling(dp)

