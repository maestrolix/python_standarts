from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from typing import Optional

from pydantic import validate_arguments

from ssd_libs.components import component

from .serializer import Serializer
from demo_project.application import services
from demo_project.application.dto import Event


@component
class BaseMailSender:
    session: Optional[SMTP] = None,
    smtp_sender: str
    smtp_password: str
    smtp_host: str
    smtp_port: int
    email_service: services.EmailService

    def update_session(self):
        self.session = SMTP(self.smtp_host, self.smtp_port)
        self.session.ehlo()
        self.session.starttls()
        self.session.login(self.smtp_sender, self.smtp_password)


@component
class BookMainSender(BaseMailSender):

    def __check_connection(self):
        try:
            self.session.ehlo()
        except Exception:
            self.update_session()

    @validate_arguments
    def send_event(self, email_message: Event):
        self.__check_connection()
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Из маганиза КНИЖЕЯКА :3'
        message['From'] = self.smtp_sender
        message['To'] = 'Вам'

        emails = self.email_service.get_users_email()
        html = Serializer.serialize_event(email_message)
        message.attach(MIMEText(html, 'html'))

        for email in emails:
            self.session.send_message(message, self.smtp_sender, email)
