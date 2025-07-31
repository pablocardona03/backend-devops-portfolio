from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy import update as sql_update, delete as sql_delete
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_id(user_id: UUID, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    return user

async def create_user(user_data: UserCreate, db: AsyncSession):
    new_user = User(name=user_data.name, email=user_data.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def update_user(user_id: UUID, user_data: UserUpdate, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None

    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email

    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(user_id: UUID, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return False

    await db.delete(user)
    await db.commit()
    return True
