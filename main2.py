import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

#импортируем клаву
import bord2

token = '6376558301:AAHa1nHkRWa-KWcAoMzaZ-xFq8FiSh8Y1M0'
bot = Bot(token, parse_mode = "HTML")
dp = Dispatcher()

@dp.message(CommandStart())  #CommandStart() - обрабатывает команду start
async def start(message: Message):
    await message.answer("Hello!!!", reply_markup = bord2.main_kb)

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())