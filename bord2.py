# импортируем классы для создания клавы
from aiogram.types import (
    ReplyKeyboardMarkup,    #крепится под полем ввода
    KeyboardButton,         #ReplyKeyboardMarkup - кнопки для ReplyKeyboardMarkup
    InlineKeyboardMarkup,   #крепится под самими сообщениями
    InlineKeyboardButton,    #кнопки для InlineKeyboardMarkup
    KeyboardButtonPollType,   #для создания викторины (quiz) или голосования(regular)
)
# для работы с Билдером
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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
    input_field_placeholder = "Выберите действие с меню", # текст в меню для активации клавы
    selective = True, # для чатов, клава активируется только у того кто ее вызвал???
)


# обработчик "ссылки"
links_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Instagram', url = "https://www.instagram.com/chemodan_blog/"),
            InlineKeyboardButton(text = 'Youtube', url = "https://www.youtube.com/channel/UCWFU4cESpwDhRS-zQzSorJg"),
            InlineKeyboardButton(text = 'Telegram', url = "tg://resolve?domain=CosmoIryna")
            #  t.me://CosmoIryna    -- откроется в браузере
            #  tg://resolve?domain=CosmoIryna    -- откроется в телеграм
        ]
    ]
)

# обработчик "спец.кнопки"
spec_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Отправить ГЕО', request_location = True),  #request_location - отправлять геолокацию
            KeyboardButton(text = 'Отправить контакт', request_contact = True),  #request_contact - отправлять контакт
            KeyboardButton(text = 'Создать викторину', request_poll = KeyboardButtonPollType()),
            #request_poll = KeyboardButtonPollType() - создать викторину или голосование
            #request_poll = KeyboardButtonPollType("quiz") - создать викторину
            #request_poll = KeyboardButtonPollType("regular") - создать голосование

        ],
        [
            KeyboardButton(text="НАЗАД"),
        ]
    ],
    resize_keyboard = True
)

# билдэр всегда возращается функцией
# билдээр калькулятора
def calc_kb():
    items = [
        "1", "2", "3", "/",
        "4", "5", "6", "*",
        "7", "8", "9", "-",
        "0", ".", "=", "+",
    ]
    builder = ReplyKeyboardBuilder()
    # создаем кнопки
    # for item in items:
    #     builder.button(text=item)
    # или обраьтмся к генератору
    [builder.button(text=item) for item in items]
    builder.button(text="НАЗАД")
    # для контроля сколько кнопок должно быть в каком ряду
    builder.adjust(4,4,4,4) # в каждом ряду по 4 кнопки

    return builder.as_markup(resize_keyboard=True)
    # resize_keyboard=True  -- что бы все кнопки стали маленькими