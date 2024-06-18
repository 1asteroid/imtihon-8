from pydantic import BaseModel
from typing import Optional

# class RegisterModel(BaseModel):
#     id: Optional[int]
#     first_name: str
#     last_name: str
#     username: str
#     email: str
#     password: str
#     is_staff: Optional[bool]
#     is_active: Optional[bool]
#
#
# class LoginModel(BaseModel):
#     username: str
#     password: str
#
#
# class ProductModel(BaseModel):
#     id: Optional[int]
#     name: str
#     slug: str
#     image: str
#     price: float
#     description: str
#
#
# class OrderModel(BaseModel):
#     id: Optional[int]
#     user_id: Optional[int]
#     paid: bool
#     complete: bool
#
#
# class OrderItemModel(BaseModel):
#     id: Optional[int]
#     product_id: Optional[int]
#     count: int
#     order_id: Optional[int]
#
#
# class TeamModel(BaseModel):
#     id: Optional[int]
#     name: str
#     team_id: Optional[int]
#     text: str
#     image: str
#
#


class JwtModel(BaseModel):
    authjwt_secret_key: str = 'e83b71885bdf56a5437f6fa32cddefaee70b95e5106e769509e1b3707f838d56'
