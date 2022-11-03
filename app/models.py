from core_.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
import datetime
import sqlalchemy


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    is_active = Column(Boolean, default=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    hashed_password = Column(String)
    date_created = Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())
    # @classmethod
    # async def get(cls, id):
    #     query = cls.select().where(cls.c.id == id)
    #     user = await db.fetch_one(query)
    #     return user

    # @classmethod
    # async def create(cls, **user):
    #     query = cls.insert().values(**user)
    #     user_id = await db.execute(query)
    # return user_id


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
