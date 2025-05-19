import asyncio
import logging
from aiogram import Bot, Dispatcher
# from bot.config import BOT_TOKEN
from data.config import load_config, Config
from bot.handlers.handlers import router
# from bot.database import init_db
from data.engine import create_db, session_maker
from bot.keyboards.main_menu import set_main_menu
from middlewares.db import DataBaseSession
from data.utils import escape_markdown_v2

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

config: Config = load_config()

async def on_startup(bot):
    # await drop_db()
    await create_db()
    print("Бот запущен")

async def on_shutdown(bot):
    print('Бот лег')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode="MarkdownV2"))
    dp = Dispatcher()

    # bot = Bot(
    #     token=config.tg_bot.token,
    #     default=DefaultBotProperties(parse_mode="HTML")
    # )


    dp.include_router(router)  # Подключаем рутеры
    dp.update.middleware(DataBaseSession(session_pool=session_maker))  # сессия на все хэндлеры
    # await drop_db()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await set_main_menu(bot)
    await bot.send_message(config.tg_bot.id_admin, text='Бот запущен')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


