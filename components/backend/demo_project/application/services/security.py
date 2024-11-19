import datetime
import time

import falcon
import jwt

from ssd_libs.components import component

from demo_project.adapters.http_api.auth import Groups, secret_key
from demo_project.application import interfaces
from demo_project.application.dto.security import UserAuthInfo
from demo_project.application.utils import compare_passwords


@component
class SecurityService:
    user_repo: interfaces.IUserRepo

    def try_login(self, user: UserAuthInfo) -> tuple[str, datetime]:
        user_db = self.user_repo.get_by_login(user.login)

        if user_db is None:
            raise falcon.HTTPError(
                status=404, 
                title='Пользователь не найден',
                description=f'Пользователь с логином {user.login} не найден'
            )
        if not compare_passwords(user.password, user_db.password):
            raise falcon.HTTPError(
                status=403, 
                title='Неправильный пароль',
                description=f'Введите новый пароль'
            )
        if user_db.is_admin:
            group = Groups.ADMINS
        else:
            group = Groups.USERS

        token = jwt.encode(
            {
                'sub': user_db.id,
                'login': user_db.login,
                'name': '',
                'groups': [group.name],
                'exp': int(time.time()) + 60 * 2 * 24
            },
            key=secret_key
        )
        exp = datetime.datetime.now() + datetime.timedelta(seconds=60**2 * 24)
        return token, exp
