from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove,
)

#основная клавиатура для команды start
main = ReplyKeyboardMarkup(
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

# обработчик "спец.кнопки"
spec = ReplyKeyboardMarkup(
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

rmk = ReplyKeyboardRemove()