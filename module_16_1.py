import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {'message': 'Главная страница'}


@app.get("/admin")
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def id_user(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get("/user")
async def user_dict(username: str, age: int) -> dict:
    return {f'Информация о пользователе. Имя': {username}, 'Возраст': {age}}


if __name__ == "__main__":
    uvicorn.run("module_16_1:app", host="127.0.0.1", port=8000, workers=4)
