
import pathlib
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.ext.asyncio import AsyncSession
from data.get_async_session import get_async_session
from data.orm_query import orm_get_categories
from data.config import load_config

# Загружаем конфиг из .env
config = load_config(".env")  # <-- обязательно путь к .env

# Логируем путь до базы
print(f"📦 Подключение к базе данных: {config.db.dsn}")

# Определяем путь до корня проекта
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


# Создаём FastAPI-приложение
app = FastAPI()

# Подключаем папку static
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Подключаем Jinja2-шаблоны
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/mini_app", response_class=HTMLResponse)
async def mini_app(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/menu", response_class=HTMLResponse)
async def get_menu(request: Request, session: AsyncSession = Depends(get_async_session)):
    try:
        # Получаем категории
        categories = await orm_get_categories(session)
        print("Категории:", categories)

        return templates.TemplateResponse("menu_category.html", {
            "request": request,
            "categories": categories
        })

    except Exception as e:
        print(f"❌ Ошибка при получении категорий: {e}")
        return HTMLResponse(content=f"<h1>Ошибка: {e}</h1>", status_code=500)



















