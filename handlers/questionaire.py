# заполнение анкеты
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.builders import profile

from utils.states import Form

from keyboards.reply import rmk

router = Router()

@router.message(Command('profile'))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "Давай начнем, введи свое имя",
        reply_markup = profile(message.from_user.first_name)
    )

# Обрабатываем стейт
@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("Отлично, теперь укажи возраст.", reply_markup = rmk)

@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer("Теперь укажи пол", reply_markup = profile(["Парень", "Девушка"]))
    else:
        await message.answer("Введите число еще раз!")

@router.message(Form.sex, F.text.casefold().in_(["парень", "девушка"]))
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Form.about)
    await message.answer("Расскажи немного о себе", reply_markup = rmk)

# если не парень и не девушка, а написал что то от себя
@router.message(Form.sex)
async def incorrect_form_sex(message: Message, state: FSMContext):  #state: FSMContext - не используем, но без него не работает
    await message.answer("Нажать надо на кнопку!")

@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 10:
        await message.answer("Напиши больше о себе, а то совсем мало!")
    else:
        await state.update_data(about = message.text)
        await state.set_state(Form.photo)
        await message.answer("Теперь отправь свое фото!")

@router.message(Form.photo, F.photo)
async def form_photo(mesage: Message, state: FSMContext):
    photo_file_id = mesage.photo[-1].file_id  # -1 потому что надо получить последний элемент, а это фото в хорошем качестве
    # это последний элемент и нам надо получить все данные
    data = await state.get_data()
    #завершаем стейт
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]

    # отправляем фото и данные о юзере
    await mesage.answer_photo(photo_file_id, "\n".join(formatted_text))

# если отправил не фото
@router.message(Form.photo, ~F.photo)       # ~F.photo   -- не фото
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer("Отправь фото")
