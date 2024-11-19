# Стандарты отдела python

Данный репозиторий создан для стандартизации разработки на python. 

Мы старались не переписывать документацию библиотек, которые мы используем на проектах, поэтому объяснения в основном по нашей архитектуре, корпаративным библиотекам и стилю написания кода.

Каждый пользователь может внести предложения к доработкам и улучшению стандартов при помощи ПР.

**Какие изменения можно предложить?**
- Добавление крутых ссылок по одному из разделов, которые помогут разработчикам лучше понимать инструмент
- Исправление грамматических ошибок (надеюсь правильно написал)
- Предложение по более чёткому и понятному объяснению работы того или иного инструмента
- Исправление опечаток
- Предложение правил описания кода, которые изначально забыли добавить
- Добавление более подробного описания того или иного раздела


**Почему мы выбрали подход описания стандартов в рамках репозитория?**
- Возможность быстрого доступа к файлу, в котором применяется тот или иной инструмент
- Возможность сопровождения документации читаемыми вставками кода
- Возможность генерации статического сайта с документацией на основе MD файлов
- Возможность коллективного развития стандартов python посредством ПР, которые могут комментировать все разработчики отдела
- Независимость документации от сторонних сервисов, которые не имеют открытого кода, а также повышенная мобильность за счёт описания в формате MD



---
---

## [Components](./docs/components/)
Директория содержит модули приложения, как правило, это бэкенд и фронтэнд. 
Всё зависит от того, сколько модулей пишется в одном репозитории

---

## [Deployment](./docs/deployment/)
Директория содержит всю информацию по развёртыванию приложения на серверах. В COMPONENTS не должно содержаться никакой информации, которая относится к деплою, чтобы 
- Не засорять глаз лишней информации во время разработки
- Удобство при настройке деплоя
- При ревью кодовой базы будет сложно просмотреть изменения в деплое проекта

---

## [Docs](./docs/docs/)
Вся документация проекта.
- Gitflow
- Взаимодействие внутренних сервисов приложения
- Стратегия авторизации
- Нетепичные архитектурные решения
- Общая идея приложения
- Работа приложения в рамках общей инфраструктуры
- И любые другие моменты, которые хочется зафиксировать в публичном месте 


### Содержание
Документация практически полностью подражает устройству файлов в проекте для интуитивно понятной навигации



* **Перечень приложений**
    * [Бэкенд проект](./docs/components/backend/basic.md)
        * **Основная кодовая база приложения**
            * [Адаптерная логика](./docs/components/backend/project/adapters/basic.md)
                * **База данных**
                    * [Настройка миграций](./docs/components/backend/project/adapters/database/alembic.md)
                    * [Маппинг таблиц БД с сущностями](./docs/components/backend/project/adapters/database/mapping.md)
                    * [Репозитории](./docs/components/backend/project/adapters/database/repositories.md)
                    * [Таблицы БД](./docs/components/backend/project/adapters/database/tables.md)
                * **Рассылка сообщений на почту**
                    * [Отправка сообщений](./docs/components/backend/project/adapters/email_sender/sender.md)
                    * [Сериализация сообщений](./docs/components/backend/project/adapters/email_sender/serializer.md)
                * **Формирование API**
                    * [Запуск HTTP сервера](./docs/components/backend/project/adapters/http_api/app.md)
                    * [Настройка работы с пользователем ролёвка/досутпы/группы/стратегия авторизации](./docs/components/backend/project/adapters/http_api/auth.md)
                    * [Контроллеры](./docs/components/backend/project/adapters/http_api/controllers.md)
                    * [Настройка spectree (авто документация API)](./docs/components/backend/project/adapters/http_api/spectree.md)
                * **Логи**
                * **Шина сообщений**
                    * [Маршрутизация потребителей очередей](./docs/components/backend/project/adapters/message_bus/consumers.md)
                    * [Создание очередей](./docs/components/backend/project/adapters/message_bus/scheme.md)
            * [Доменная логика](./docs/components/backend/project/application/basic.md)
                * [DTO](./docs/components/backend/project/application/dto.md)
                * [Бизнес сущности](./docs/components/backend/project/application/entities.md)
                * [Интерфейсы](./docs/components/backend/project/application/interfaces.md)
                * [Сервисы](./docs/components/backend/project/application/services.md)
                * [Утилиты](./docs/components/backend/project/application/utils.md)
            * [Запуски процессов](./docs/components/backend/project/composites/basic.md)
                * [Запуск миграций](./docs/components/backend/project/composites/alembic_runner.md)
                * [Запуск потребителя шины сообщений](./docs/components/backend/project/composites/consumer.md)
                * [Запуск HTTP сервера](./docs/components/backend/project/composites/http_api.md)
                * [Запуск планировщика задач](./docs/components/backend/project/composites/scheduler.md)
        * [Тесты](./docs/components/backend/tests/basic.md)
            * [Интеграционные тесты](./docs/components/backend/tests/integration.md)
            * [Модульные тесты](./docs/components/backend/tests/unit.md)
        * [Корпаративные библиотеки](./docs/components/backend/ssd_libs/basic.md)
            <!-- * TODO: реализовать после завершения описания библиотек и рефакторинга -->
* **Деплой приложений**
    * [Билд бэкенда](./docs/deployment/backend.md)
    * [Развёртывание контейнеров](./docs/deployment/backend.md)
* [Докуметация проекта](./docs/docs/base.md)