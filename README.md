**Key relationships in my system**

- One-to-Many (Most Common)
- Many-to-One
- Many-to-many (I am not implementing this for now)

- I will use back_populates for the bidirectional relationships

## A Brand has many Products (one-to-many)

- one brand can have many products
- so, in the brand Model, we can have a relationship to Products -> foreignkey

## A Category has many Products (one-to-many)

- a relationship to Product -> foreign key

## A Purchase has many PurchaseItems (one-to-many)

- one Purchase can have many PurchaseItems
- in Purchase model - define a rlshp to Purchase Item

## A Sale has many SaleItems (one-to-many)

- one Sale can have many salesItems -> rlshp to SaleItems

## A Product has many PurchaseItems and many SaleItems (one-to-many)

- have a relsp to both salesItems and PurchaseItems

# Query Relationships

# Get all products for a brand

- (brand referes to a variable just created)
  brand = session.query(Brands).filter_by(brand_name="Nike").first()
  for product in brand.products:
  print(product.product_name)

      brand.products gives you a list of all Products related to that brand.
      product.brand gives you the Brands object related to a given product.

       brand in brand.products refers to the brand variable, which is an instance of the Brands class — it's not referring to the class itself, or the other brand in product.brand

# Output: Air Max, Dry-Fit Tee

# Get brand from a product

product = session.query(Products).filter_by(product_name="Air Max").first()
print(product.brand.brand_name) # Output: Nike
