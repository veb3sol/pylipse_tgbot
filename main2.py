import asyncio
from aiogram import Bot, Dispatcher

# вытягиваем нужные роутеры
from handlers import bot_messages, user_commands, questionaire
from callbacks import pagination

from config_reader import config

# token = '6665446931:AAF2haWZeMD8BZdiIR0eJWRZQTVIdGfWFk8'
# token = '6376558301:AAHa1nHkRWa-KWcAoMzaZ-xFq8FiSh8Y1M0'


# по поводу in_()   -- можно обрабатывать несколько входящих сообщений

async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode = "HTML")
    dp = Dispatcher()

    # указываем все роутеры -- очень важен порядок указания
    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router,
    )


    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())