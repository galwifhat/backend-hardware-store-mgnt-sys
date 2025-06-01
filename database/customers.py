# This is a customer class
from . import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    customer_name = Column(String(), nullable=False)
    customer_phone = Column(String(), nullable=False)
    created_at = Column(DateTime, default=datetime.now())


    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.customer_name}', phone='{self.customer_phone}')>"
