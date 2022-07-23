from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel


class GetMovie(BaseModel):
    movie_id: str
    name: str
    budget: Optional[str] = None
    release_date: Optional[date] = None
    creation_time: Optional[datetime] = None
    updation_time: Optional[datetime] = None
    is_deleted: str

    class Config:
        orm_mode = True


class DeleteMovie(BaseModel):
    movie_id: str

    class Config:
        orm_mode = True


class UpdateMovie(BaseModel):
    name: Optional[str]
    budget: Optional[str]
    release_date: Optional[str]

    class Config:
        orm_mode = True


class AddMovie(BaseModel):
    name: str
    budget: Optional[str] = None
    release_date: Optional[str] = None

    class Config:
        orm_mode = True


class AddMovies(BaseModel):
    movies: List[AddMovie]

    class Config:
        orm_mode = True


class GetMovies(BaseModel):
    movies: List[GetMovie]

    class Config:
        orm_mode = True
