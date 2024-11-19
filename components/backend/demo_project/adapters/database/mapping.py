from sqlalchemy.orm import registry

from demo_project.adapters.database import tables
from demo_project.application import entities

mapper = registry()

mapper.map_imperatively(entities.User, tables.users)
mapper.map_imperatively(entities.Author, tables.authors)
mapper.map_imperatively(entities.Book, tables.books)
