from pydantic import BaseModel
from sqlalchemy import DateTime


class BrandSchema(BaseModel):
    brand_name: str


class CategorySchema(BaseModel):
    category_name: str


class CustomerSchema(BaseModel):
    customer_name: str
    customer_phone: str


class ProductsSchema(BaseModel):
    product_name: str
    sku: str
    brand_id: int
    category_id: int
    image_url: str
    current_stock: int


class PurchaseItemsSchema(BaseModel):
    purchase_id: int
    product_id: int
    quantity_added: int
    unit_cost: float


class PurchasesSchema(BaseModel):
    total_cost: float
    note: str


class SalesItemsSchema(BaseModel):
    sale_id: int
    product_id: int
    quantity_sold: int
    unit_price: float


class SalesSchema(BaseModel):
    customer_id: int
    total_amount: float


# Method 1
class TrashSchema(BaseModel):
    id: int
    product_id: int

    class Config:
        orm_mode = True


# Method 2
# the base schema
# common fields between input and output (like product_id)/shared fields
# Prevents code duplication.


# class TrashBase(BaseModel):
#     product_id: int


# # when creating a new trash record; Input when creating soft delete
# class TrashCreate(TrashBase):
#     pass
# # Output from backend/API; fields: id, product_id, deleted_at
# class TrashResponse(TrashBase):
#     id: int
#     deleted_at: DateTime

#     class Config:
#         orm_mode = True
