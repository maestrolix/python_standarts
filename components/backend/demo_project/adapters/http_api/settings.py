from typing import List, Tuple, Union

from pydantic import BaseSettings, Field


class SwaggerSettings(BaseSettings):
    ON: bool = False
    TITLE: str = 'DemoProject'
    PATH: str = 'apidoc'
    FILENAME: str = 'openapi.json'
    SERVERS: List[Tuple[str, str]] = Field(default_factory=list)

    class Config:
        env_file = '.env'
        env_prefix = 'SWAGGER_'
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    SWAGGER: SwaggerSettings = Field(default_factory=SwaggerSettings)
    ALLOW_ORIGINS: Union[str, Tuple[str, ...]] = Field(default_factory=tuple)
    LOGGING_LEVEL: str = 'INFO'

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'gunicorn': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }
