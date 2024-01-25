from aiogram import F, Router
from aiogram.types import Message
from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json

router = Router()

@router.message(F.text.lower().in_(["хай", "хеллоу", "приветик"]))
async def greetings(message: Message):
    await message.reply("Привет, дружище!!!!")


#Обработка текста с кнопок стартового меню
@router.message()
async def echo(message: Message):
    msg = message.text.lower()      # все проверки проводить после этого только в нижнем регистре
    smiles = await get_json("smiles.json")

    if msg == 'ссылки':
        await message.answer("Вот Вам ссылки на мои социальные сети!", reply_markup = inline.links)
    if msg == 'спец.кнопки':
        await message.answer("Специальные кнопки!", reply_markup = reply.spec)
    if msg == 'калькулятор':
        await message.answer("Ваш персональный калькулятор!", reply_markup = builders.calc())
    if msg == 'смайлики':
        await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup = fabrics.paginator())

