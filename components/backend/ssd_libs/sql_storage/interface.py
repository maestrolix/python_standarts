from abc import ABC, abstractmethod
from typing import Optional, Type


class IBaseRepository(ABC):
    """ Расширение функционала базового репозитория. """

    @abstractmethod
    def add_obj(self, obj: object) -> object:
        """ Добавляет объект в БД. """

    @abstractmethod
    def add_objs(self, objs: list[object]) -> list[object]:
        """ Добавляет объекты в БД. """

    @abstractmethod
    def get_obj_by_id(self, id: int, cls: Type) -> Optional[object]:
        """ Возвращает объект по его ID. """

    @abstractmethod
    def get_objs_by_ids(self, ids: list[int], cls: Type) -> list[Optional[object]]:
        """ Возвращает список объектов по списку ID. """

    @abstractmethod
    def del_obj_by_id(self, id: int, cls: Type) -> None:
        """ Удаляет запись из БД по ID. """

    @abstractmethod
    def del_objs_by_ids(self, ids: list[int], cls: Type) -> None:
        """ Удаляет записи из БД по списку ID. """

    @abstractmethod
    def update_obj(self, obj: object, cls: Type) -> object:
        """ Обналвяет записи в БД по объекту. """

    @abstractmethod
    def update_objs(self, objs: list[object], cls: Type) -> list[object]:
        """ Обновляет записи в БД по объектам. """
