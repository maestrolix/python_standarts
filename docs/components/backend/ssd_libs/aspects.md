# Библиотека aspects


## Описание
* При старте приложения, все методы, обернутые в декоратор `@join_point`
добавляются во внутренний список библиотеки, после чего, каждый добавленный метод можно обернуть декораторами, с помощью метода `join()`.



---
* Пример. Данный метод (контроллер) был сохранен в локальном хранилище библиотеки
```python
@join_point
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

* Далее, уже непосредственно в сборке приложения, происходит оборачивание другими декораторами, которые были прокинуты в метод `join(...)`. В данном примере, ко всем методам, обернутым декоратором `join_point`, будет применен контекстный менеджер, для корректного закрытия сессии, подтверждения транзакций и, в случае ошибки транзакции, её `rollback`.
* Так же, `join`, позволяет добавить ни один декоратор, а множество.
```python
class Aspects:
    application.join_points.join(DB.context)
    http_api.join_points.join(DB.context)
```

---
## Полезные ссылки
1. [Декораторы](https://pythonworld.ru/osnovy/dekoratory.html)