from fastapi import FastAPI

from app.api import api
from app.settings import settings

app = FastAPI()

app.include_router(api.router, prefix=settings.API_V1_STR)
