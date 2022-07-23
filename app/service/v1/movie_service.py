from sqlalchemy.orm import Session

from app.core.schemas import MoviesSchema
from app.repository import movie_repository


def get_movie_by_movie_id(movie_id: str, db: Session):
    """
    give movie details by id
    """
    return movie_repository.get_movie_by_movie_id(movie_id, db).first()


def delete_movie_by_movie_id(movie_id: str, db: Session):
    """
    delete movies by id - Soft delete
    """
    movie = movie_repository.get_movie_by_movie_id(movie_id, db)
    movie.update({"is_deleted": "Y"})
    db.commit()
    return True


def add_movies(request: MoviesSchema.AddMovies, db: Session):
    """
    add multiple movies
    """
    return movie_repository.add_movies(request, db)
