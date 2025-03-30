from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.mistral import get_mistral_response
from bot.database import save_message

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("🤖 Привет! Я бот, использующий Mistral AI. Напиши мне что-нибудь!")


@router.message()
async def chat_handler(message: types.Message):
    user_text = message.text
    response = get_mistral_response(user_text)

    # Проверяем, что response не None и не пустая строка
    if not response or response is None:
        response = "Ошибка: модель не смогла обработать запрос."

    save_message(message.from_user.id, user_text, response)  # Сохраняем в БД

    await message.answer(response)

