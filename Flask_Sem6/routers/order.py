from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from db import database, orders, users, products
from models.order import OrderIn, Order

router = APIRouter()


@router.post("/order", response_model=dict)
async def add_order(order: OrderIn):
    """ Создать заказ """
    query = orders.insert().values(user_id=order.user_id,
                                   prod_id=order.prod_id,
                                   date=order.date,
                                   status=order.status)
    last_record_id = await database.execute(query)
    return {"Ok": order, "id": last_record_id}


@router.get("/orders/", response_model=List[Order])
async def read_orders():
    """ Вывести список всех заказов """
    query = orders.select()

    # query = select(orders.c.order_id.label('order_id'), orders.c.date.label('date'),
    #                orders.c.status.label('status'),
    #                users.c.user_id.label('user_id'), users.c.username.label('username'),
    #                users.c.lastname.label('lastname'), users.c.email.label('email'),
    #                products.c.prod_id.label('prod_id'), products.c.name.label('name'),
    #                products.c.description.label('description'), products.c.price.label('price')
    #                ).join(products).join(users)
    # Выводит данные так:
    # {
    #     "order_id": 1,
    #     "user_id": 2,
    #     "prod_id": 2,
    #     "date": "2023-10-08",
    #     "status": "Ожидает оплаты"
    # }???
    # Почему-то не выводить указанные в запросе поля. Работает также, как query = orders.select()

    return await database.fetch_all(query)


@router.put("/order/{order_id}", response_model=dict)
async def update_order(order_id: int, new_order: OrderIn):
    """ Обновление заказа """
    query = orders.update().where(orders.c.order_id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {"Ok": new_order, "id": order_id}


@router.get("/order/{order_id}", response_model=Order)
async def read_order(order_id: int):
    """ Вывод заказа по id """
    query = orders.select().where(orders.c.order_id == order_id)
    return await database.fetch_one(query)


@router.delete("/order/{order_id}")
async def delete_product(order_id: int):
    """ Удаление заказа """
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}
