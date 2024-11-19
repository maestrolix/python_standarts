from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    RABBITMQ_PORT: int = 5672
    RABBITMQ_HOST: str = Field('localhost', env='rabbitmq_host')
    RABBITMQ_USER: str = Field('guest', env='rabbitmq_user')
    RABBITMQ_PASS: str = Field('guest', env='rabbitmq_password')

    LOGGING_LEVEL: str = 'INFO'

    @property
    def RABBITMQ_URL(self):
        url = 'amqp://{user}:{password}@{host}:{port}/'

        return url.format(
            user=self.RABBITMQ_USER,
            password=self.RABBITMQ_PASS,
            host=self.RABBITMQ_HOST,
            port=self.RABBITMQ_PORT,
        )

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'kombu': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False,
                }
            }
        }

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
