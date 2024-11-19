# Основное веб-приложение

**Описываемый файл**: [http_api.py](../../../../../components/backend/demo_project/composites/http_api.py)


---


* Необходимые импорты для работы основного веб-приложения.
```python
from kombu import Connection
from sqlalchemy import create_engine

from demo_project.adapters.http_api.app import create_app
from demo_project import application
from demo_project.adapters import database, http_api, log, message_bus, settings
from demo_project.adapters.database import repositories
from demo_project.application import services
from ssd_libs.messaging_kombu import KombuPublisher
from ssd_libs.sql_storage import TransactionContext
```


* Данный класс, является хранилещем, настроек адаптера\адаптеров. В данном классе присутствуют такие настройки как:
    - http_api -> Настройки сваггера, и настройки формата логирования;
    - common_settings -> Общие настройки для веб-приложения;
    - log -> Настройки для логирования;
    - message_bus -> Непосредственно настройки адаптера для работы с очередями
    - db -> Настройки для работы с БД.
```python
class Settings:
    db = database.Settings()
    http_api = http_api.Settings()
    common_settings = settings.Settings()
    log = log.Settings()
    message_bus = message_bus.Settings()
```


* Данный класс, отвечает за конфигурацию логирования.
```python
class Logger:
    log.configure(
        Settings.http_api.LOGGING_CONFIG,
        Settings.db.LOGGING_CONFIG,
    )
```


* Данный класс, отвечает за:
    - создание объекта подключения к RabbitMQ;
    - создание отправителя(publisher), для отправки сообщения в RabbitMQ;
```python
class MessageBus:
    try:
        connection = Connection(Settings.message_bus.RABBITMQ_URL)
        message_bus.email_broker_scheme.declare(connection)
        publisher = KombuPublisher(
            connection=connection, scheme=message_bus.email_broker_scheme
        )
    except:
        publisher = None
```


* Данный класс, существуеют для прокидывания объектов сессий в объекты [репозитория](../adapters/database/repositories.md). Происходит создание объекта enige для последующей работы с сессиями БД. В каждый репозиторий, который общается с БД должен быть прокинут context.
```python
class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)

    library_repo = repositories.LibraryRepo(context=context)
    user_repo = repositories.UserRepo(context=context)
```


* Данный класс, существует для создания объектов сервисов, в который прокидываются созданные в классе DB объекты репозиториев.
```python
class Application:
    library_service = services.LibraryService(
        library_repo=DB.library_repo, publisher=MessageBus.publisher
    )
    user_service = services.UserService(user_repo=DB.user_repo)
    security_service = services.SecurityService(user_repo=DB.user_repo)
```


* Данный класс, предназначен для настройки декораторов, которые работают с сессиями БД.
```python
class Aspects:
    application.join_points.join(DB.context)
    http_api.join_points.join(DB.context)
```

* Здесь создается основной объект веб приложения. В данный метод, прокидываются настройки, такие как:
    - is_dev_mode -> Запущено ли приложение в режиме разработчика
    - swagger_settings -> Настройки для сваггера(автодокументация API)
    - *_service -> Сервисы для последующего прокидывания их в методе в объекты контроллеров.
```python
app = create_app(
    is_dev_mode=Settings.common_settings.IS_DEV_MODE,
    swagger_settings=Settings.http_api.SWAGGER,
    allow_origins=Settings.http_api.ALLOW_ORIGINS,
    library_service=Application.library_service,
    user_service=Application.user_service,
    security_service=Application.security_service
)
```

* Запускается с помощью команды

**Через точку указывается путь к файлу, относительно текущей директории**

```python -m demo_project.composites.consumer```

## Полезные ссылки
1. [falcon](https://falcon.readthedocs.io/en/stable/user/quickstart.html)
2. [spectree](https://spectree.readthedocs.io/en/latest/)