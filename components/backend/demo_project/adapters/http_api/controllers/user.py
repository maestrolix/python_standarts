from falcon import Request, Response
from spectree import Response as RespValidate

from ssd_libs.components import component
from ssd_libs.http_auth import authenticator_needed

from demo_project.adapters.http_api.join_points import join_point
from demo_project.adapters.http_api.spectree import spectree
from demo_project.application import services
from demo_project.application.dto import UserCreateReq, UserCreateResp, user_tag


@authenticator_needed
@component
class User:
    user_service: services.UserService

    @join_point
    @spectree.validate(
        json=UserCreateReq,
        resp=RespValidate(HTTP_200=UserCreateResp),
        tags=(user_tag, )
    )
    def on_post_create_user(self, req: Request, resp: Response):
        """ Создание юзера """
        result = self.user_service.create_user(req.context.json)
        resp.media = result
