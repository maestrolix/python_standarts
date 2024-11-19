# Развертывание проекта 


## 1. Установка зависимостей.

В директории /components/backend/, прописать следующие команды:

```
python3 -m venv .venv
source env/bin/activate
pip install -r requirements.txt
```


## 2. Создание окружения.

В директории /components/backend/, создать файл .env и записать
слеюущие строки:

```
DATABASE_NAME='demo_project_book'
DATABASE_HOST='localhost'
DATABASE_PORT=1337
DATABASE_USER='postgres'
DATABASE_PASS='postgres'

RABBITMQ_PORT=5672
RABBITMQ_HOST=localhost
RABBITMQ_USER=guest
RABBITMQ_PASSWORD=guest

SMTP_HOST='smtp.gmail.com'
SMTP_PASSWORD=''
SMTP_SENDER=''
SMTP_PORT=587

SWAGGER_ON=true
```

## 3. Работа с локальной БД в докере.

```
sudo docker-compose up -d
```

Минимальная настройка докер файла:

```
version: "3.3"
services:
  postgres-demo_project:
    image: postgres:12.3
    environment:
      POSTGRES_DB: "demo_project_book"
      POSTGRES_USER: "postgres"
      POSTGRES_PASSWORD: "postgres"
      PGDATA: "/var/lib/postgresql/data/pgdata"
    volumes:
      - .:/var/lib/postgresql/data
    ports:
      - "1337:5432"
```

## 4. Применение миграций к БД.

В директории /components/backend/, прописать следующую команду:
```
python -m demo_project.composites.alembic_runner upgrade head
```

## 5. Создание миграций (опционально).

В директории /components/backend/, прописать следующую команду:
```
python -m demo_project.composites.alembic_runner revision --autogenerate -m 'your_name'
```

## 6. Откат миграций (опционально).

В директории /components/backend/, прописать следующую команду:
```
python -m demo_project.composites.alembic_runner downgrade -[1-N]
```

## 7. Запуск http-сервера.

В директории /components/backend/, прописать следующую команду:
```
gunicorn demo_project.composites.http_api:app --bind=0.0.0.0:5002 --reload -t 300
```

## 8. Запуск остальных сервисов (опционально).

В директории /components/backend/, прописать следующую команду:
```
python3 -m demo_project.composites.scheduler
python3 -m demo_project.composites.consumer
```

# Тестирование проекта


## 1. Запуск тестов.

```
pytest tests/
```

Более подробный вывод информации о тестах.

```
pytest -vvv -s --disable-warnings
```


# Пре-комиты

## 1. Установка.
 
```
pre-commit install
```

## 2. Возможные ошибки

Ошибка:
```
ModuleNotFoundError: No module named 'virtualenv.seed.via_app_data'
```
Решение:
```
sudo apt remove --purge python3-virtualenv
```


# Линтеры

## 1. Flake8

Команда должна исполняться в директории, где находится pyproject.toml
```
flake8p demo_project/
```

## 2. isort

Команда должна исполняться в директории, где находится pyproject.toml
```
isort demo_project/
```

## 3. yapf
Пока не используется
