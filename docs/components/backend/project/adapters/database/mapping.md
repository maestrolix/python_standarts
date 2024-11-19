# Маппинг

**Описываемый файл**: [mapping.py](../../../../../../components/backend/demo_project/adapters/database/mapping.py)


---


* Импорт всех описываемых [таблиц](../../../../../../components/backend/demo_project/adapters/database/tables.py) и их 
[датаклассов](../../../../../../components/backend/demo_project/application/entities.py)
```python
from sqlalchemy.orm import registry

from demo_project.adapters.database import tables
from demo_project.application import entities
```


* "Маппинг" классов описания таблицы, с их аналогами датаклассов.
```python
mapper = registry()

mapper.map_imperatively(
    entities.User, tables.users #[датакласс], [объект класса таблицы]
)
mapper.map_imperatively(
    entities.Author, tables.authors
)
mapper.map_imperatively(
    entities.Book, tables.books
)
```

**ПРИМЕЧАНИЕ**

* Не забывайте добавить объект ```mapper``` в ```__init__.py```, иначе
запросы к БД не будут корректно отрабатывать

* Имена полей в [датаклассах](../../../../../../components/backend/demo_project/application/entities.py) и в [объектах таблиц](../../../../../../components/backend/demo_project/adapters/database/tables.py) должны быть
одинаковыми. 


---


## Полезные ссылки
1) [Императивный подход](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#imperative-mapping)
