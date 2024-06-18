from sqlalchemy import Column,Boolean, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'auth_user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(String(40), nullable=True)
    username = Column(String(50))
    password = Column(String(300))
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime, default=datetime.now())
    user_order = relationship('Order', back_populates='user')


class Product(Base):
    __tablename__ = 'product_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    slug = Column(String(200))
    image = Column(String(200))
    price = Column(Float())
    description = Column(Text())
    product_orderitem = relationship('OrderItem', back_populates='product')


class Order(Base):
    __tablename__ = 'product_order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('auth_user.id'))
    user = relationship('User', back_populates='user_order')
    paid = Column(Boolean, default=False)
    complete = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now())
    order_orderitem = relationship('OrderItem', back_populates='order')


class OrderItem(Base):
    __tablename__ = 'product_orderitem'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product_product.id'))
    product = relationship("Product", back_populates="product_orderitem")
    count = Column(Integer, default=1)
    order_id = Column(Integer, ForeignKey("product_order.id"))
    order = relationship('Order', back_populates="order_orderitem")
    create_date = Column(DateTime, default=datetime.now())


class Team(Base):
    __tablename__ = 'product_team'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(200))
    speciality = Column(String(200))
    description = Column(Text())
    image = Column(String(200))
    blog = relationship("Blog", back_populates="team")


class Blog(Base):
    __tablename__ = 'product_blog'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    team_id = Column(Integer, ForeignKey('product_team.id'))
    team = relationship("Team", back_populates="blog")
    text = Column(Text())
    image = Column(String(200))
    create_date = Column(DateTime, default=datetime.now())

