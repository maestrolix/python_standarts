# Библиотека scheduler

`#TODO пример динамического планировщика`

**Базовый класс**: [scheduler.py](../../../../components/backend/ssd_libs/scheduler/scheduler.py)


## Описание
* Данная библиотека при помощи синтаксиса крона, способна запускать
задачи в фоне.


---
## Scheduler_wrapper (обёртка) 

**Описываемый файл**: [scheduler.py](../../../../components/backend/ssd_libs/scheduler/scheduler_wrapper.py)


* В основном, функционал базового класса не используется. Используется упрощенная обертка над ним.
  - Имеется возможность отключения.
  - Перезапуск задач. 
  - Запуск задач.


<br>

* Пример наполнения задачи для планировщика. [library_event.py](../../../../components/backend/demo_project/application/services/library_event.py)
```python
task = Task(
    name='reminder',
    cron_schedule='* * * * *',
    job=self.__publish_message, # Ссылка на метод
    job_kwargs={                # Аргументы
        'msg': msg,
        'queue_name': 'MailEvent'
    }
)
```

* Непосредственно запуск планировщика. [scheduler.py](../../../../components/backend/demo_project/composites/scheduler.py)
```python
class Tasks:
    task = Application.library_event_service.get_reminder_task()
    scheduler = Scheduler(task)
    scheduler.run()
```
---

## Полезные ссылки
1. [threads](https://docs.python.org/3/library/threading.html)
2. [croniter](https://pypi.org/project/croniter/)