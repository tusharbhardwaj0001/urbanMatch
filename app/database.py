import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Free to use remote db or create a local database. Modify the URl appropriately
# SQLALCHEMY_DATABASE_URL = "sqlite:///./urbanMatch.db"
SQLALCHEMY_DATABASE_URL = "postgresql://mrikal:mrikal123@127.0.0.1:5432/urbanMatch"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

