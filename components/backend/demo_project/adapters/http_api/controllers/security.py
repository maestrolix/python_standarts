from falcon import Request, Response
from spectree import Response as RespValidate

from ssd_libs.components import component
from ssd_libs.http_auth import authenticator_needed

from demo_project.adapters.http_api.join_points import join_point
from demo_project.adapters.http_api.spectree import spectree
from demo_project.application import services
from demo_project.application.dto import UserAuthInfo, UserHttpException, security_tag


@authenticator_needed
@component
class Security:
    security_service: services.SecurityService

    @join_point
    @spectree.validate(
        json=UserAuthInfo,
        resp=RespValidate(
            HTTP_200=None, 
            HTTP_404=UserHttpException,
            HTTP_403=UserHttpException
        ),
        tags=(security_tag, )
    )
    def on_post_login(self, req: Request, resp: Response):
        """ """
        token, exp = self.security_service.try_login(req.context.json)
        resp.set_cookie(
            'token', token, http_only=False, expires=exp, secure=False, path='/'
        )
