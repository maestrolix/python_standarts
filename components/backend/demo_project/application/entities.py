from datetime import datetime
from typing import Optional

from attr import dataclass


@dataclass
class User:
    id: Optional[int] = None
    login: str = None
    password: str = None
    email_address: str = None
    created_at: Optional[datetime] = None
    is_admin: bool = None


@dataclass
class Author:
    id: Optional[int] = None
    name: str = None
    surname: str = None
    middlename: str = None
    created_at: Optional[datetime] = None


@dataclass
class Book:
    id: Optional[int] = None
    title: str = None
    created_at: Optional[datetime] = None
    author_id: Optional[int] = None
