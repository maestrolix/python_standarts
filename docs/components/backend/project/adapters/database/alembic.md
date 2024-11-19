# Alembic (Конфигурация миграций)

**Описываемые файлы**
1. [env.py](../../../../../../components/backend/demo_project/adapters/database/alembic/env.py)
2. [script.py.mako](../../../../../../components/backend/demo_project/adapters/database/alembic/script.py.mako)


---


## **Предисловие**
* В данном разделе происходит настройка алембика, для создания миграций.


---
## env.py

* Импорт необходимого. Обратите внимание на комментарий.
```python
from alembic import context
from sqlalchemy import create_engine, pool

# Обратите внимание, что нужна метадата, которая была прокинута
# при создании объектов таблиц, по ней будет происходить поиск.
from demo_project.adapters.database.tables import metadata
```


* Проброс метадаты. Здесь присваивается метадата, которая была импортирована выше.
```python
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata
```

---
## script.py.mako
* Файл для указания шаблона того, как должна выглядеть миграция.
Это похоже на шаблонизатор jinja, где указывается, куда и что
нужно вставить.
```python
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
# Можете указать свои импорты для удобства.
from alembic import op          
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}

```

---


## Полезные ссылки
1) https://habr.com/ru/articles/585228/
2) https://alembic.sqlalchemy.org/en/latest/tutorial.html