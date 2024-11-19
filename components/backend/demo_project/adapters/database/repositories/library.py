from typing import List

from sqlalchemy import select

from ssd_libs.components import component
from ssd_libs.sql_storage import BaseRepository

from demo_project.application import interfaces
from demo_project.application.entities import Author, Book


@component
class LibraryRepo(BaseRepository, interfaces.ILibraryRepo):

    def add_object(self, object: Book | Author) -> Book | Author:
        self.session.add(object)
        self.session.commit()
        return object

    def all_objects(self, cls: type(Book | Author)) -> List[Book | Author]:
        query = select(cls)
        return self.session.execute(query).scalars().all()
