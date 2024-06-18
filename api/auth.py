from fastapi import APIRouter
from database import session, ENGINE
from pydantic import BaseModel
from typing import Optional
from models import User
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from werkzeug import security
import datetime


session = session(bind=ENGINE)

auth_router = APIRouter(prefix="/auth")


class RegisterModel(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_superuser: bool = False
    is_staff: bool = False
    is_active: bool = True
    date_joined: str = datetime.datetime.now()
    reset_password: str


class LoginModel(BaseModel):
    username: str
    password: str


@auth_router.get("/")
async def auth():
    return {
        "message": "This is auth page"
    }


@auth_router.post("/register")
async def register(user: RegisterModel):

    if user.reset_password != user.password:
        return {
            "message": "password and reset_password are not like"
        }

    username = session.query(User).filter(User.username == user.username).first()
    if username:
        message = f"{user.username} username already exists"
        return {
            "message": message
        }

    email = session.query(User).filter(User.email == user.email).first()
    if email:
        message = f"This {user.email} is in use"
        return {
            "message": message
        }

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        password=security.generate_password_hash(user.password),
        email=user.email
    )
    session.add(new_user)
    session.commit()

    return HTTPException(status_code=status.HTTP_201_CREATED)


@auth_router.post("/login")
async def login(user: LoginModel):

    check_user = session.query(User).filter(User.username == user.username).first()

    if check_user:
        password = check_user.password

        if security.check_password_hash(password, user.password):
            return HTTPException(status_code=status.HTTP_200_OK, detail={"username": user.username,
                                                                         "message": "User found"})

        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"username": user.username,
                                                                                "message": "Password incorrect"})

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"username": user.username,
                                                                        "message": "No user with this username"})