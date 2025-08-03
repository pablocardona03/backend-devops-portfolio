# app/models/auth_model.py
from sqlalchemy import Column, String
from app.db.postgres import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class AuthUser(Base):
    __tablename__ = "auth_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


# app/schemas/auth_schema.py
from pydantic import BaseModel, Field

class AuthUserCreate(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "admin",
                "password": "strongpassword123"
            }
        }

class AuthUserLogin(BaseModel):
    username: str
    password: str


# app/utils/security.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
