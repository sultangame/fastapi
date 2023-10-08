from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path().parent.parent


class Settings(BaseSettings):
    db_url: str = (f'sqlite + aisqlite://{BASE_DIR}/db.sqlite3')
    # db_echo: bool = False
    db_echo: bool = True


settings = Settings()
