from database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


# class Trash(Base):
#     __tablename__ = "trash"
#     id = Column(Integer(), primary_key=True, autoincrement=True)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     deleted_at = Column(DateTime(timezone=True), default=datetime.now())

#     # product rlshp lets us access the full product via record.product
#     product = relationship("Product", backref="trash_entries")
