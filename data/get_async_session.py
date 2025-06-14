# data/database.py

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from data.config import load_config

# Загружаем конфигурацию из .env
config = load_config(".env")

# ✅ Подключение к БД из конфигурации
DATABASE_URL = config.db.dsn
print(f"📦 Используем базу данных: {DATABASE_URL}")

# 🔧 Создаём движок
engine = create_async_engine(DATABASE_URL, echo=False)

# 🔧 Создаём фабрику сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# 🧱 Базовый класс для моделей
class Base(DeclarativeBase):
    pass

# 🔁 Зависимость FastAPI: создаёт сессию на каждый запрос
async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
