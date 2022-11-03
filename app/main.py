from fastapi import FastAPI
from .schema import User as SchemaUser
from .models import User as ModelUser
# from core import db
# from core.db import db
app = FastAPI()

users = []


# @app.get("/users", response_model=List[User])
# async def get_users():
#     return users


# @app.post("/users")
# async def create_user(user):
#     users.append(user)
#     return {"message": f"Hello {users}"}


@app.get("/users/{id}")
async def get_user(id: int):
    return {"users": users[id]}


# @app.post("/user/", response_model=SchemaUser)
# def create_user(user: SchemaUser):
#     db_user = ModelUser(
#         first_name=user.first_name, last_name=user.last_name, age=user.age
#     )
#     db.session.add(db_user)
#     db.session.commit()
#     return db_user
