from xmlrpc.client import Boolean
from pydantic import BaseModel


class User(BaseModel):
    bio: str
    is_active: Boolean
    email: int

    class Config:
        orm_mode = True
