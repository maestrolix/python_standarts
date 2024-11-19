# Сборка основного приложения

**Описываемый файл**: [app.py](../../../../../../components/backend/demo_project/adapters/http_api/app.py)

---

## **Предисловие**
* В данном файле происходит сборка основного приложения. Здесь происходит прокидывание сервисов в контроллеры, некоторые общие настройки для приложения.


---
* Импорт всего необходимого для сборки приложения.
```python
from functools import partial
from typing import Tuple, Union

import falcon
import rapidjson
from falcon import media

# Импорт всех контроллеров для последующей регистрации
# Импорт объектов для авторизации и аутентификации
from demo_project.adapters.http_api import auth, controllers 
# Настройки сваггера
from demo_project.adapters.http_api.settings import SwaggerSettings 

# Метод для настройки сваггера.
from demo_project.adapters.http_api.spectree import setup_spectree  
# Сервисы для прокидывания их в контроллеры
from demo_project.application import services  
# Класс основго приложени                     
from ssd_libs.http_api import App                                   

# Кастомная библиотека для аутентификации и авторизации
from ssd_libs.http_auth import Authenticator
```


* В данный метод, прокидываются объекты [сервисов](../../../../../components/backend/project/application/services.md).
```python
def create_app(
    is_dev_mode: bool, 
    swagger_settings: SwaggerSettings,
    allow_origins: Union[str, Tuple[str,...]], 
    library_service: services.LibraryService,
    user_service: services.UserService, 
    security_service: services.SecurityService
) -> App:
```
**Примечание**
* Не забывайте прописать здесь сервис, который Вы разработали, для
его последующего прокидывания в контроллер.

<br>

* Тело метода. В нём приведены комментарии, за что отвечает
каждая часть.
```python
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    
    # В зависимости от флага, выставляются разрешенные источники
    # для мидлваре
    if is_dev_mode:
        cors_middleware = falcon.CORSMiddleware(
            allow_origins='*'
        )
    else:
        cors_middleware = falcon.CORSMiddleware(
            allow_origins=allow_origins
        )

    middleware = [cors_middleware]
    app = App(middleware=middleware, prefix='/api')

    # В данном приложении используется аутентификация по
    # токену, который формируется на стороне приложения и
    # возврощается фронту.
    authenticator.set_strategies(auth.jwt_strategy)

    # Непосредственно, регистрация контроллера, после чего
    # появляется возможность отправлять запросы.
    app.register(
        controllers.Library(
            authenticator=authenticator, 
            library_service=library_service
        )
    )
    
    # некоторые app.register были опущены...
    ...

    # В зависимости от флага, выставляются настройки для сваггера.    
    # То есть, сваггер можно отключить.
    if swagger_settings.ON:
        setup_spectree(
            app=app,
            title=swagger_settings.TITLE,
            path=swagger_settings.PATH,
            filename=swagger_settings.FILENAME,
            servers=swagger_settings.SERVERS,
        )

    # Наработка, в которой всей сериализацией данных занимается
    # библиотека rapid_json. Она более быстрая и решает некоторые проблемы
    # с сериализацией.
    json_handler = media.JSONHandler(
        dumps=partial(
            rapidjson.dumps,
            default=str,
        ),
        loads=rapidjson.loads,
    )
    extra_handlers = {
        'application/json': json_handler,
    }

    # Применение изменений.
    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)

    return app
```
**Примечание**
* путь к конечным точкам (endpoints) формируется по имени класса [контроллера](../http_api/controllers.md)
в нижнем регистре через ```_```.


---


## Полезные ссылки
1. [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
2. [CORSMiddleware](https://falcon.readthedocs.io/en/stable/api/cors.html)
3. [rapidjosn](https://rapidjson.org/)
4. [spectree](https://spectree.readthedocs.io/en/latest/)
5. [Установка сериализатора](https://falcon.readthedocs.io/en/stable/api/media.html#replacing-the-default-handlers)
6. [Routing](https://falcon.readthedocs.io/en/stable/api/routing.html)