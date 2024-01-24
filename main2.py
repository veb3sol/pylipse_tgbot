import asyncio
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest  # для работы с ошибками телеграма

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

#импортируем клаву
import bord2

token = '6665446931:AAF2haWZeMD8BZdiIR0eJWRZQTVIdGfWFk8'
# token = '6376558301:AAHa1nHkRWa-KWcAoMzaZ-xFq8FiSh8Y1M0'
bot = Bot(token, parse_mode = "HTML")
dp = Dispatcher()

# набор смайликов
smiles = [
    ["🍕", "пицца готова!"],
    ["🍺", "пиво холодное подано!"],
    ["🍉", "арбуз нарезан!"],
    ["🥝", "обожаю киви!"],

]

@dp.message(CommandStart())  #CommandStart() - обрабатывает команду start
async def start(message: Message):
    await message.answer("Hello!!!", reply_markup = bord2.main_kb)

# логика для нашего пагинатора
# @dp.callback_query(bord2.Pagination.filter())  # если ничего не передавать в фильтер - можем обрабатывать все две кнопки Вперед  и Назад
#@dp.callback_query(bord2.Pagination.filter(F.action == "prev"))  # можно делать обработчик на каждую кнопку отдельно
@dp.callback_query(bord2.Pagination.filter(F.action.in_(["prev", "next"])))  # для обработки нескольких кнопок
async def pagination_handler(call: CallbackQuery, callback_data: bord2.Pagination):
    # callback_data.action  -- тут находится текст prev или next
    # callback_data.page  -- тут находится номер страницы
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0
    #!!! телеграм вывидет сообщение что невозможно изменить сообщение так как оно идентичное предыдущему(если нажимать постоянно кнопку)

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    # меняем текст сообщения со смайликом исходя из того на какой мы страничке
    # !!! телеграм вывидет сообщение что невозможно изменить сообщение так как оно идентичное предыдущему(если нажимать постоянно кнопку)
    with suppress(TelegramBadRequest):      # игнорируем ошибки телеграма
        await call.message.edit_text(
            f"{smiles[page][0]} <b>{smiles[page][1]}</b>", # выводим нужный смайлик и описание к нему
            reply_markup = bord2.paginator(page),   # выводим клавиатуру с нужной страничкой
        )
    await call.answer() #пустой ответ - даем понять aiogram что мы обработали кнопку

# по поводу in_()   -- можно обрабатывать несколько входящих сообщений
@dp.message(F.text.lower().in_(["хай", "хеллоу", "приветик"]))
async def greetings(message: Message):
    await message.reply("Привет, дружище!!!!")


#Обработка текста с кнопок стартового меню
@dp.message()
async def echo(message: Message):
    msg = message.text.lower()      # все проверки проводить после этого только в нижнем регистре
    if msg == 'ссылки':
        await message.answer("Вот Вам ссылки на мои социальные сети!", reply_markup = bord2.links_kb)
    if msg == 'спец.кнопки':
        await message.answer("Специальные кнопки!", reply_markup = bord2.spec_kb)
    if msg == 'калькулятор':
        await message.answer("Ваш персональный калькулятор!", reply_markup = bord2.calc_kb())
    if msg == 'смайлики':
        await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup = bord2.paginator())



async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())