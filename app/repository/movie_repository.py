import uuid

import bleach
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.models import models
from app.core.schemas import MoviesSchema


def movie_query(db: Session):
    """
    :param db: DB dependency injection
    :return: return Query Class which return active movies
    """
    return db.query(models.Movies).filter(models.Movies.is_deleted == 'N')


def get_movie_by_movie_id(movie_id: str, db: Session):
    """
    :param movie_id: String
    :param db: DB dependency injection
    :return: return Query Class which return active movies with particular id
    """
    movie = movie_query(db).filter(models.Movies.movie_id == movie_id)
    if not movie.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Movie with the id {movie_id} is not available")
    return movie


def get_movie_by_ids(movie_ids, db):
    """
    :param movie_ids: List (array) of movie ID's
    :param db:
    :return: List of all movies
    """
    return db.query(models.Movies).filter(models.Movies.movie_id.in_(tuple(movie_ids))).all()


def add_movies(movie_items: MoviesSchema.AddMovies, db: Session):
    """
    Add multiple movies
    :param movie_items: List of movies
    :param db:
    :return: Dictionary with List of all movies
    TODO: Already exists movies not checked
    """
    movie_ids = []
    for item in movie_items.movies:
        movie_id = str(uuid.uuid4())
        movie_ids.append(movie_id)
        new_item = models.Movies(movie_id=movie_id,
                                 name=bleach.clean(item.name),
                                 release_date=bleach.clean(item.release_date),
                                 budget=bleach.clean(item.budget))

        db.add(new_item)
        db.commit()
    movies = get_movie_by_ids(movie_ids, db)
    return {"movies": movies}
