from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    is_active: bool
    bio: Optional[str]
    email: str
