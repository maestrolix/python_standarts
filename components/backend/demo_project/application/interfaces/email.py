from abc import abstractmethod
from typing import List

from ssd_libs.sql_storage.interface import IBaseRepository


class IEmailRepo(IBaseRepository):

    @abstractmethod
    def get_users_email(self) -> List[str]:
        """ Возвращает почты пользователей """
