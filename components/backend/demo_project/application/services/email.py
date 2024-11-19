from typing import List

from ssd_libs.components import component

from demo_project.application import interfaces


@component
class EmailService:
    email_repo: interfaces.IEmailRepo

    def get_users_email(self) -> List[str]:
        return self.email_repo.get_users_email()
