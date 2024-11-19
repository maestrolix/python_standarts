import threading
from contextlib import ContextDecorator

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import PendingRollbackError

from ssd_libs.components import component

from .utils import ThreadSafeCounter


@component(init=False)
class TransactionContext(ContextDecorator):

    def __init__(self, **kwargs):
        self.create_session = sessionmaker(**kwargs)
        self._storage = threading.local()
        self._calls = ThreadSafeCounter()

    def _get_session_if_exists(self):
        return getattr(self._storage, 'session', None)

    @property
    def current_session(self) -> Session:
        session = self._get_session_if_exists()
        if session is None:
            session = self.create_session()
            self._storage.session = session
        return session

    def __enter__(self):
        self._calls.increment()
        return self

    def __exit__(self, *exc):
        self._calls.decrement()

        if self._calls.is_last:
            session = self._get_session_if_exists()
            if session is None:
                return None

            try:
                session.commit()
            except PendingRollbackError:
                session.rollback()
                raise
            finally:
                session.close()

        return False
