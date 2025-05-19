
from aiogram import Router, types
from aiogram.filters import CommandStart
from data.mistral import get_mistral_response
from data.orm_query import orm_add_user
from sqlalchemy.ext.asyncio import AsyncSession
from data.utils import escape_markdown_v2

router = Router()



# 📂 Загрузка знаний компании с экранированием
with open("bot/company_info.md", "r", encoding="utf-8") as file:
    raw_company_knowledge = file.read()
    company_knowledge = escape_markdown_v2(raw_company_knowledge)

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
    await message.answer("🤖 Привет! Я бот, использующий Mistral AI. Напиши мне что-нибудь!")

# 📬 Отправка длинного сообщения по частям
async def send_long_message(message: types.Message, text: str):
    max_length = 4096
    for i in range(0, len(text), max_length):
        await message.answer(text[i:i + max_length], disable_web_page_preview=True)

# 🤖 Основной хендлер для ответов на вопросы
@router.message()
async def consult_user(message: types.Message):
    user_text = escape_markdown_v2(message.text)  # экранируем ввод пользователя
    prompt = (
        f"Ты персональный помощник в компании ЗАО 'Сливки бай'. "
        f"Давай короткие, четкие ответы.\n"
        f"У тебя есть информация о компании:\n{company_knowledge}\n"
        f"Вопрос: {user_text}"
    )

    response = get_mistral_response(prompt)

    if not response:
        response = "Я не смог найти ответ. Попробуйте задать вопрос по-другому."

    response = escape_markdown_v2(response)
    await send_long_message(message, response)









###############################################################33

# from aiogram import Router, types
# from aiogram.filters import CommandStart
# from data.mistral import get_mistral_response
# from data.orm_query import orm_add_user
# from sqlalchemy.ext.asyncio import AsyncSession
# from data.mistral import get_mistral_response
#
#
# router = Router()
#
#
# # with open("bot/company_info.txt", "r", encoding="utf-8") as file:
# with open("bot/company_info.md", "r", encoding="utf-8") as file:
#     company_knowledge = file.read()
#
#
# @router.message(CommandStart())
# async def start_handler(message: types.Message, session: AsyncSession):
#
#     await orm_add_user(session,
#                        user_id=message.from_user.id,
#                        username=message.from_user.username,
#                        first_name=message.from_user.first_name,
#                        last_name=message.from_user.last_name,
#                        )
#     await message.answer("🤖 Привет! Я бот, использующий Mistral AI. Напиши мне что-нибудь!")
#
#
#
# async def send_long_message(message: types.Message, text: str):
#     max_length = 4096
#     for i in range(0, len(text), max_length):
#         await message.answer(text[i:i + max_length], disable_web_page_preview=True)
#
#
# @router.message()
# async def consult_user(message: types.Message):
#     user_text = message.text
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
#     await send_long_message(message, response)


##################################################################################################

# with open("bot/company_info.md", "r", encoding="utf-8") as file:
#     company_knowledge = file.read()
#
# @router.message()
# async def consult_user(message: types.Message):
#     user_text = message.text
#     prompt = f"Ты персональный помошник в компании ЗАО 'Сливки бай'. У тебя есть информация о компании:\n{company_knowledge}\nВопрос: {user_text}"
#     response = get_mistral_response(prompt)
#
#     if not response:
#         response = "Я не смог найти ответ. Попробуйте задать вопрос по-другому."
#
#     await message.answer(response,
#                          disable_web_page_preview=True)









# @router.message()
# async def chat_handler(message: types.Message):
#     user_text = message.text
#     response = get_mistral_response(user_text)
#
#     # Проверяем, что response не None и не пустая строка
#     if not response or response is None:
#         response = "Ошибка: модель не смогла обработать запрос."
#
#     # save_message(message.from_user.id, user_text, response)  # Сохраняем в БД
#
#     await message.answer(response)

