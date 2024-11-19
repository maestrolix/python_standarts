# Репозитории

**Описываемый файл**: [repositories/user.py](../../../../../../components/backend/demo_project/adapters/database/repositories/user.py)


---
## **Предисловие**
* Цель репозитория - это общения с "нашей" БД. В репозиториях не должна содержаться какая-либо логика, кроме запросов к БД. Любая бизнес-логика происходит в applications.


---
## **Описание**

* Импорт небходимого. 
```python
#Для создания запросов
from sqlalchemy import delete, select, update   

# Интерфейсы для наследования
from demo_project.application import interfaces 
# Импорт сущности, для работы с таблицей БД, так же для аннотации кода.
from demo_project.application.entities import User  
# Создание датакласса из класса
from ssd_libs.components import component 
# Базовый репозиторий для наследования     
from ssd_libs.sql_storage import BaseRepository 
```

* Пример класса репозитория.
```python
@component
class UserRepo(BaseRepository, interfaces.UserRepo):

    def get_by_login(self, login: str) -> User:
        query = select(User).where(User.login == login)
        return self.session.execute(query).scalar()

    def add_object(self, object) -> object:
        self.session.add(object)
        self.session.commit()
        return object
```

# **Правила**

* Незабывайте накинуть декоратор [@component](../../../ssd_libs/components.md) на класс.
* Первым от чего должен наследоваться данный класс это - [BaseRepository](../../../ssd_libs/sql_storage.md)
* Не забывайте АННОТИРОВАТЬ то, что вы принимаете и то, что вы возвращаете.
* В некоторых случаях, нужно вручную прописать `self.session.commit()`, так как, 
данные сохраняются только в конце всей работы с ними.

---


## Полезные ссылки
1. [Примеры запросов ORM](https://ploshadka.net/sqlalchemy-primery-zaprosov-orm/)
2. [SELECT if else](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.case)