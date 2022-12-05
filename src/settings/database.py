# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# Project
from src.settings.settings import DATABASE
from src.settings.settings import Base

# Session maker
def create_sessionmaker():
    """Sets the database parameters that will be used to start sessions."""
    uri = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DATABASE['DB_USERNAME'],
        password=DATABASE['DB_PASSWORD'],
        host=DATABASE['DB_HOST'],
        name=DATABASE['DB_NAME'],
        port=DATABASE['DB_PORT']
    )

    try:
        db_engine = create_engine(uri)
        Base.metadata.create_all(db_engine)

    except OperationalError:
        print('Something failed')
        raise OperationalError

    return sessionmaker(db_engine), db_engine


Session, engine = create_sessionmaker()