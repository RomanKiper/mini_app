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



