import enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.types import Enum

from app.core.database.database import Base


class DeleteStatus(str, enum.Enum):
    Y = 'Y'
    N = 'N'


class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(String, unique=True, index=True)
    name = Column(String)
    budget = Column(String)
    release_date = Column(String)
    creation_time = Column(String, server_default=func.now())
    updation_time = Column(String, onupdate=func.now(), server_default=func.now())
    is_deleted = Column(Enum(DeleteStatus), server_default="N")
