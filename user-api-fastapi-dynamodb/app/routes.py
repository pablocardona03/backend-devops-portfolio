from fastapi import APIRouter, HTTPException
from app.models import User
from app.dynamo import table
from boto3.dynamodb.conditions import Key
from uuid import uuid4
from typing import List

router = APIRouter()

@router.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    user.id = str(uuid4()) 
    table.put_item(Item=user.dict())
    return user

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    response = table.get_item(Key={"id": user_id})
    if "Item" not in response:
        raise HTTPException(status_code=404, detail="User not found")
    return response["Item"]

@router.get("/users", response_model=List[User])
def list_users():
    response = table.scan()
    return response.get("Items", [])

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    response = table.get_item(Key={"id": user_id})
    if "Item" not in response:
        raise HTTPException(status_code=404, detail="User not found")
    table.delete_item(Key={"id": user_id})
    return

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, updated_user: User):
    response = table.get_item(Key={"id": user_id})
    if "Item" not in response:
        raise HTTPException(status_code=404, detail="User not found")

    updated_data = updated_user.dict()
    updated_data["id"] = user_id  
    table.put_item(Item=updated_data)
    return updated_data
