from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.filters import CommandObject

from typing import Any

class CheckForDigit(BaseFilter):
    # async def __call__(self, message: Message, command: CommandObject) -> bool:
    async def __call__(self, message: Message, **data: Any) -> bool:
        # **data: Any   --- словарь
        print(data)
        command: CommandObject = data.get("command")
        arg = command.args
        if arg.isnumeric() or (arg.count('.') and arg.replace(".", "").isnumeric()):
            return True
        return False