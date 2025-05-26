
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from data.orm_query import orm_add_user
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


router = Router()


# 🎬 Старт-команда
@router.message(CommandStart())
async def start_handler(message: types.Message, session: AsyncSession):
    await orm_add_user(
        session,
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await message.answer("🤖 Привет! Я бот для теста первого mini_app для ресторанов и кафе.")



@router.message(F.text == "/mini_app")
async def start_handler(message: Message):
    # Кнопка, которая открывает именно Mini App, а не внешний браузер
    web_app_btn = InlineKeyboardButton(
        text="Открыть Mini App",
        web_app=WebAppInfo(url="https://574ec79cbc18d09bf8fc624bef0a0515.serveo.net/mini_app")

    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[web_app_btn]])

    # Делаем ответ и прикрепляем клавиатуру
    await message.answer(
        "Нажми на кнопку ниже, чтобы открыть наше мини-приложение:",
        reply_markup=kb
    )



# @router.message(F.text == "/mini_app")
# async def start_handler(message: Message):
#     web_app_btn = InlineKeyboardButton(
#         text="Открыть Mini App",
#         web_app=WebAppInfo(url="https://mycafebot.serveo.net/mini_app")
#     )
#     kb = InlineKeyboardMarkup(inline_keyboard=[[web_app_btn]])
#     await message.answer(
#         "Нажми на кнопку ниже, чтобы открыть наше мини-приложение:",
#         reply_markup=kb
#     )






# # 📂 Загрузка знаний компании с экранированием
# with open("bot/company_info.md", "r", encoding="utf-8") as file:
#     raw_company_knowledge = file.read()
#     company_knowledge = escape_markdown_v2(raw_company_knowledge)


#
# # 📬 Отправка длинного сообщения по частям
# async def send_long_message(message: types.Message, text: str):
#     max_length = 4096
#     for i in range(0, len(text), max_length):
#         await message.answer(text[i:i + max_length], disable_web_page_preview=True)
#
# # 🤖 Основной хендлер для ответов на вопросы
# @router.message()
# async def consult_user(message: types.Message):
#     user_text = escape_markdown_v2(message.text)  # экранируем ввод пользователя
#     prompt = (
#         f"Ты персональный помощник в компании ЗАО 'Сливки бай'. "
#         f"Давай короткие, четкие ответы.\n"
#         f"У тебя есть информация о компании:\n{company_knowledge}\n"
#         f"Вопрос: {user_text}"
#     )
#
#     response = get_mistral_response(prompt)
#
#     if not response:
#         response = "Я не смог найти ответ. Попробуйте задать вопрос по-другому."
#
#     response = escape_markdown_v2(response)
#     await send_long_message(message, response)

