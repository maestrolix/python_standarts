from pydantic import BaseModel
from spectree import Tag

security_tag = Tag(name='Аутентификация', description='')


class UserAuthInfo(BaseModel):
    login: str
    password: str
