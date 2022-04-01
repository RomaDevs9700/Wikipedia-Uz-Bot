import logging
import wikipedia

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''
wikipedia.set_lang('uz')
ADMINS = []  # your telegram id

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start_welcome(message: types.Message):
    await message.reply(f"Salom 👋 {message.from_user.full_name}! \n"
                        f"🌏 Wikipedia Qidiruvi Botiga Xush Kelibsiz!")
    if message.from_user.username:
        user_n = message.from_user.username
    else:
        user_n = "username yo'q"
    msg = f"{message.from_user.full_name} va @{user_n} foydalanuvchi Wikipedia botdan foydalandi"
    await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.message_handler(commands=['help'])
async def send_help_welcome(message: types.Message):
    await message.reply(f"✅ Wikipedia Qidiruvi Botidan foydalanish uchun bizga maqolani mavzusini yuboring! \n"
                        f"❗  Maqola mavzusi to'g'ri kiritilmasa yoki Wikipediada majud bo'lmasa,\n"
                        f"Siz kiritgan mavzudagi maqola topilmaganligi bo'yicha xabar yuboriladi!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)