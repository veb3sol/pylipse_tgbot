
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# обработчик "ссылки"
links = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Instagram', url = "https://www.instagram.com/chemodan_blog/"),
            InlineKeyboardButton(text = 'Youtube', url = "https://www.youtube.com/channel/UCWFU4cESpwDhRS-zQzSorJg"),
            InlineKeyboardButton(text = 'Telegram', url = "tg://resolve?domain=RuslanRuzh")
            #  t.me://CosmoIryna    -- откроется в браузере
            #  tg://resolve?domain=CosmoIryna    -- откроется в телеграм
        ]
    ]
)
