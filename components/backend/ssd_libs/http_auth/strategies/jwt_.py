from typing import Any, Dict, Optional, Sequence, Type
import falcon
try:
    import jwt
except ImportError:
    pass

from ssd_libs.http_auth import errors, interfaces
from ssd_libs.http_auth.entities import Client

from .base import BaseStrategy


class JwtClientFactory(interfaces.ClientFactory):

    def get_client_cls(self) -> Type[Client]:
        return Client

    #TODO groups=map(str.strip, instance_params.get('groups', '').split(',')),
    def create(self, **instance_params) -> Client:
        return self.get_client_cls().create(
            user_id=instance_params.get('sub'),
            login=instance_params.get('login'),
            name=instance_params.get('name'),
            groups=instance_params.get('groups', []),
            email=instance_params.get('email'),
            app_groups=instance_params.get('app_groups'),
        )


class JWT(BaseStrategy):
    default_client_factory = JwtClientFactory()

    def __init__(
        self,
        *,
        secret_key: str,
        algorithms: Sequence[str] = None,
        decoding_options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.secret_key = secret_key
        self.algorithms = algorithms or ['HS256']
        self.decoding_options = decoding_options

        try:
            jwt
        except NameError:
            raise AssertionError('Package pyjwt should be installed')

    def _get_client_data(self, request: 'falcon.Request') -> Dict[str, Any]:

        #TODO проверка, есть ли токен в auth
        encoded_token = None
        auth_param = request.auth 
        cockie_token = request.cookies.get('token')

        if cockie_token is None and auth_param is None:
            raise errors.AuthenticationError('No auth info in a request')

        if cockie_token is not None: 
            encoded_token = cockie_token
        else:
            parts = request.auth.split(' ')
            encoded_token = parts[-1]

        try:
            client_data = jwt.decode(
                encoded_token,
                self.secret_key,
                algorithms=self.algorithms,
                options=self.decoding_options,
            )
        except jwt.DecodeError:
            raise errors.AuthenticationError('Token decoding error')
        except jwt.PyJWTError as e:
            raise errors.AuthenticationError(
                f'Unexpected token error [{str(e)}]'
            )
        else:
            return client_data
