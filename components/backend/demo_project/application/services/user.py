from ssd_libs.components import component

from demo_project.application import interfaces
from demo_project.application.dto import UserCreateReq
from demo_project.application.entities import User
from demo_project.application.utils import hash_password


@component
class UserService:
    user_repo: interfaces.IUserRepo

    def create_user(self, user: UserCreateReq) -> dict:
        user_dc = User(**user.dict())

        is_exists = self.user_repo.get_by_login(user_dc.login)
        if is_exists is not None:
            raise

        user_dc.password = hash_password(user_dc.password)
        self.user_repo.add_object(user_dc)
        return {'msg': 'success'}
