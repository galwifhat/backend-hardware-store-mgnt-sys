# This python file imports all my models
from database import Base  # my declarative base
from database.customers import Customers
from database.brands import Brands
from database.category import Categories
from database.products import Products
from database.purchaseitems import PurchaseItems
from database.purchases import Purchases
from database.salesitems import Sales_Items
from database.sales import Sales
from database.trash import Trash

# importing all other models
