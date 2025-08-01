from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy import update as sql_update, delete as sql_delete
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID, uuid4
from app.crud.log_crud import create_log

# ✅ GET ALL USERS
async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

# ✅ GET USER BY ID
async def get_user_by_id(user_id: UUID, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

# ✅ CREATE USER + log
async def create_user(user_data: UserCreate, db: AsyncSession):
    user_id = str(uuid4())
    new_user = User(id=user_id, **user_data.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    await create_log(
        action="create_user",
        user_id=user_id,
        details={"email": user_data.email, "name": user_data.name}
    )

    return new_user

# ✅ UPDATE USER + log
async def update_user(user_id: UUID, user_data: UserUpdate, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None

    before_update = {"name": user.name, "email": user.email}

    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email

    await db.commit()
    await db.refresh(user)

    await create_log(
        action="update_user",
        user_id=str(user_id),
        details={
            "before": before_update,
            "after": {"name": user.name, "email": user.email}
        }
    )

    return user

# ✅ DELETE USER + log
async def delete_user(user_id: UUID, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return False

    await db.delete(user)
    await db.commit()

    await create_log(
        action="delete_user",
        user_id=str(user_id),
        details={
            "deleted_user": {
                "name": user.name,
                "email": user.email
            }
        }
    )

    return True
