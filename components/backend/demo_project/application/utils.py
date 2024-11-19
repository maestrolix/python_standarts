
from hashlib import sha256


def hash_password(password: str) -> str:
    """ Метод хеширующий парль с помощью SHA256. """
    hashed = sha256(password.encode('utf-8')).hexdigest()
    return hashed


def compare_passwords(raw, hashed) -> bool:
    """ Метод сравнивающий исходный пароль с его хешем. """
    return hash_password(raw) == hashed