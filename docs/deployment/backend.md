# Настройка бэкенда для запуска

**Описываемые файлы**: 
- [Dockerfile](../../deployment/backend/Dockerfile)
- [entrypoint_api.sh](../../deployment/backend/entrypoint_api.sh)
- [entrypoint_await.sh](../../deployment/backend/entrypoint_await.sh)
- [entrypoint_consumer.sh](../../deployment/backend/entrypoint_consumer.sh)
- [entrypoint_migrations.sh](../../deployment/backend/entrypoint_migrations.sh)

---

## **Предисловие**
* Для каждого раздела [components](../../components) создаётся отдельная директория в 
[deployment](../../deployment). В данном документе возьмём за пример [backend](../../deployment/backend) 

---
### [Dockerfile](../../deployment/backend/Dockerfile)
В рамках данного файла описывается билд приложения
```dockerfile
# Указываем используемый образ
FROM python:3.10.7 as standart-api

# Устанавливаем пеменной окружения "USERNAME" значение "app"
ENV USERNAME=app

# Установка недостающих зависимостей
RUN apt update \
    && apt install -y unixodbc-dev \
    && rm -fr /etc/apt/auth.conf.d/reg.conf \
    && apt install -y netcat

# Копируем кодовую базу бэкенда в директорию контейнера /app/
COPY ./components/backend/ /app/

# Устанавливаем директорию /app/ внутри контейнера "рабочей" для исполнение терминальных команд в ней
WORKDIR /app

# Обновление pip
RUN pip install --upgrade pip

# Копируем файл хранящий все зависимости
COPY ./components/backend/requirements.txt /usr/src/app/requirements.txt

# Устанавливаем все зависимости проекта
RUN pip install -r requirements.txt

RUN groupadd -r $USERNAME &&\
    useradd -r -g $USERNAME -d /home/$USERNAME -s /sbin/nologin -c "Docker image user" app

# Копируем команды запуска процессов в bin с передачей прав владения пользователю "app"
COPY --chown=app:app ./deployment/backend/entrypoint_*.sh /usr/local/bin/

# Повышаем права доступа для использования наших команд
RUN chmod +x /usr/local/bin/entrypoint_*.sh

FROM standart-api as final
```
---

### [entrypoint_api.sh](../../deployment/backend/entrypoint_api.sh)

```shell
#!/usr/bin/env bash
set -e
# Проверка наличия переменной окружения "$API_LOG_LEVEL", 
# которая отвечает за уровень логирования приложения (опционально = info)
if [ -z "$API_LOG_LEVEL" ]; then
  API_LOG_LEVEL=info
fi
# Проверка наличия переменной окружения "$API_PORT", 
# которая отвечает за запускаемого приложения (опционально = 5002)
if [ -z "$API_PORT" ]; then
  API_PORT=5002
fi
# Формирование аргументов gunicorn
GUNICORN_CMD_ARGS="--bind=0.0.0.0:${API_PORT}"
export GUNICORN_CMD_ARGS

# Запуск скрипта для ожидания готовности БД
entrypoint_await.sh
# Запуск скрипта для накатывания миграций БД
entrypoint_migrations.sh

# Запуск сервера
gunicorn demo_project.composites.http_api:app
```

---

### [entrypoint_await.sh](../../deployment/backend/entrypoint_await.sh)

```shell
#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    
    # Запуск бесконечного цикла пока не получится пингануть БД
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
    sleep 10
fi

exec "$@"
```

---

### [entrypoint_consumer.sh](../../deployment/backend/entrypoint_consumer.sh)

```shell
#!/usr/bin/env bash

# Запуск потребителя информации брокера сообщений
python -m demo_project.composites.consumer
```


---

### [entrypoint_migrations.sh](../../deployment/backend/entrypoint_migrations.sh)

```shell
#!/usr/bin/env bash

# Запуск миграций
python -m demo_project.composites.alembic_runner upgrade head
```

---


## Полезные ссылки
1. [Docker build оф.док.](https://docs.docker.com/engine/reference/builder/)
2. [Shell if else](https://www.digitalocean.com/community/tutorials/if-else-in-shell-scripts)
3. [Shell работа с переменными окружения](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux-ru)
4. [Linux команда nc](https://losst.pro/komanda-nc-v-linux)
5. [Linux работа chmod](https://losst.pro/komanda-chmod-linux)
6. [Linux работа chown](https://losst.pro/komanda-chown-linux)
