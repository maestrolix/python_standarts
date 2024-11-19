# Алембик

**Описываемый файл**: [alembic_runner.py](../../../../../components/backend/demo_project/composites/alembic_runner.py)

---

* Необходимые импорты для работы [алембика](../adapters/database/alembic.md).
```python
import sys

from alembic.config import CommandLine, Config

from demo_project.adapters import database
```


* Данный класс, является хранилещем, настроек адаптера\адаптеров. В данном случае для работы алембика, нужны только настройки адептера базы данных.
```python
class Settings:
    db = database.Settings()
```


* Данная функция, настраивает конфигурацию для:
    - указания места хранения созданной миграции;
    - указания места конфигурационного файла для алебмика;
    - указания url для общения с БД;
    - указания некоторого шаблона, по которому алембик будет формировать 
    название файла;
    - указания времени, в данном случае UTC.
```python
def make_config():
    config = Config()
    config.set_main_option('script_location', Settings.db.ALEMBIC_SCRIPT_LOCATION)
    config.set_main_option('version_locations', Settings.db.ALEMBIC_VERSION_LOCATIONS)
    config.set_main_option('sqlalchemy.url', Settings.db.DATABASE_URL)
    config.set_main_option('file_template', Settings.db.ALEMBIC_MIGRATION_FILENAME_TEMPLATE)
    config.set_main_option('timezone', 'UTC')

    return config
```


* Данный метод, отвечает за парсинг переданных параметров через терминал,
Настройку алембика для создания\применения миграций и их последующий запуск.
```python
def run_cmd(*args):
    cli = CommandLine()
    cli.run_cmd(make_config(), cli.parser.parse_args(args))
```


* Данный файл, запускается как python-модуль. После чего параметры передаются в 
выше описанный метод.
```python
if __name__ == '__main__':
    run_cmd(*sys.argv[1:])
```
Например:

**Через точку указывается путь к файлу, относительно текущей директории**

```python -m demo_project.composites.alembic_runner revision --autogenerate -m 'actual_db'```

В метод run_cmd, попадет только та часть, с которой может работать alembic 

```revision --autogenerate -m 'actual_db'```


## Полезные ссылки
1. [Официальная документация](https://alembic.sqlalchemy.org/en/latest/index.html) 