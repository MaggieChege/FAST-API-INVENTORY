from fastapi import FastAPI
from typing import List
from .models import User

app = FastAPI()

users = []


# @app.get("/users", response_model=List[User])
# async def get_users():
#     return users


@app.post("/users")
async def create_user(user):
    users.append(user)
    return {"message": f"Hello {users}"}


@app.get("/users/{id}")
async def get_user(id: int):
    return {"users": users[id]}
