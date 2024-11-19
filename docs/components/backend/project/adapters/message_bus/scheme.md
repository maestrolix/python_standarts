# Схемы

```#TODO Ссылки на наши либы```

**Описываемый файл**: [scheme.py](../../../../../../components/backend/demo_project/adapters/message_bus/scheme.py)

## 

---

* Здесь создаются очереди в RabbitMQ.
```python
from kombu import Exchange, Queue

from ssd_libs.messaging_kombu import BrokerScheme

email_broker_scheme = BrokerScheme(
    Queue('SendMailEvent', Exchange('MailEvent')), 
)

```

---

## Полезные ссылки

1. [Kombu](https://docs.celeryq.dev/projects/kombu/en/stable/introduction.html)
2. [RabbitMQ](https://www.rabbitmq.com/documentation.html)