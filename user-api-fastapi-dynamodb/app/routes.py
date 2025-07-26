from fastapi import APIRouter, HTTPException
from app.models import User
from app.dynamo import table
from boto3.dynamodb.conditions import Attr
from typing import List

router = APIRouter()

@router.post("/users", status_code=201)
def create_user(user: User):

    response = table.scan(FilterExpression=Attr("email").eq(user.email))
    if response.get("Items"):
        raise HTTPException(status_code=400, detail="Email already registered")

    table.put_item(Item=user.dict())
    return {"message": "User created successfully", "user_id": user.id}

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

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, updated_user: User):
    existing = table.get_item(Key={"id": user_id})
    if "Item" not in existing:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user.id = user_id 
    table.put_item(Item=updated_user.dict())
    return updated_user

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    response = table.get_item(Key={"id": user_id})
    if "Item" not in response:
        raise HTTPException(status_code=404, detail="User not found")

    table.delete_item(Key={"id": user_id})
    return {"message": "User deleted"}
