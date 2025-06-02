from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

# this is my catalog -> stores all products info
class Products(Base):
    __tablename__ = "products"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    product_name = Column(String(), nullable=False)
    sku = Column(String(), nullable=False, unique=True)
    brand_id = Column(Integer(), ForeignKey("brands.id"))
    category_id = Column(Integer(), ForeignKey("categories.id"))
    image_url = Column(String(), default=0)
    current_stock = Column(Integer)  # current stock = Total Purchase - Total Sold
    is_deleted = Column(Boolean(), default=False)

#buying price - seen by manager
#selling price seen buy customer
    
    purchases = relationship("PurchaseItems", back_populates="product", cascade=("all, delete-orphan"))
    sales = relationship("Sales_Items", back_populates="product")
    brand = relationship("Brands", back_populates="products")