from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite3
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# postgres
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:qwer1234@localhost:5432/postgres'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# mysql


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
