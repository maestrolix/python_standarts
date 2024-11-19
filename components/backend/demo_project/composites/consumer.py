from kombu import Connection
from sqlalchemy import create_engine

from ssd_libs.sql_storage import TransactionContext

from demo_project.adapters import database, email_sender, log, message_bus
from demo_project.adapters.database import repositories
from demo_project.application import services


class Settings:
    message_bus = message_bus.Settings()
    email = email_sender.Settings()
    db = database.Settings()


class Logger:
    log.configure(Settings.message_bus.LOGGING_CONFIG, Settings.email.LOGGING_CONFIG)


class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)
    email_repo = repositories.EmailRepo(context=context)


class Application:
    email_service = services.EmailService(email_repo=DB.email_repo)


class Email:
    sender = email_sender.BookMainSender(
        smtp_sender=Settings.email.SMTP_SENDER,
        smtp_password=Settings.email.SMTP_PASSWORD,
        smtp_host=Settings.email.SMTP_HOST,
        smtp_port=Settings.email.SMTP_PORT,
        email_service=Application.email_service
    )


class MessageBus:
    connection = Connection(Settings.message_bus.RABBITMQ_URL)
    consumer = message_bus.create_email_consumer(
        connection=connection, sender=Email.sender
    )

    @staticmethod
    def declare_scheme():
        message_bus.email_broker_scheme.declare(MessageBus.connection)


if __name__ == '__main__':
    MessageBus.declare_scheme()
    MessageBus.consumer.run()
