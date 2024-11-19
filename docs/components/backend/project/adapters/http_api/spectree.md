# SpecTree

**Описываемый файл**: [spectree.py](../../../../../../components/backend/demo_project/adapters/http_api/spectree.py)


---
## **Предисловие**
* Spectree - библиотека для создания документа OpenAPI и проверки запроса и ответа с аннотациями Python. 


---


* Необходимые импорты.
```python
from typing import List, Tuple

from falcon import App
from spectree import SpecTree
from spectree.models import Server
```

* Начальная настройка объекта SpecTree.
```python
spectree = SpecTree(
    'falcon',               # Указание имени фреймфорка
    mode='strict',          # Собрать все маршруты, которые оформлены этим экземляром 
    annotations=True,       # Использование аннотации
    version='v0.1-alpha',   # Указание версии
)
```


* Метод настройки spectree. В целом, всё что здесь находится не 
нужно как-либо изменять.
```python
def setup_spectree(
    app: App,
    title: str,
    path: str,
    filename: str,
    servers: List[Tuple[str, str]],
):
    servers = [Server(url=url, description=description) for url, description in servers]

    # Конфигурация spectree
    spectree.config.title = title
    spectree.config.path = path
    spectree.config.filename = filename
    spectree.config.servers = servers

    spectree.register(app)
```

---
## Полезные ссылки
1. [spectree](https://spectree.readthedocs.io/en/latest/)