# Планировщик 

**Описываемый файл**: [scheduler.py](../../../../../components/backend/demo_project/composites/scheduler.py)

---

* Необходимые импорты для работы планировщика.
```python
from kombu import Connection
from sqlalchemy import create_engine

from demo_project.adapters import database, log, message_bus, settings
from demo_project.adapters.database import repositories
from demo_project.application import services
from ssd_libs.messaging_kombu import KombuPublisher
from ssd_libs.scheduler import Scheduler
from ssd_libs.sql_storage import TransactionContext
```


* Данный класс, является хранилещем, настроек адаптера\адаптеров. В данном классе присутствуют такие настройки как:
    - log -> Настройки вывода логов.
    - message_bus -> Настройки адаптера для работы с RabbitMQ;
    - db -> Настройки для работы с БД.
```python
class Settings:
    db = database.Settings()
    common_settings = settings.Settings()
    log = log.Settings()
    message_bus = message_bus.Settings()
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
            connection=connection,
            scheme=message_bus.email_broker_scheme
        )
    except:
        publisher = None
```


* Данный класс, существуеют для прокидывания объектов сессий в объекты [репозитория](../adapters/database/repositories.md). Происходит создание объекта enige для последующей работы с сессиями БД. В каждый репозиторий, который общается с БД должен быть прокинут context.
```python
class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)
    library_event_repo = repositories.LibraryEventRepo(context=context)
```


* Данный класс, существует для создания объектов [сервисов](../application/services.md), в который прокидываются созданные в классе DB объекты репозиториев.
```python
class Application:
    library_event_service = services.LibraryEventService(
        library_event_repo=DB.library_event_repo, publisher=MessageBus.publisher
    )
```

* В данном классе происходит создание объекта планировщика, прокидывание 
в него объектов задач и непосредственно запуск.
```python
class Tasks:
    task = Application.library_event_service.get_reminder_task()
    scheduler = Scheduler(task)
    scheduler.run()
```

* Запускается с помощью команды

**Через точку указывается путь к файлу, относительно текущей директории**

```python -m demo_project.composites.scheduler```

## Полезные ссылки
1. [удобный инструмент для формирования синтаксиса cron](https://crontab.guru/) 