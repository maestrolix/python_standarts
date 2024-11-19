from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field, validator
from spectree import Tag

user_tag = Tag(name='Апи для взаимодействия с пользователями', description='')


class UserCreateReq(BaseModel):
    login: str
    password: str
    email_address: str

    class Config:
        title = ''


class UserCreateResp(BaseModel):
    msg: str


class UserHttpException(BaseModel):
    status: int
    title: str
    description: str