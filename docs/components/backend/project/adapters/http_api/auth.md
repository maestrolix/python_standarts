# Настройки прав пользователей

**Описываемый файл**: [auth.py](../../../../../../components/backend/demo_project/adapters/http_api/auth.py)

---
## **Предисловие**
* В данном документе, будет предоставлено описание 
авторизации\аутентификации по jwt токену. Присутствует так же и 
другие способы, но они будут описаны позднее.
---
<br>


* Для аутентификации и авторизации используется своя 
библиотека [http_auth](../../../ssd_libs/http_auth.md)
```python
from falcon import Request

from ssd_libs.http_auth import Group, Permission, strategies
```


* Здесь описываются всевомзожные доступы, которые
вы можете предоставить разным группам пользователей
```python
class Permissions:
    FULL_CONTROL = Permission('full_control')
    READ_CONTROL = Permission('read_control')
```


* В данном классе, описываются названия групп и их 
доступы(права)
```python
class Groups:
    ADMINS = Group('Admin', permissions=(Permissions.FULL_CONTROL, ))
    USERS = Group('All', permissions=(Permissions.READ_CONTROL, ))

```

 
* Настройка токена.
```python
secret_key = 'KFjldjf2341klfjs'
decoding_options = {'verify_exp': 'verify_signature', 'require': ['exp']}

# Создание объекта стратегии. это важный момент
jwt_strategy = strategies.JWT(secret_key=secret_key, decoding_options=decoding_options)
```

* Константа для удобства использования
```python
ALL_GROUPS = (
    Groups.ADMINS,
    Groups.USERS,
)
```

---
## Полезные ссылки
1. [JWT TOKEN](https://ru.wikipedia.org/wiki/JSON_Web_Token)