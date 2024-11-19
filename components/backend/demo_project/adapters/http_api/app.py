from functools import partial
from typing import Tuple, Union

import falcon
import rapidjson
from falcon import media

from ssd_libs.http_api import App
from ssd_libs.http_auth import Authenticator

from demo_project.adapters.http_api import auth, controllers
from demo_project.adapters.http_api.settings import SwaggerSettings
from demo_project.adapters.http_api.spectree import setup_spectree
from demo_project.application import services


def create_app(
    is_dev_mode: bool, swagger_settings: SwaggerSettings,
    allow_origins: Union[str, Tuple[str,...]], 
    library_service: services.LibraryService,
    user_service: services.UserService, 
    security_service: services.SecurityService
) -> App:
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)

    if is_dev_mode:
        cors_middleware = falcon.CORSMiddleware(allow_origins='*')
    else:
        cors_middleware = falcon.CORSMiddleware(allow_origins=allow_origins)

    middleware = [cors_middleware]
    app = App(middleware=middleware, prefix='/api')

    authenticator.set_strategies(auth.jwt_strategy)

    app.register(
        controllers.Library(
            authenticator=authenticator, library_service=library_service
        )
    )
    app.register(
        controllers.User(authenticator=authenticator, user_service=user_service)
    )
    app.register(
        controllers.Security(
            authenticator=authenticator, security_service=security_service
        )
    )

    if swagger_settings.ON:
        setup_spectree(
            app=app,
            title=swagger_settings.TITLE,
            path=swagger_settings.PATH,
            filename=swagger_settings.FILENAME,
            servers=swagger_settings.SERVERS,
        )

    json_handler = media.JSONHandler(
        dumps=partial(
            rapidjson.dumps,
            default=str,
        ),
        loads=rapidjson.loads,
    )
    extra_handlers = {
        'application/json': json_handler,
    }

    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)

    return app
