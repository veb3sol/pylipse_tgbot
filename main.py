from aiogram import Bot, Dispatcher, F
# F -- проверки и фильтра
# Dispatcher -- получает апдейты в реальном времени
# Bot --- связывает нас с API telegram

from aiogram.enums.dice_emoji import DiceEmoji

import random
# random -- отвечает за рандомность

from aiogram.filters import Command, CommandObject
# Command -- что б каждый раз не писать обработчик
# CommandObject -- что бы без машины состояний реализовать задавание диапазона

from aiogram.types import Message
import asyncio  # позволяет писать ассинхронные функции

token = '6376558301:AAHa1nHkRWa-KWcAoMzaZ-xFq8FiSh8Y1M0'

bot = Bot(token, parse_mode = "HTML")
dp = Dispatcher()

# @dp.message(F.text == "/start")
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, <b>{message.from_user.first_name} !!!!</b>")

@dp.message(Command(commands = ['rn', 'rando'])) # rn 1-100  мы хотим так задавать диапазон
async def get_random_number(message: Message, command: CommandObject):     # передавать именно название command
    #await message.answer(command.args)  # /rn 55555  -- вернет 55555
    a, b = [int(n) for n in command.args.split('-')] # вернет например [1, 100]
    rnum = random.randint(a,b)
    await message.reply(f'Случайное число {rnum}')

@dp.message(F.text == 'play')
async def play_game(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    # answer_dice() -- отправляет вращающийся кубик
    print(x.dice.value)

    # await message.answer(f"У тебя выпало {x.dice.value}")  -- выводится раньше чем остановится кубик


@dp.message()
async def echo(message: Message):
    await message.answer(f"Я тебя не понимаю, {message.from_user.first_name}, неправильная команда!")


async def main():
    # удаляем веб хук который собирает сообщения в выключенном состоянии
    # отправленные сообщения во время выключеного бота не будут приходить
    await bot.delete_webhook(drop_pending_updates = True)

    #запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())    # запуск функции старта бота