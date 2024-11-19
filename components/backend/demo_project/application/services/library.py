from typing import List, Optional

from ssd_libs.components import component
from ssd_libs.messaging import Message, Publisher

from demo_project.application import interfaces
from demo_project.application.dto.library import AuthorCreateReq, BookCreateReq
from demo_project.application.entities import Author, Book


@component
class LibraryService:
    library_repo: interfaces.ILibraryRepo
    publisher: Optional[Publisher] = None

    def create_author(self, author: AuthorCreateReq) -> Author:
        author_dc = Author(**author.dict())
        self.library_repo.add_object(author_dc)
        msg = {
            'email_message': {
                'txt': 'Появился новый автор',
                'desc': f'{author_dc.surname} {author_dc.name} {author_dc.middlename}'
            }
        }
        self.__publish_message(msg, 'MailEvent')
        return author_dc

    def create_book(self, book: BookCreateReq) -> Book:
        book_dc = Book(**book.dict())
        self.library_repo.add_object(book_dc)
        msg = {
            'email_message': {
                'txt': 'Появилась новая книга!',
                'desc': f'Название книги: {book_dc.title}'
            }
        }
        self.__publish_message(msg, 'MailEvent')
        return book_dc

    def get_all_books(self) -> List[Book]:
        return self.library_repo.all_objects(Book)

    def get_all_authors(self) -> List[Author]:
        return self.library_repo.all_objects(Author)

    def __publish_message(self, msg: dict, queue_name: str) -> None:
        if self.publisher is not None:
            self.publisher.publish(Message(queue_name, msg))
