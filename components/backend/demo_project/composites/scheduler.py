from kombu import Connection
from sqlalchemy import create_engine

from ssd_libs.messaging_kombu import KombuPublisher
from ssd_libs.scheduler import Scheduler
from ssd_libs.sql_storage import TransactionContext

from demo_project.adapters import database, log, message_bus, settings
from demo_project.adapters.database import repositories
from demo_project.application import services


class Settings:
    db = database.Settings()
    common_settings = settings.Settings()
    log = log.Settings()
    message_bus = message_bus.Settings()


class MessageBus:
    try:
        connection = Connection(Settings.message_bus.RABBITMQ_URL)
        message_bus.email_broker_scheme.declare(connection)
        publisher = KombuPublisher(
            connection=connection,
            scheme=message_bus.email_broker_scheme
        )
    except:
        publisher = None


class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)
    library_event_repo = repositories.LibraryEventRepo(context=context)


class Application:
    library_event_service = services.LibraryEventService(
        library_event_repo=DB.library_event_repo, publisher=MessageBus.publisher
    )


class Tasks:
    task = Application.library_event_service.get_reminder_task()
    scheduler = Scheduler(task)
    scheduler.run()
