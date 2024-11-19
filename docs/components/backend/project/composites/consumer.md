# Работа с брокером очередей.


**Описываемый файл**: [consumer.py](../../../../../components/backend/demo_project/composites/consumer.py)

---

* Необходимые импорты для работы с очередью и сервисов. 
```python
from kombu import Connection
from sqlalchemy import create_engine

from demo_project.application import services
from demo_project.adapters.database import repositories
from ssd_libs.sql_storage import TransactionContext
from demo_project.adapters import database, email_sender, log, message_bus
```

* Данный класс, является хранилещем, настроек адаптера\адаптеров. В данном классе присутствуют такие настройки как:
    - message_bus -> Непосредственно настройки адаптера для работы с очередями;
    - email -> Настройки адаптера, который должен рассылать опопвещения о магазине "Книжечка";
    - db -> Настройки для работы с БД.
```python
class Settings:
    message_bus = message_bus.Settings()
    email = email_sender.Settings()
    db = database.Settings()
```


* Данный класс, отвечает за конфигурацию логирования.
```python
class Logger:
    log.configure(Settings.message_bus.LOGGING_CONFIG, Settings.email.LOGGING_CONFIG)
```


* Данный класс, существуеют для прокидывания объектов сессий в объекты [репозитория](../adapters/database/repositories.md). Происходит создание объекта enige для последующей работы с сессиями БД. В каждый репозиторий, который общается с БД должен быть прокинут context.
```python
class DB:
    engine = create_engine(Settings.db.DATABASE_URL)
    context = TransactionContext(bind=engine)
    email_repo = repositories.EmailRepo(context=context)
```


* Данный класс, существует для создания объектов [сервисов](../application/services.md), в который прокидываются созданные в классе **DB** объекты репозиториев.
```python
class Application:
    email_service = services.EmailService(email_repo=DB.email_repo)
```


* Данный класс, отвечает за настройку [адаптера](../adapters/email_sender/sender.md), который занимается рассылкой сообщений.
```python
class Email:
    sender = email_sender.BookMainSender(
        smtp_sender=Settings.email.SMTP_SENDER,
        smtp_password=Settings.email.SMTP_PASSWORD,
        smtp_host=Settings.email.SMTP_HOST,
        smtp_port=Settings.email.SMTP_PORT,
        email_service=Application.email_service
    )
```


* Данный класс, отвечает за:
    - создание объекта подключения к RabbitMQ;
    - создание объекта потребителя([consumer](../adapters/message_bus/consumers.md)), который занимается тем, что получает от RabbitMQ сообщения;
    - Отправкой данных в метод сервиса, который был ему прокинут.
```python
class MessageBus:
    connection = Connection(Settings.message_bus.RABBITMQ_URL)
    consumer = message_bus.create_email_consumer(
        connection=connection, sender=Email.sender
    )

    @staticmethod
    def declare_scheme():
        message_bus.email_broker_scheme.declare(MessageBus.connection)
```


* Данный файл, запускается как python-модуль, поэтому используется данный синтаксис.
```python
if __name__ == '__main__':
    MessageBus.declare_scheme()
    MessageBus.consumer.run()
```

Например:

**Через точку указывается путь к файлу, относительно текущей директории**

```python -m demo_project.composites.consumer```

## Полезные ссылки
1. [Для общенго понимания](https://habr.com/ru/articles/434510/)
2. [Библиотека, которая используется на проекте](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html)
3. [Документация RabbitMQ](https://www.rabbitmq.com/documentation.html)