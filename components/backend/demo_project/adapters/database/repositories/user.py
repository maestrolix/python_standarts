from sqlalchemy import delete, select, update

from ssd_libs.components import component
from ssd_libs.sql_storage import BaseRepository

from demo_project.application import interfaces
from demo_project.application.entities import User


@component
class UserRepo(BaseRepository, interfaces.IUserRepo):

    def get_by_login(self, login: str) -> User:
        query = select(User).where(User.login == login)
        return self.session.execute(query).scalar()

    def add_object(self, object: User) -> User:
        self.session.add(object)
        self.session.commit()
        return object
