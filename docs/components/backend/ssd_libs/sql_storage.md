# Библиотека sql_storage


## Предисловие
* Данная библиотека занимается тем, что:
1. Корректно создает и закрывает `сессию` для работы с БД (Один поток, одна сессия)
2. Данная библиотека потокобезопасная.
3. В случае ошибки в транзакции происходит rollback.
4. Производит подсчет вызовов, чтобы сессия не закрылась раньше, чем нужно.
5. Работает как контекстный менеджер. То есть может быть вызван через декоратор или with.


## Примеры использования
* При старте приложения, мы прокидываем наш контекст в join_points ([http_api](../project/composites/http_api.md)).
```python
class Aspects:
    application.join_points.join(DB.context)
    http_api.join_points.join(DB.context)
```

* Далее в [controllers](../project/adapters/http_api/controllers.md) мы оборачиваем контроллер декоратором join_point,
таким образом на время жизни запроса, будет создана сессия (в момент первого обращения к БД) и после окончания запроса, происходит `commit` транзакций или
`rollback`.
```python
@join_point #ТУТА
@spectree.validate(
    json=UserCreateReq,
    resp=RespValidate(HTTP_200=UserCreateResp),
    tags=(user_tag, )
)
def on_post_create_user(self, req: Request, resp: Response):
    """ Создание юзера """
    result = self.user_service.create_user(req.context.json)
    resp.media = result
```


---
## **BaseRepository**

* [BaseRepository](../../../../components/backend/ssd_libs/sql_storage/repository.py) предоставляет некоторый базовый функционал, помимо выдачи сессии, который позволяет не писать стандартные методы добавления, удаления, выборки и обновления записей в БД.
---
## Полезные ссылки
1. [contextlib](https://docs.python.org/3/library/contextlib.html)
2. [sessionmaker](https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker)
3. [threads](https://docs.python.org/3/library/threading.html)
