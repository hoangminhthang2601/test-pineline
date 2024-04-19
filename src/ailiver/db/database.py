"""
Configure all the database connection of the BE.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_HOST"),
    os.environ.get("DB_NAME"),
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
