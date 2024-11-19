from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    SMTP_HOST: str
    SMTP_PASSWORD: str
    SMTP_SENDER: str
    SMTP_PORT: int

    LOGGING_LEVEL: str = 'INFO'

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'email_log': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
