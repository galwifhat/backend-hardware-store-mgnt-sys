from . import Base
from sqlalchemy import Column, Integer, DateTime, Text, Float
from datetime import datetime
from sqlalchemy.orm import relationship


class Purchases(Base):
    __tablename__ = "purchases"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    purchase_date = Column(DateTime, default=datetime.now())
    total_cost = Column(Float())
    note = Column(Text())

    items = relationship("PurchaseItems", back_populates="purchases")

