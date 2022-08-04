from pydantic import BaseModel
from typing import Optional
from core.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    is_active = Column(Boolean, default=True)
    email = Column(String, unique=True, index=True)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
