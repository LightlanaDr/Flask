from typing import List

from fastapi import APIRouter, HTTPException
from db import database, products
from models.product import ProductIn, Product

router = APIRouter()



@router.get("/fake_prod/{count}")
async def create_prod(count: int):
    """ Заполнение таблицы Продукты """
    for i in range(count):
        query = products.insert().values(name=f'name{i}',
                                         description=f'description{i}',
                                         price=f'{i + 100}')
        await database.execute(query)
    return {'message': f'{count} fake products create'}



@router.post("/product/", response_model=dict)
async def create_product(product: ProductIn):
    """ Добавить новый продукт """
    query = products.insert().values(name=product.name,
                                     description=product.description,
                                     price=product.price)
    await database.execute(query)
    return {"Ok": product}



@router.put("/product/{prod_id}", response_model=dict)
async def update_user(prod_id: int, new_user: ProductIn):
    """ Обновление продукта в БД, update """
    query = products.update().where(products.c.prod_id == prod_id).values(**new_user.model_dump())
    await database.execute(query)
    return {"Ok": new_user, "id": prod_id}


@router.get("/products/", response_model=List[Product])
async def read_products():
    """ Вывести список всех продуктов """
    query = products.select()
    return await database.fetch_all(query)

@router.get("/product/{prod_id}", response_model=Product)
async def read_product(prod_id: int):
    """ Вывести один продукт """
    query = products.select().where(products.c.prod_id == prod_id)
    return await database.fetch_one(query)

@router.delete("/product/{prod_id}")
async def delete_product(prod_id: int):
    """ Удалить продукт из базы данных """
    query = products.delete().where(products.c.prod_id == prod_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
