from sqladmin import Admin, ModelView
from fastapi import FastAPI
from data.engine import async_engine, session_maker  # твои настройки базы данных
from data.models import User, Category, Product  # твои модели

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


# Простой бэкенд авторизации (можно сделать токены, OAuth, сессии — пока сделаем просто)
class SimpleAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        return form.get("username") == "admin" and form.get("password") == "1234"

    async def logout(self, request: Request) -> bool:
        return True

    async def authenticate(self, request: Request):
        if request.session.get("token") == "authenticated":
            return True
        return False


# Инициализация FastAPI и Admin
app = FastAPI()

admin = Admin(app, engine=async_engine, authentication_backend=SimpleAuth())

# Создаем представления для моделей
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.user_id, User.username, User.first_name, User.last_name]

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]

class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.price, Product.category_id, Product.user_id]
    form_excluded_columns = ["id"]
    icon = "🍽️"

# Регистрируем модели
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(ProductAdmin)
