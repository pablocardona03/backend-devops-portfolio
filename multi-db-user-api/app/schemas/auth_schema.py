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
