"""Database file that has everything related to the SQLAlchemy connection.

   This file contains database URL constants, creates an engine, a session,
   declares a dependency.
"""
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
LOCAL_DB_URL = 'postgresql+psycopg2://nev:pass@localhost:5432/storm'
if DATABASE_URL is not None:
    conn_string = DATABASE_URL[11:]
    engine = create_engine('postgresql+psycopg2://'+conn_string,
                           echo=True, pool_pre_ping=True, pool_use_lifo=True)
else:
    engine = create_engine(LOCAL_DB_URL, echo=True,
                           pool_pre_ping=True, pool_use_lifo=True)

# create Postgres db engine


# declare model base
Base = declarative_base(engine)

# define session
SessionLocal = sessionmaker(autocommit=False, bind=engine)


def get_db():
    """Creates a session object.

    :yield: Yields a database session.
    :rtype: Returns SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
