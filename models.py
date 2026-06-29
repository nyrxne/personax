from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    occupation: str
    skills: list[str]
    hobbies: list[str]
    education: str
    favorite_language: str
    career_goals: str