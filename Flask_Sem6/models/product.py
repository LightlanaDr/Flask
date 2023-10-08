from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(title="Наименование", max_length=32)
    description: str = Field(title="Описание", max_length=128)
    price: int


class Product(BaseModel):
    prod_id: int
    name: str = Field(title="Наименование", max_length=32)
    description: str = Field(title="Описание", max_length=128)
    price: int
