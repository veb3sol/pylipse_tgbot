# билдэр всегда возращается функцией
# билдээр калькулятора
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def calc():
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