## Используем Python 3.10

## Какие пакеты применяем для разработки:
- [falcon](https://falcon.readthedocs.io/en/stable/index.html)
- [pydantic](https://docs.pydantic.dev/latest/)
- [sqlalchemy](https://docs.sqlalchemy.org/en/20/)
- [alembic](https://alembic.sqlalchemy.org/en/latest/)
- [psycopg2](https://www.psycopg.org/docs/)
- [kombu](https://docs.celeryq.dev/projects/kombu/en/stable/index.html)
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- [requests](https://requests.readthedocs.io/en/latest/index.html)
- [pytest](https://docs.pytest.org/_/downloads/en/stable/pdf/)
- [isort](https://pycqa.github.io/isort/)
- [flake8](https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html#flake8)
- [toml](https://pypi.org/project/toml/)
- [gunicorn](https://docs.gunicorn.org/en/stable/)
- [spectree](https://spectree.readthedocs.io/en/latest/)
- [mypy](https://mypy.readthedocs.io/en/stable/)

## Общая информация об архитектуре
* Наши проекты придерживаются гексагональной архитектуры. Думаю нет смысла дублировать информацию, 
которая прекрасно описана в статьях приложенных в полезных ссылках.

----

## Основные преимущества:
- Компоненты изолированы и независимы друг от друга напрямую. Вместо этого они связаны посредством абстракций.
- Каждый компонент работает в чётких рамках и решает лишь одну задачу.
- "Dependency injection" разрешает все проблемы для unit тестирования любых компонентов проекта на любом уровне.
Это позволяет сделать подход TDD очень даже экономным и удобным.
- С учётом того, что зависимости описываются абстракциями, можно безболезненно заменить один компонент другим.
Замена ORM, библиотеки для миграций или фреймворка становится простой задачей не требующий больших усилий.
- Простота в разбиении монолита на микросервисы. Если иметь под рукой схему во взаимодействию компонентов, 
то все микросервисы можно выделить в течение 5 минут.
- Повышенная читаемость и внедрения новых разработчиков в проекты
- Реализация принципов SOLID
- Простота изменения бизнес-правил, так как все они собраны в одном месте, 
не размазаны по проекту и не перемешаны с низкоуровневым кодом.
- Независимость от внешних агентов: наличие абстракций между бизнес-логикой и внешним миром в определенных случаях позволяет менять внешние источники, 
не затрагивая внутренние слои. Работает, если вы не завязали бизнес-логику на специфические особенности внешних агентов, например, транзакции БД.

----

## Полезные ссылки
1. [DDD в python c примером реализации](https://habr.com/ru/articles/559560/)
2. [Чистая архитектура в python](https://habr.com/ru/companies/exness/articles/494370/)
3. [Что можно узнать о Domain Driven Design за 10 минут?](https://habr.com/ru/companies/dododev/articles/489352/)
4. [S.O.L.I.D.](https://teletype.in/@loginovpavel/solid-in-python)