from typing import List
from fastapi import APIRouter, HTTPException
from db import users, database
from models.user import User, UserIn

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f'username{i}',
                                      lastname=f'lastname{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post("/user", response_model=dict)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username,
                                  lastname=user.lastname,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {"Ok": user, "id": last_record_id}


@router.put("/users/{user_id}", response_model=dict)
async def update_user(user_id: int, new_user: UserIn):
    """Обновление пользователя в БД, update"""
    query = users.update().where(users.c.user_id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {"Ok": new_user, "id": user_id}


@router.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
