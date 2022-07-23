from http import HTTPStatus

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.core.database import database
from app.core.dependency.LoggingDependency import LoggingDependency
from app.core.schemas import MoviesSchema
from app.service.v1 import movie_service

router = APIRouter(
    prefix="/movie",
    tags=['Movie'],
    route_class=LoggingDependency
)

get_db = database.get_db


@router.get('/{movie_id}', status_code=status.HTTP_200_OK, response_model=MoviesSchema.GetMovie)
def get_movie_by_movie_id(movie_id: str, db: Session = Depends(get_db)):
    return movie_service.get_movie_by_movie_id(movie_id, db)


@router.delete('/{cart_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_movie_by_movie_id(movie_id: str, db: Session = Depends(get_db)):
    is_deleted = movie_service.delete_movie_by_movie_id(movie_id, db)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=MoviesSchema.GetMovies)
def add_movies(request: MoviesSchema.AddMovies, db: Session = Depends(get_db)):
    return movie_service.add_movies(request, db)
