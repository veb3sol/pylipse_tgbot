from aiogram.filters import BaseFilter
from aiogram.types import Message

from typing import List    # что бы можно бало передавать не один id

class IsAdmin(BaseFilter):

    #необязательный метод
    def __init__(self, user_ids: int or List[int]) -> None: # принимает число или список чисел - idшники, ничего не вернет
            self.user_ids = user_ids

    #обязательный метод
    async def __call__(self, message: Message) -> bool: #принимает сообщение, вернет булево значение
        if isinstance(self.user_ids, int):          # если установленный id админа это число
            return message.from_user.id == self.user_ids    # тогда сравниваем с числом
        return message.from_user.id in self.user_ids    # если нет - то проверяем на наличеи такого id в списке


