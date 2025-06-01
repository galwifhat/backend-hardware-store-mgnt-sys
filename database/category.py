from . import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    category_name = Column(String(), unique=True)
    created_at = Column(DateTime, default=datetime.now())
