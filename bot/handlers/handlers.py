
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from data.orm_query import orm_add_user
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from bot.lexicon.lexicon import TUNEL_URL


router = Router()


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
async def start_miniapp_handler(message: Message):
    web_app_btn = InlineKeyboardButton(
        text="Открыть Mini App",
        # web_app=WebAppInfo(url="https://miniminimini.serveo.net/mini_app")
        web_app=WebAppInfo(url=f"{TUNEL_URL}/mini_app")

    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[web_app_btn]])
    await message.answer(
        "Нажми на кнопку ниже, чтобы открыть наше мини-приложение:",
        reply_markup=kb
    )



