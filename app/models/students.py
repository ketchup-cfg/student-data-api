from pydantic import BaseModel


class Student(BaseModel):
    """Student user for the system."""

    name: str
