from kombu import Connection

from ssd_libs.messaging_kombu import KombuConsumer

from .scheme import email_broker_scheme
from demo_project.adapters import email_sender


def create_email_consumer(
    connection: Connection, sender: email_sender.BookMainSender
) -> KombuConsumer:
    consumer = KombuConsumer(connection=connection, scheme=email_broker_scheme)

    consumer.register_function(sender.send_event, 'SendMailEvent')
    return consumer
