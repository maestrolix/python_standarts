from typing import Type, Optional

from attr import asdict
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from ssd_libs.components import component
from ssd_libs.sql_storage.transactions import TransactionContext

from ssd_libs.sql_storage.interface import IBaseRepository


@component
class BaseRepository(IBaseRepository):
    """
    Base class for Repositories, using SQLAlchemy
    """
    context: TransactionContext

    @property
    def session(self) -> Session:
        return self.context.current_session
    
    def add_obj(self, obj: object) -> object: 
        """ Добавляет объект в БД. """
        self.session.add(obj)
        self.session.commit()
        return obj

    def add_objs(self, objs: list[object]) -> list[object]:
        """ Добавляет объекты в БД. """
        self.session.add_all(objs)
        self.session.commit()
        return objs

    def get_obj_by_id(self, id: int, cls: Type) -> Optional[object]: 
        """ Возвращает объект по его ID. """
        query = select(cls).where(cls.id == id)
        return self.session.execute(query).scalar()

    def get_objs_by_ids(self, ids: list[int], cls: Type) -> list[Optional[object]]:
        """ Возвращает список объектов по списку ID. """
        query = select(cls).where(cls.id.in_(ids))
        return self.session.execute(query).scalars().all()

    def del_obj_by_id(self, id: int, cls: Type) -> None: 
        """ Удаляет запись из БД по ID. """
        query = delete(cls).where(cls.id == id)
        self.session.execute(query)
        self.session.commit()
        return None

    def del_objs_by_ids(self, ids: list[int], cls: Type) -> None:
        """ Удаляет записи из БД по списку ID. """
        query = delete(cls).where(cls.id.in_(ids))
        self.session.execute(query)
        self.session.commit()
        return None
    
    def update_obj(self, obj: object, cls: Type) -> object:  
        """ Обналвяет записи в БД по объекту. """
        param = asdict(obj)
        query = update(cls).where(
            cls.id == param.pop('id')
        ).values(param)
        self.session.execute(query)
        self.session.commit()
        return obj

    def update_objs(self, objs: list[object], cls: Type) -> list[object]:
        """ Обновляет записи в БД по объектам. """
        query = update(cls)
        self.session.execute(query, [asdict(obj) for obj in objs])
        self.session.commit()
        return objs