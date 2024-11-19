# Рассылка почты
`#TODO Ссылки на библы`


---

* Установка соединения [sender.py](../../../../../../components/backend/demo_project/adapters/email_sender/sender.py)
  
```python
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
```


* Здесь происходит проверка соединнения и не посредственно формирование
сообщения получателю
```python
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
        message['Subject'] = 'Из маганиза КНИЖЕЧКА :3'
        message['From'] = self.smtp_sender
        message['To'] = 'Вам'

        emails = self.email_service.get_users_email()
        html = Serializer.serialize_event(email_message)
        message.attach(MIMEText(html, 'html'))

        for email in emails:
            self.session.send_message(message, self.smtp_sender, email)
```

## Полезные ссылки
1. [SMTP](https://ru.wikipedia.org/wiki/SMTP)
2. [python smtplib](https://docs.python.org/3/library/smtplib.html)
3. [google email service](https://support.google.com/mail/answer/7126229?hl=ru)
4. [example vidos](https://www.youtube.com/watch?v=ZvAGL0EDLVY)