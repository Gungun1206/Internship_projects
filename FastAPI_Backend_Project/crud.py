from models import User
from sqlalchemy import select

async def create_user(db, user_data):

    user = User(
        name=user_data.name,
        email=user_data.email
    )

    db.add(user)

    await db.commit()

    await db.refresh(user)

    return user

async def get_users(db):

    result = await db.execute(
        select(User)
    )

    return result.scalars().all()
