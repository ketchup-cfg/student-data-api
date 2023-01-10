from fastapi import FastAPI

from app.routes import students


app = FastAPI()

app.include_router(students.router)
