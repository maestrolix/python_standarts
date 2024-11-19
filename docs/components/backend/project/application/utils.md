# Инструменты

**Описываемый файл**: [utils.py](../../../../../components/backend/demo_project/application/utils.py)


---

## **Предисловие**
* В данном файле содержаться некоторые общие инструменты, которые используется
во многих участках кода.


---

* Пример двух методов, которые производят хеширование и сравнение паролей.
```python
from hashlib import sha256


def hash_password(password: str) -> str:
    """ Метод хеширующий парль с помощью SHA256. """
    hashed = sha256(password.encode('utf-8')).hexdigest()
    return hashed


def compare_passwords(raw, hashed) -> bool:
    """ Метод сравнивающий исходный пароль с его хешем. """
    return hash_password(raw) == hashed

```

**Правила**
1. Обязательные комментарии к методам
2. Аннотирование переменных.


---

## Полезные ссылки
