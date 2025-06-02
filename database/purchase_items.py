from . import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class PurchaseItems(Base):
    __tablename__ = "purchase_items"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    purchase_id = Column(Integer(), ForeignKey("purchases.id"))
    product_id = Column(Integer(), ForeignKey("products.id"))
    quantity_added = Column(Integer(), nullable=False)
    unit_cost = Column(Integer(), nullable=False)
    added_at = Column(DateTime, default=datetime.now())

    product = relationship("Products", back_populates="purchases")
    purchases = relationship("Purchases", back_populates="items")
