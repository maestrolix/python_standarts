from typing import Optional

from ssd_libs.components import component
from ssd_libs.messaging import Message, Publisher
from ssd_libs.scheduler import Task

from demo_project.application import interfaces


@component
class LibraryEventService:
    library_event_repo: interfaces.ILibraryEventRepo
    publisher: Optional[Publisher] = None

    def get_reminder_task(self) -> Task:
        msg = {
            'email_message': {
                'txt': 'Книжочка любит вас :3',
                'desc': 'Не забывайте про книжочку'
            }
        }
        task = Task(
            name='reminder',
            cron_schedule='* * * * *',
            job=self.__publish_message,
            job_kwargs={
                'msg': msg,
                'queue_name': 'MailEvent'
            }
        )
        return task

    def __publish_message(self, msg: dict, queue_name: str) -> None:
        if self.publisher is not None:
            self.publisher.publish(Message(queue_name, msg))
