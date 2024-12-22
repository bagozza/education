import uvicorn
from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: Annotated[int, Path(ge=1, le=100, description='Enter ur ID', example=1)]
    username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Alexandr')]
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]


@app.get("/users")
async def get_all_messages() -> list[User]:
    return users


@app.post("/user/{user_id}/{username}/{age}")
async def create_message(user: User):
    user.id = len(users) + 1
    users.append(user)
    return f'user : {user}'


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user: User):
    for i in users:
        if i.id == user.id:
            i.username = user.username
            i.age = user.age
            return {"user": user}
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'Message with {user_id} was deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


if __name__ == "__main__":
    uvicorn.run("module_16_4:app", host="127.0.0.1", port=8000, workers=4)
   