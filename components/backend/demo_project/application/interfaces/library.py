from abc import abstractmethod
from typing import List

from demo_project.application.entities import Author, Book
from ssd_libs.sql_storage.interface import IBaseRepository


class ILibraryRepo(IBaseRepository):

    @abstractmethod
    def add_object(self, object: Book | Author) -> Book | Author:
        """Сохраняет переданный объект в БД и возвращает его."""

    @abstractmethod
    def all_objects(self, cls: type(Book | Author)) -> List[Book | Author]:
        """ Возвращает все записи из таблицы по классу. """
