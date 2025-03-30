import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import router
from bot.database import init_db

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)  # Подключаем рутеры

    init_db()  # Инициализируем базу данных при запуске

    await bot.send_message(chat_id="1006569664", text="✅ Бот запущен!")  # Уведомление о запуске
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

