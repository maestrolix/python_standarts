from typing import List, Tuple

from falcon import App
from spectree import SpecTree
from spectree.models import Server

spectree = SpecTree(
    'falcon',
    mode='strict',
    annotations=True,
    version='v0.1-alpha',
)


def setup_spectree(
    app: App,
    title: str,
    path: str,
    filename: str,
    servers: List[Tuple[str, str]],
):
    servers = [Server(url=url, description=description) for url, description in servers]

    spectree.config.title = title
    spectree.config.path = path
    spectree.config.filename = filename
    spectree.config.servers = servers

    spectree.register(app)
