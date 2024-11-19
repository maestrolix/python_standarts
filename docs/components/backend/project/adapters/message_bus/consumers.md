# Консюмер


```#TODO Ссылки на наши либы```

**Описываемый файл**: [consumers.py](../../../../../../components/backend/demo_project/adapters/message_bus/consumers.py)


---

* Здесь создаются консьюмеры. Указывается из какой очереди взять
сообщение и на какой метод отправить данные для последующей работы.
```python
from kombu import Connection

from ssd_libs.messaging_kombu import KombuConsumer

from .scheme import email_broker_scheme
from demo_project.adapters import email_sender


def create_email_consumer(
    connection: Connection, sender: email_sender.BookMainSender
) -> KombuConsumer:
    consumer = KombuConsumer(connection=connection, scheme=email_broker_scheme)

    consumer.register_function(sender.send_event, 'SendMailEvent')
    return consumer

```


---

## Полезные ссылки

1. [Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/introduction.html)
2. [RabbitMQ](https://www.rabbitmq.com/documentation.html)