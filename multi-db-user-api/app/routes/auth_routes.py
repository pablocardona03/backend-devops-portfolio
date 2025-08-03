from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth_schema import AuthUserCreate, AuthUserLogin
from app.db.postgres import get_db
from app.crud.auth_crud import register_user, authenticate_user
from app.utils.jwt import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
async def register(user_data: AuthUserCreate, db: AsyncSession = Depends(get_db)):
    user = await register_user(user_data, db)
    return {"id": user.id, "username": user.username}

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
