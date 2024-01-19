# импортируем классы для создания клавы
from aiogram.types import (
    ReplyKeyboardMarkup,    #крепится под полем ввода
    KeyboardButton,         #ReplyKeyboardMarkup - кнопки для ReplyKeyboardMarkup
    InlineKeyboardMarkup,   #крепится под самими сообщениями
    InlineKeyboardButton    #кнопки для InlineKeyboardMarkup
)

#основная клавиатура для команды start
main_kb = ReplyKeyboardMarkup(
    keyboard = [
        # 1 строка с кнопками
        [
            KeyboardButton(text="Смайлики"),
            KeyboardButton(text="Ссылки")
        ],
        # 2 строка с кнопками
        [
            KeyboardButton(text="Калькулятор"),
            KeyboardButton(text="Спец.кнопки")
        ]
    ],
    resize_keyboard = True,  #кнопки адаптируются под кнопки телефона - стают маленькими
    one_time_keyboard = True, # клава скрывается после первого использования
    input_field_placeholder = "Выдерите действие с меню", # текст в меню для активации клавы
    selective = True, # для чатов, клава активируется только у того кто ее вызвал???
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Instagram', url = "https://www.instagram.com/chemodan_blog/"),
            InlineKeyboardButton(text = 'Youtube', url = "https://www.youtube.com/channel/UCWFU4cESpwDhRS-zQzSorJg"),
            # InlineKeyboardButton(text = 'Telegram', url = "tg://resolve?dbmain=@CosmoIryna")
        ]
    ]
)