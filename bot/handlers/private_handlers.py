

from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from filters.is_admin import IsAdminMsg
from filters.chat_types import ChatTypeFilter


admin_private_router = Router()
admin_private_router.message.filter(ChatTypeFilter(['private']), IsAdminMsg())
admin_private_router.callback_query.filter(IsAdminMsg())


@admin_private_router.message(F.text == "/mini_admin")
async def start_admin(message: Message):
    web_app_btn = InlineKeyboardButton(
        text="Открыть админку",
        web_app=WebAppInfo(url="https://miniminimini.serveo.net/admin")
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[web_app_btn]])
    await message.answer(
        "Нажми на кнопку ниже, чтобы открыть Админку:",
        reply_markup=kb
    )



