from fastapi import APIRouter, status, HTTPException
from models import Order
from database import session, ENGINE
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

order_router = APIRouter(prefix='/order')

session = session(bind=ENGINE)


class OrderModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    paid: bool
    complete: bool
    create_date: str = datetime.now()


@order_router.get('/')
async def order_list():
    orders = session.query(Order).all()

    context = [
        {
            "id": order.id,
            "user_id": order.user_id,
            "paid": order.paid,
            "complete": order.complete,
            "create_date": order.create_date,
        }
        for order in orders
    ]

    return jsonable_encoder(context)
