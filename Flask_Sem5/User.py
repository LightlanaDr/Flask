# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class User(UserIn):
    id: int


users = []
for i in range(10):
    users.append(User(
        id=i + 1,
        name=f'name{i + 1}',
        email=f'email{i + 1}@mail.ru',
        password='123'
    ))


@app.get("/users", response_class=HTMLResponse)
async def get_user(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


if __name__ == "__main__":
    uvicorn.run("User:app", host="127.0.0.1", port=8060, reload=True)
