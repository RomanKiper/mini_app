import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from data.config import load_config, Config
from bot.handlers.handlers import router
from data.engine import create_db, session_maker
from bot.keyboards.main_menu import set_main_menu
from middlewares.db import DataBaseSession

import uvicorn


####################################

from data.web_app import app as fastapi_app
from admin.admin_panel import setup_admin

# Настраиваем админку
setup_admin(fastapi_app)


config: Config = load_config()

async def on_startup(bot: Bot):
    await create_db()
    print("🟢 Bot started")

async def on_shutdown(bot: Bot):
    print("🔴 Bot stopped")


async def start_bot():
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    # подключаем хендлеры и middleware
    dp.include_router(router)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await set_main_menu(bot)
    await dp.start_polling(bot)


async def start_api():
    await create_db()
    config_uvicorn = uvicorn.Config(
        fastapi_app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
    server = uvicorn.Server(config_uvicorn)
    await server.serve()  # блокирует до остановки

async def main():
    logging.basicConfig(level=logging.INFO)
    # Запускаем бот и API **параллельно**
    bot_task = asyncio.create_task(start_bot())
    api_task = asyncio.create_task(start_api())

    # Ждём, пока оба сервиса не завершатся (обычно — Ctrl+C)
    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(main())


