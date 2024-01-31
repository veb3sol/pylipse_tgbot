from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import Callable, Awaitable, Dict, Any

from keyboards.inline import sub_channel

class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        # 2 способа получить bot
        # bot = data.get("bot")
        chat_member = await event.bot.get_chat_member("@Beauty_Kyiv_Sity", event.from_user.id)
        print("5555555555")
        if chat_member.status == 'left':
            await event.answer("Для взаимодействия с ботом подпишись на наш канал!", reply_markup = sub_channel)
        else:
            return await handler(event, data)
        #     print('33333333333333333333')