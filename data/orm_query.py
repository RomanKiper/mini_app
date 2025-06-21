from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data.models import User, Category, Product
from typing import List


async def orm_add_user(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    username: str | None = None,
    phone: str | None = None,
):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            User(user_id=user_id, first_name=first_name, last_name=last_name, phone=phone, username=username)
        )
        await session.commit()


async def orm_get_categories(session: AsyncSession) -> List[Category]:
    result = await session.execute(select(Category))
    return result.scalars().all()


async def orm_get_products_by_category(category_id: int, session: AsyncSession) -> List[Product]:
    stmt = select(Product).where(Product.category_id == category_id)
    result = await session.execute(stmt)
    return result.scalars().all()