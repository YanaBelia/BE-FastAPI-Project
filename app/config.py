import os
from dotenv import load_dotenv
from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname("../"))
load_dotenv(dotenv_path=f"{basedir}/.env")


class Settings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = r"C:\Users\Public\Documents\Kur_2019A\FastApi\.env"


settings = Settings()
