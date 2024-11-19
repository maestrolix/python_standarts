# Сервисы

**Описываемый файл**: [entities.py](../../../../../components/backend/demo_project/application/entities.py)


---

## **Предисловие**
* Сервисы выполняют основную бизнес-логику (расчеты, обработка данных и ТД.)

# TODO Используются такие-то библы

---
<br>

* Пример сервиса.
```python
from demo_project.application import interfaces
from demo_project.application.dto import UserCreateReq
from demo_project.application.entities import User
from demo_project.application.utils import hash_password
from ssd_libs.components import component


@component
class UserService:
    user_repo: interfaces.UserRepo

    def create_user(self, user: UserCreateReq):
        user_dc = User(**user.dict())

        is_exists = self.user_repo.get_by_login(user_dc.login)
        if is_exists is not None:
            raise

        user_dc.password = hash_password(user_dc.password)
        self.user_repo.add_object(user_dc)
        return {'msg': 'success'}
```


--- 


**Правила**
1. Адаптер в сервисе должен аннотироваться с помощью [интерфейса](interfaces.md).
2. В названии должен присутствовать постфикс `Service`


---

## Полезные ссылки
