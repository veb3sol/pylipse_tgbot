from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from keyboards import reply, inline, builders, fabrics
from contextlib import suppress

from data.subloader import get_json

router = Router()

# логика для нашего пагинатора
# @dp.callback_query(bord2.Pagination.filter())  # если ничего не передавать в фильтер - можем обрабатывать все две кнопки Вперед  и Назад
#@dp.callback_query(bord2.Pagination.filter(F.action == "prev"))  # можно делать обработчик на каждую кнопку отдельно
@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))  # для обработки нескольких кнопок
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    smiles = await get_json("smiles.json")
    # print(smiles)
    # print(smiles)
    # callback_data.action  -- тут находится текст prev или next
    # callback_data.page  -- тут находится номер страницы
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0
    #!!! телеграм вывидет сообщение что невозможно изменить сообщение так как оно идентичное предыдущему(если нажимать постоянно кнопку)

    if callback_data.action == "next":
        page = page_num + 1 if page_num < 3 else page_num

    # меняем текст сообщения со смайликом исходя из того на какой мы страничке
    # !!! телеграм вывидет сообщение что невозможно изменить сообщение так как оно идентичное предыдущему(если нажимать постоянно кнопку)
    with suppress(TelegramBadRequest):      # игнорируем ошибки телеграма
        await call.message.edit_text(
            f"{smiles[page][0]} <b>{smiles[page][1]}</b>", # выводим нужный смайлик и описание к нему
            reply_markup = fabrics.paginator(page),   # выводим клавиатуру с нужной страничкой
        )
    await call.answer() #пустой ответ - даем понять aiogram что мы обработали кнопку
