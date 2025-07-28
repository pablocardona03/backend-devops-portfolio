from fastapi import APIRouter, HTTPException
from .models import User
from .db import table

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    table.put_item(Item=user.dict())
    return {"message": "User created successfully"}
