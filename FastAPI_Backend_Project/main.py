from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine
from database import get_db

from models import Base

from schemas import UserCreate

from crud import create_user
from crud import get_users

import time

app = FastAPI()

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.middleware("http")
async def log_requests(request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()

    print(f"Request Time: {end-start}")

    return response

@app.get("/")
async def home():
    return {"message": "FastAPI Running"}

@app.post("/users")
async def add_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    return await create_user(db, user)

@app.get("/users")
async def read_users(
    db: AsyncSession = Depends(get_db)
):

    return await get_users(db)
