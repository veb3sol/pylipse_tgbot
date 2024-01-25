from random import random

from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram import Router

from keyboards import reply

router = Router()

@router.message(CommandStart())  #CommandStart() - обрабатывает команду start
async def start(message: Message):
    await message.answer("Hello!!!", reply_markup = reply.main)

@router.message(Command(commands = ['rn', 'rando'])) # rn 1-100  мы хотим так задавать диапазон. без разницы /rn или /rando
async def get_random_number(message: Message, command: CommandObject):     # передавать именно название command
    #await message.answer(command.args)  # /rn 55555  -- вернет 55555
    a, b = [int(n) for n in command.args.split('-')] # вернет например [1, 100]
    rnum = random.randint(a,b)
    await message.reply(f'Случайное число {rnum}')
