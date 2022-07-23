import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.config import get_configs

configs = get_configs()
# For Development, we will get config from local environment .env file
# For Production we will get from prod setup like OKD
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://" + configs.database_username + ":" + urllib.parse.quote_plus(
    configs.database_password) + "@" + configs.database_host + ":" + configs.database_port + "/" + configs.database

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       pool_pre_ping=True,
                       pool_recycle=configs.pool_recycle,
                       pool_timeout=configs.pool_timeout,
                       pool_size=configs.pool_size,
                       max_overflow=configs.max_overflow
                       )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    except is very important here. Because if you not close the connection in case of exception
    it will NOT close the connection in checkout
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as exception:
        db.close()
    finally:
        db.close()
