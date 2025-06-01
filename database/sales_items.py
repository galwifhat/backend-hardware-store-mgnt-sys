from . import Base
from sqlalchemy import Column, Integer, Float, ForeignKey


class Sales_Items(Base):
    __tablename__ = "sales_items"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    sale_id = Column(Integer(), ForeignKey("sales.id"))
    product_id = Column(Integer(), ForeignKey("products.id"))
    quantity_sold = Column(Integer(), nullable=False)
    unit_price = Column(Float(), nullable=False)
