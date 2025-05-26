# data/engine.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from data.config import load_config

config = load_config()

if not config.db.dsn:
    raise RuntimeError("DB_LITE не прочитана из .env — проверьте load_config()")

# создаём движок по DSN из конфига
engine = create_async_engine(config.db.dsn, echo=True)

session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def create_db():
    # если у вас есть Base в data.models
    from data.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)






# import os
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
# from data.models import Base
#
#
#
#
# # образец подключения базы данных sqlite3
# engine = create_async_engine(os.getenv('DB_LITE'), echo=True)
#
# # DB_URL=postgresql+asyncpg://dev:golovchenko84@localhost:5432/bun_presentation
# # engine = create_async_engine(os.getenv('DB_URL'), echo=True) # движок для постгрес
#
# session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#
#
# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#     # async with session_maker() as session:
#     #     await orm_create_categories(session, categories)
#     #     await orm_add_banner_description(session, description_for_info_pages)
#
#
# async def drop_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)