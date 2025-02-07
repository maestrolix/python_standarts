"""init

Revision ID: c7ccf0466e9a
Revises:
Create Date: 2023-05-10 10:14:55.344507+00:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c7ccf0466e9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('name', sa.String(length=255), nullable=False, comment='Имя'),
        sa.Column('surname', sa.String(length=255), nullable=False, comment='Фамилия'),
        sa.Column(
            'middlename', sa.String(length=255), nullable=False, comment='Отчество'
        ),
        sa.Column(
            'created_at',
            sa.DateTime(),
            nullable=False,
            comment='Когда была создана запись'
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_authors')),
        comment='Таблица для авторов'
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column(
            'login',
            sa.String(length=255),
            nullable=False,
            comment='Логин пользователя'
        ),
        sa.Column(
            'password',
            sa.String(length=255),
            nullable=False,
            comment='Пароль пользователя'
        ),
        sa.Column(
            'email_address', sa.String(length=255), nullable=False, comment='Почта'
        ),
        sa.Column(
            'created_at',
            sa.DateTime(),
            nullable=False,
            comment='Когда была создана запись'
        ),
        sa.Column(
            'is_admin',
            sa.Boolean(),
            nullable=False,
            comment='Является ли пользователем администратором'
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
        sa.UniqueConstraint('login', name=op.f('uq_users_login')),
        comment='Таблица для пользователей'
    )
    op.create_table(
        'books',
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column(
            'title', sa.String(length=255), nullable=False, comment='Название книги'
        ),
        sa.Column(
            'created_at',
            sa.DateTime(),
            nullable=False,
            comment='Когда была создана запись'
        ),
        sa.Column(
            'author_id',
            sa.Integer(),
            nullable=True,
            comment='ID автора, написавшего книгу'
        ),
        sa.ForeignKeyConstraint(
            ['author_id'], ['authors.id'],
            name=op.f('fk_books_author_id_authors'),
            ondelete='SET NULL'
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_books')),
        comment='Таблица для книг'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('users')
    op.drop_table('authors')
    # ### end Alembic commands ###
