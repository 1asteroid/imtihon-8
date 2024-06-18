
from fastapi import APIRouter, status, HTTPException
from models import Product
from database import session, ENGINE
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


product_router = APIRouter(prefix='/product')

session = session(bind=ENGINE)


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    slug: str
    image: str
    price: float
    description: str
    create_date: str = datetime.now()


@product_router.get('/')
async def product_list():
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "slug": product.slug,
            "image_url": product.image,
            "create_date": product.create_date
        }
        for product in products
    ]
    return jsonable_encoder(context)


@product_router.post('/create')
async def product_create(product: ProductModel):
    check_product_id = session.query(Product).filter(Product.id == product.id).first()

    if check_product_id is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bu product allaqachon mavjud")

    # elif check_product_id is None and check_category_id:
    new_product = Product(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        slug=product.slug,
        image=product.image,
        create_date=product.create_date
    )
    session.add(new_product)
    session.commit()
    data = {
        "code": 201,
        "success": True,
        "msg": "Created new product",
        "data": {
            "id": new_product.id,
            "name": new_product.name,
            "description": new_product.description,
            "price": new_product.price,
            "slug": product.slug,
            "image_url": product.image,
            "create_date": product.create_date,
        }
    }
    return data


@product_router.get('/{id}')
async def product_id(id: int):
    check_product = session.query(Product).filter(Product.id == id).first()
    if check_product:
        context = {
            "id": check_product.id,
            "name": check_product.name,
            "description": check_product.description,
            "price": check_product.price,
            "slug": check_product.slug,
            "image_url": check_product.image,
            "create_date": check_product.create_date,
        }
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bunday product mavjud emas")


@product_router.put('/{id}')
async def update_product(id: int, data: ProductModel):
    product = session.query(Product).filter(Product.id == id).first()

    if product:

        for key, value in data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        session.commit()

        data = {
            "code": 200,
            "message": "Update product"
        }
        return jsonable_encoder(data)

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed section")


@product_router.delete('/{id}')
async def product_delete(id: int):
    check_product = session.query(Product).filter(Product.id == id).first()
    if check_product:
        session.delete(check_product)
        session.commit()
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Deleted successfully")
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not fount")