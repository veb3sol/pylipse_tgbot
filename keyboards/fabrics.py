from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# создаем пагинацию  -- реализуем тут фабрику колбэков
class Pagination(CallbackData, prefix="page"):   # унаследовались от CallbackData
    action: str     # действие
    page: int      # номер страницы

# билдер для пагинации
def paginator(page:int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text = "⬅", callback_data = Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text = "➡", callback_data = Pagination(action="next", page=page).pack()),
        width = 2  # сколько кнопок в одной строке - по умолчанию - 3
        # pack() - генерирует строку
    )
    return builder.as_markup()