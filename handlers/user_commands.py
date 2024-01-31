from random import random

from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram import Router

from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import CheckForDigit

router = Router()

#@router.message(CommandStart(), IsAdmin(732140356))  #CommandStart() - обрабатывает команду start
@router.message(CommandStart())  #CommandStart() - обрабатывает команду start
# IsAdmin(732140356) --- если True то сработает
async def start(message: Message):
    await message.answer("Hello!!!", reply_markup = reply.main)

@router.message(Command("pay"), CheckForDigit())
async  def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer('Вы успешно оплатили товар!')


@router.message(Command(commands = ['rn', 'rando'])) # rn 1-100  мы хотим так задавать диапазон. без разницы /rn или /rando
async def get_random_number(message: Message, command: CommandObject):     # передавать именно название command
    #await message.answer(command.args)  # /rn 55555  -- вернет 55555
    a, b = [int(n) for n in command.args.split('-')] # вернет например [1, 100]
    rnum = random.randint(a,b)
    await message.reply(f'Случайное число {rnum}')
