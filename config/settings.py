import os
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


DATABASE = {
    "DB_HOST": os.getenv("DB_HOST", default="db"),
    "DB_PORT": os.getenv("DB_PORT", default=5432),
    "DB_PASSWORD": os.getenv("DB_PASSWORD", default="postgres"),
    "DB_USERNAME": os.getenv("DB_USERNAME", default="postgres"),
    "DB_NAME": os.getenv("DB_NAME", default="eight_queens"),
}


SERVER = {
    "HOST": os.getenv("HOST", default="0.0.0.0"),
    "PORT": os.getenv("PORT", default=8000),
    "DEBUG": os.getenv("DEBUG", default=False),
}
