from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from uuid import uuid4
from datetime import datetime


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique user ID")
    name: str = Field(..., min_length=2, max_length=100, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat(), description="Creation timestamp in ISO format")

    class Config:
        schema_extra = {
            "example": {
                "name": "Pablo César",
                "email": "pablo@example.com"
            }
        }
