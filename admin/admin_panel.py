# admin/admin_panel.py

from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy import create_engine
from data.models import User, Category, Product, Base  # важно импортировать Base!
from data.config import load_config


# Загружаем конфиг и получаем строку подключения
config = load_config()

# Приводим строку подключения к синхронному варианту для sqlite
SQLALCHEMY_DATABASE_URL = config.db.dsn.replace("+asyncpg", "").replace("+aiosqlite", "")

# Создаём синхронный движок SQLAlchemy
sync_engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# ВАЖНО: создаём таблицы в базе (если их ещё нет)
Base.metadata.create_all(bind=sync_engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.user_id, User.first_name, User.last_name, User.username, User.phone]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-list"


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.price, Product.category_id]
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-burger"


def setup_admin(app: FastAPI):
    admin = Admin(app=app, engine=sync_engine, title="Админка Mini App", base_url="/admin")
    admin.add_view(UserAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(ProductAdmin)






