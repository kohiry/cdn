from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    P_DB: str
    P_USER: str
    P_PASS: str
    DATABASE_URL: str
    TOKEN: str

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
