from kombu import Connection
from sqlalchemy import create_engine

from ssd_libs.messaging_kombu import KombuPublisher
from ssd_libs.sql_storage import TransactionContext

from demo_project import application
from demo_project.adapters import database, http_api, log, message_bus, settings
from demo_project.adapters.database import repositories
from demo_project.adapters.http_api.app import create_app
from demo_project.application import services


class Settings:
    db = database.Settings()
    http_api = http_api.Settings()
    common_settings = settings.Settings()
    log = log.Settings()
    message_bus = message_bus.Settings()


class Logger:
    log.configure(
        Settings.http_api.LOGGING_CONFIG,
        Settings.db.LOGGING_CONFIG,
    )


class MessageBus:
    try:
        connection = Connection(Settings.message_bus.RABBITMQ_URL)
        message_bus.email_broker_scheme.declare(connection)
        publisher = KombuPublisher(
            connection=connection, scheme=message_bus.email_broker_scheme
        )
    except ConnectionError:
        publisher = None


class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)

    library_repo = repositories.LibraryRepo(context=context)
    user_repo = repositories.UserRepo(context=context)


class Application:
    library_service = services.LibraryService(
        library_repo=DB.library_repo, publisher=MessageBus.publisher
    )
    user_service = services.UserService(user_repo=DB.user_repo)
    security_service = services.SecurityService(user_repo=DB.user_repo)


class Aspects:
    application.join_points.join(DB.context)
    http_api.join_points.join(DB.context)


app = create_app(
    is_dev_mode=Settings.common_settings.IS_DEV_MODE,
    swagger_settings=Settings.http_api.SWAGGER,
    allow_origins=Settings.http_api.ALLOW_ORIGINS,
    library_service=Application.library_service,
    user_service=Application.user_service,
    security_service=Application.security_service
)
