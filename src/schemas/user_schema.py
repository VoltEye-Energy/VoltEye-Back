from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    status: str
    id: int
    name: str
    email: str
