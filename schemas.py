from pydantic import BaseModel


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
