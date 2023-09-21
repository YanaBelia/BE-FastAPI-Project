from fastapi import FastAPI
import os
from databases import Database
from dotenv import load_dotenv
from starlette.routing import Mount
from app.my_data.database import SQLALCHEMY_DATABASE_URL, engine
from app.models import models
import databases
from fastapi.middleware.cors import CORSMiddleware
from app.router.user import router
from app.router.auth import router1
from app.router.company import router2
from app.router.invite import router3

async def init_models():
    async with engine.begin() as con:
        await con.run_sync(models.Base.metadata.drop_all)
        await con.run_sync(models.Base.metadata.create_all)


app = FastAPI()
basedir = os.path.abspath(os.path.dirname("../"))
load_dotenv(dotenv_path=f"{basedir}/.env")
db = databases.Database(SQLALCHEMY_DATABASE_URL)

app.include_router(router, prefix="/user", tags=["user"])
app.include_router(router1, prefix="/auth", tags=["auth"])
app.include_router(router2, prefix="/company", tags=["company"])
app.include_router(router3, prefix="/invite", tags=["invite"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,  # Add CORSMiddleware from BE-3*
    allow_headers=["*"],
    allow_methods=["*"],
)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
def root():
    return {"status": "Working"}
