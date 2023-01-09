from fastapi import APIRouter

router = APIRouter()


@router.get("/students")
async def get_students():
    """Return all students."""
    return [{"name": "Trevor Pierce"}, {"name": "Not Trevor Pierce"}]
