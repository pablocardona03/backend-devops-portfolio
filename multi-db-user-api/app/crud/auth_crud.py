from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from app.models.auth_model import AuthUser
from app.schemas.auth_schema import AuthUserCreate
from app.utils.security import hash_password, verify_password


async def register_user(user_data: AuthUserCreate, db: AsyncSession) -> AuthUser:
    hashed_pwd = hash_password(user_data.password)

    new_user = AuthUser(
        username=user_data.username,
        hashed_password=hashed_pwd
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def get_user_by_username(username: str, db: AsyncSession) -> Optional[AuthUser]:
    result = await db.execute(
        select(AuthUser).where(AuthUser.username == username)
    )
    return result.scalar_one_or_none()


async def authenticate_user(username: str, password: str, db: AsyncSession) -> Optional[AuthUser]:
    user = await get_user_by_username(username, db)
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
