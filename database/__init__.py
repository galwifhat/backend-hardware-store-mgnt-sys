# creates Base
from sqlalchemy.ext.declarative import declarative_base

# create a base class
# This file defines the declarative base that all models will inherit from
Base = declarative_base()
metadata = Base.metadata

