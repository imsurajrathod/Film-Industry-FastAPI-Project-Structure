from fastapi import FastAPI

from app.core.database.database import engine
from app.core.models import models
from app.routers.api import v1_router

app = FastAPI(title="Film Industry")

models.Base.metadata.create_all(engine)

app.include_router(v1_router.router)
