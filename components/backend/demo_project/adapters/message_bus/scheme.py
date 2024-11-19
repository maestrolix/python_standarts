from kombu import Exchange, Queue

from ssd_libs.messaging_kombu import BrokerScheme

email_broker_scheme = BrokerScheme(
    Queue('SendMailEvent', Exchange('MailEvent')), 
)
