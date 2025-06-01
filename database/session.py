from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Cretae an engine that connects with out db
engine = create_engine("sqlite:///hardware.db", echo=True)
# 2. create a session and import
Session = sessionmaker(bind=engine)
#  3. for fastapi, we need to create a func of method that returns the session


def get_db():
    session = Session()
    # try and catch
    try:
        yield session
    finally:
        session.close()
