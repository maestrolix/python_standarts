from abc import abstractmethod

from demo_project.application.entities import User
from ssd_libs.sql_storage.interface import IBaseRepository


class IUserRepo(IBaseRepository):

    @abstractmethod
    def get_by_login(self, login: str) -> User:
        """"""

    @abstractmethod
    def add_object(self, object: User) -> User:
        """"""
