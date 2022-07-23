from fastapi import APIRouter

from app.routers.api.v1 import movie_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(movie_router.router)
