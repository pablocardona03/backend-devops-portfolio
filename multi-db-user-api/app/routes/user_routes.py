from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.crud import user_crud
from app.db.postgres import get_db
from app.utils.jwt import get_current_user
from app.models.auth_model import AuthUser  # <- importante para tipar el usuario autenticado

router = APIRouter()

# GET /users/
@router.get("/", response_model=List[UserResponse])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    return await user_crud.get_all_users(db)

# GET /users/{user_id}
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    user = await user_crud.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST /users/
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    return await user_crud.create_user(user_data, db)

# PUT /users/{user_id}
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: UUID,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    user = await user_crud.update_user(user_id, user_data, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# DELETE /users/{user_id}
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    success = await user_crud.delete_user(user_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
