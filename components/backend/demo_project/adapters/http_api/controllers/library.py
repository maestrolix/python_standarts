from attr import asdict
from falcon import Request, Response
from spectree import Response as RespValidate

from ssd_libs.components import component
from ssd_libs.http_auth import authenticate, authenticator_needed, authorize

from demo_project.adapters.http_api.auth import Groups
from demo_project.adapters.http_api.join_points import join_point
from demo_project.adapters.http_api.spectree import spectree
from demo_project.application import services
from demo_project.application.dto.library import (
    BookAllResp,
    AuthorAllResp,
    AuthorCreateReq,
    AuthorCreateResp,
    BookCreateReq,
    BookCreateResp,
    library_tag
)


@authenticator_needed
@component
class Library:
    library_service: services.LibraryService

    @authenticate
    @join_point
    @spectree.validate(
        query=None,
        resp=RespValidate(HTTP_200=BookAllResp),
        tags=(library_tag, )
    )
    def on_get_all_books(self, req: Request, resp: Response):
        """ Возвращает список книг """
        books = self.library_service.get_all_books()
        resp.media = [asdict(book) for book in books]

    @authenticate
    @join_point
    @spectree.validate(
        query=None,
        resp=RespValidate(HTTP_200=AuthorAllResp),
        tags=(library_tag, )
    )
    def on_get_all_authors(self, req: Request, resp: Response):
        """ Возвращает список авторов. """
        authors = self.library_service.get_all_authors()
        resp.media = [asdict(author) for author in authors]

    @authenticate
    @join_point
    @authorize(Groups.ADMINS)
    @spectree.validate(
        json=AuthorCreateReq,
        resp=RespValidate(HTTP_200=AuthorCreateResp),
        tags=(library_tag, )
    )
    def on_post_create_author(self, req: Request, resp: Response):
        """ Создать нового автора. """
        author = self.library_service.create_author(req.context.json)
        resp.media = asdict(author)

    @authenticate
    @join_point
    @authorize(Groups.ADMINS)
    @spectree.validate(
        json=BookCreateReq,
        resp=RespValidate(HTTP_200=BookCreateResp),
        tags=(library_tag, )
    )
    def on_post_create_book(self, req: Request, resp: Response):
        """ Создать новую книгу """
        book = self.library_service.create_book(req.context.json)
        resp.media = asdict(book)
