import os
from ujson import loads # ujson быстрее чем json
import aiofiles  # позволяет синхронно работать с файлами

async def get_json(filename: str) -> list:
    path = f"data/{filename}"
    if os.path.exists(path):

        async with aiofiles.open(path, "r", encoding = "utf-8") as file:

            return loads(await file.read())
    return []       # если проверка не прошла



