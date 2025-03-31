
DB_PATH = "data/bot.db"

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    id_admins: list[int]  # Список id администраторов бота
    id_admin: int
    mistral_api_key: str # Токен для доступа к ии мистрал


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            id_admins=list(map(int, env.list('ID_ADMINS'))),
            id_admin=env('ID_MAIN_ADMIN'),
            mistral_api_key=env('MISTRAL_API_KEY')
        )
    )