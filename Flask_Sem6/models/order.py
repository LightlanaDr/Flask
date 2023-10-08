import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Status(Enum):
    unpaid = "Ожидает оплаты"
    paid = "Оплачен"
    delivery = "Передан в доставку"
    completed = "Доставлен"
    cancelled = "Отменен"


class OrderIn(BaseModel):
    user_id: int
    prod_id: int
    date: datetime.date
    status: Status = Field(title="Статус")

    class Config:
        use_enum_values = True


class Order(BaseModel):
    order_id: int
    user_id: int
    prod_id: int
    date: datetime.date
    status: Status = Field(title="Статус")

    class Config:
        use_enum_values = True
