"""add_test_data

Revision ID: e7ac2842a71e
Revises: c7ccf0466e9a
Create Date: 2023-07-17 10:43:01.139808+00:00

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, func

# revision identifiers, used by Alembic.
revision = 'e7ac2842a71e'
down_revision = 'c7ccf0466e9a'
branch_labels = None
depends_on = None

users = table(
    'users',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('login', sa.String, unique=True, default=False),
    sa.Column('password', sa.String, nullable=False),
    sa.Column('email_address', sa.String, nullable=False),
    sa.Column('created_at', sa.DateTime),
    sa.Column('is_admin', sa.Boolean)
)

authors = table(
    'authors',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String, unique=True, nullable=False),
    sa.Column('surname', sa.String, nullable=False),
    sa.Column('middlename', sa.String, nullable=False),
    sa.Column('created_at', sa.DateTime, nullable=True)
)

books = table(
    'books',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('title', sa.String, unique=True, nullable=False),
    sa.Column('created_at', sa.DateTime, nullable=False),
    sa.Column('author_id', sa.Integer, nullable=False)
)

users_list = [
    {
        'id': 1,
        'login': 'test',
        'password': '1234',
        'email_address': 'test@mail.ru',
        'created_at': datetime.now(),
        'is_admin': True
    },
]

authors_list = [
    {
        'id': 1,
        'name': "Игорь",
        'surname': "Бобров",
        'created_at': datetime.now(),
        'middlename': "Александрович",
    },
    {
        'id': 2,
        'name': "Людмила",
        'surname': "Прахова",
        'created_at': datetime.now(),
        'middlename': "Борисовна",
    },
]

books_list = [

    {
        "id": 1,
        'title': "Чистый код",
        'created_at': datetime.now(),
        'author_id': 1
    },
    {
        "id": 2,
        'title': "Программист с чистой совестью",
        'created_at': datetime.now(),
        'author_id': 1
    },
    {
        "id": 3,
        'title': "Тайны единиц и нулей",
        'created_at': datetime.now(),
        'author_id': 2
    },
    {
        "id": 4,
        'title': "Разговор по душам с ЭВМ",
        'created_at': datetime.now(),
        'author_id': 2
    },
]


def upgrade():
    op.bulk_insert(
        users, users_list
    )
    op.bulk_insert(
        authors, authors_list
    )
    op.bulk_insert(
        books, books_list
    )


def downgrade():
    op.execute(sa.delete(users))
    op.execute(sa.delete(authors))
    op.execute(sa.delete(books))
