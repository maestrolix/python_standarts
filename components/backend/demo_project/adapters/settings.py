from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    IS_DEV_MODE: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'