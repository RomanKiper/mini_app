DB_PATH = "data/bot.db"

# data/config.py
from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    id_admins: list[int]
    id_admin: int

@dataclass
class Database:
    dsn: str

@dataclass
class Config:
    tg_bot: TgBot
    db: Database

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    # читаем все нужные переменные
    tg_token = env('BOT_TOKEN')
    id_admins = list(map(int, env.list('ID_ADMINS')))
    id_admin   = env.int('ID_MAIN_ADMIN')
    db_dsn     = env('DB_LITE', "sqlite+aiosqlite:///./data/bot.db")

    return Config(
        tg_bot=TgBot(
            token=tg_token,
            id_admins=id_admins,
            id_admin=id_admin,
        ),
        db=Database(dsn=db_dsn),
    )
