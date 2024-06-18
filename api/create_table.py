from database import ENGINE, Base
from models import User, Product, Order, OrderItem, Team, Blog
Base.metadata.create_all(ENGINE)
