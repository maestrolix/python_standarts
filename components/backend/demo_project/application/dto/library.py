from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field, validator
from spectree import Tag

library_tag = Tag(name='Информация по книжкам и авторам', description='КРУД')


class AuthorCreateReq(BaseModel):
    name: str = Field(description='Имя автора', title='Имя')
    surname: str = Field(description='Фамилия автора', title='Фамилия')
    middlename: str = Field(description='Отчество автора', title='Отчество')

    class Config:
        title = 'Поля для создания автора'


class AuthorCreateResp(BaseModel):
    id: int = Field(
        description='Идентификатор записи',
        title='ID',
    )
    name: str = Field(description='Имя автора', title='Имя')
    surname: str = Field(description='Фамилия автора', title='Фамилия')
    middlename: str = Field(description='Отчество автора', title='Отчество')
    created_at: datetime = Field(
        description='Дата создания записи (string)',
        title='Дата создания',
    )

    class Config:
        title = 'Созданный автор'


class BookCreateReq(BaseModel):
    title: str = Field(title='Название', description='Название книги')
    author_id: Optional[int] = Field(
        title='ID Автора', description='ID Автора книги', ge=1
    )

    class Config:
        title = 'Поля для создания книги'


class BookCreateResp(BaseModel):
    id: int = Field(
        description='Идентификатор записи',
        title='ID',
    )
    title: str = Field(title='Название', description='Название книги')
    created_at: datetime = Field(
        description='Дата создания записи (string)',
        title='Дата создания',
    )
    author_id: Optional[int] = Field(
        title='ID Автора',
        description='ID Автора книги',
    )

    class Config:
        title = 'Созданная книга'


class BookAllResp(BaseModel):
    __root__: Optional[List[BookCreateResp]] = None

    class Config:
        title = ''


class AuthorAllResp(BaseModel):
    __root__: Optional[List[AuthorCreateResp]] = None

    class Config:
        title = ''
