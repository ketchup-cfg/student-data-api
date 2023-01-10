from fastapi import APIRouter

from app.models.students import Student

router = APIRouter()


@router.get("/students")
async def get_students() -> list[Student]:
    """Return all students."""
    return [Student(name="Trevor Pierce"), Student(name="Not Trevor Pierce")]
