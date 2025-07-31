from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
