import threading
from typing import Any, Callable, Dict, Optional

import attr
from kombu import Connection
from kombu.pools import producers

from ssd_libs.components import component
from ssd_libs.messaging import Message, Publisher

from .scheme import BrokerScheme

ProducerParams = Dict[str, Any]
ProducerParamsStrategy = Callable[[str], ProducerParams]


@component
class KombuPublisher(Publisher):
    connection: Connection
    scheme: BrokerScheme
    params_for_target: Optional[ProducerParamsStrategy] = None
    messages_params: Dict[str, Any] = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        self.pool = producers[self.connection]
        self.local = threading.local()

        if self.params_for_target is None:
            self.params_for_target = self.params_from_mapping_or_scheme

    @property
    def producer(self):
        if not hasattr(self.local, 'producer'):
            self.local.producer = self.pool.acquire(block=True)
        return self.local.producer

    def on_finish(self):
        self.producer.release()
        del self.local.producer

    def publish(self, *messages: Message):
        for message in messages:
            self.producer.publish(message.body, **self.params_for_target(message.target))

    def params_from_mapping(self, target: str) -> ProducerParams:
        return self.messages_params.get(target)

    def params_from_scheme(self, target: str) -> ProducerParams:
        exchange = self.scheme.exchanges[target]
        return dict(exchange=exchange)

    def params_from_mapping_or_scheme(self, target: str) -> ProducerParams:
        params = self.params_from_mapping(target)
        if params:
            return params

        return self.params_from_scheme(target)
