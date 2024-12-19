import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_message(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Alexandr')],
        age: int = Path(ge=18, le=120, description='Enter age', example=24)
) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    message = f'Имя: {username}, возраст: {age}'
    users[current_index] = message
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Alexandr')],
        age: int = Path(ge=18, le=120, description='Enter age', example=24),
        user_id: int = Path(ge=0)
) -> str:
    users[user_id] = f'Имя: {username}, возраст{age}'
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f'Message with {user_id} was deleted'


if __name__ == "__main__":
    uvicorn.run("module_16_3:app", host="127.0.0.1", port=8000, workers=4)
