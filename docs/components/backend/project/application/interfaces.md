# Интерфейсы

**Описываемый файл**: [interfaces/user.py](../../../../../components/backend/demo_project/application/interfaces/email.py)


---


## **Предисловие**
* Для каждого адаптера пишется свой интерфейс от которого последний, должен наследоваться и реализовать его.


---


* Пример
```python
from abc import abstractmethod
from typing import List

from ssd_libs.sql_storage.interfaces import IBaseRepository


class IEmailRepo(IBaseRepository):

    @abstractmethod
    def get_users_email(self) -> List[str]:
        """ Возвращает почты пользователей """

```

---


**Правила**
1. Так как, адаптер в сервисе мы аннотируем с помощью интерфейса, то комментарии 
к методам должны быть как в методах адаптеров, так и в интерфейсах
2. Интерфейс репозитория должен наследоваться от [IBaseRepository](../../../../../components/backend/ssd_libs/sql_storage/interface.py).
3. Остальные интерфейсы, должны наследоваться от `ABC`;
4. Имя интерфейса должно начинаться с большой английской буквы `I`. `I`
это первая буква от слова `interface`
1. Имя интерфейса для адаптера должно заканчиваться сокращением имени адаптера.
    - `Repo`sitories -> `I`User`Repo`
2. Все методы интерфейса должны быть обернуты декоратором `@abstractmethod`
3. Каждый метод адаптера должен быть описан в интерфейсе.


---
## Полезные ссылки

1. [ABC](https://habr.com/ru/articles/72757/)
