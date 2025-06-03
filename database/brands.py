from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class Brands(Base):
    __tablename__ = "brands"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    brand_name = Column(String(), unique=True)
    created_at = Column(DateTime, default=datetime.now())

    products = relationship("Products", back_populates="brand")
