from typing import List

from sqlalchemy import select

from ssd_libs.components import component
from ssd_libs.sql_storage import BaseRepository

from demo_project.application import interfaces
from demo_project.application.entities import User


@component
class EmailRepo(BaseRepository, interfaces.IEmailRepo):

    def get_users_email(self) -> List[str]:
        query = select(User.email_address)
        return self.session.execute(query).scalars().all()
