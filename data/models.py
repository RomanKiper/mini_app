import json

from sqlalchemy import String, Float, Text, DateTime, func, ForeignKey, Numeric, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())



class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)



class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(5,2), nullable=False)
    image: Mapped[str] = mapped_column(String(150))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)

    category: Mapped['Category'] = relationship(backref='product')
    user: Mapped['User'] = relationship(backref='product')

    class User(Base):
        __tablename__ = "user"

        # Телеграм user_id
        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
        first_name: Mapped[str] = mapped_column(String(150), nullable=True)
        last_name: Mapped[str] = mapped_column(String(150), nullable=True)
        username: Mapped[str] = mapped_column(unique=False, nullable=True)
        phone: Mapped[str] = mapped_column(String(13), nullable=True)