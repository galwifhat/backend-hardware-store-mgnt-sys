from . import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from datetime import datetime


class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    customer_id = Column(Integer(), ForeignKey("customers.id"))
    total_amount = Column(Float)
    sold_at = Column(DateTime, default=datetime.now())
