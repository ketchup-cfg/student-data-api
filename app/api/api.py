from fastapi import APIRouter

from app.api.endpoints import students

router = APIRouter()
router.include_router(students.router)
