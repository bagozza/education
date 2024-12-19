import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {'message': 'Главная страница'}


@app.get("/admin")
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def id_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter ur ID', exampl=1)]
) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get("/user/{username}/{age}")
async def user_dict(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]
) -> dict:
    return {f'Информация о пользователе. Имя': {username}, 'Возраст': {age}}


if __name__ == "__main__":
    uvicorn.run("module_16_2:app", host="127.0.0.1", port=8000, workers=4)
