from abc import ABC, abstractmethod
from typing import Any, Callable, Dict

from kombu import Message

from ssd_libs.components import component

MessageBody = Dict[str, Any]


@component
class MessageHandler(ABC):

    @abstractmethod
    def handle(self, message: Message, body: MessageBody):
        pass


@component
class SimpleMessageHandler(MessageHandler):
    function: Callable[[Any], Any]
    late_ack: bool = True

    def handle(self, message: Message, body: MessageBody):
        if not self.late_ack:
            message.ack()

        self.function(**body)

        if self.late_ack:
            message.ack()
