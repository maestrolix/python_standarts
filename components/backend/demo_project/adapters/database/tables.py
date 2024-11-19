from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, MetaData, String, Table, func

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(
    naming_convention=naming_convention
)

users = Table(
    'users',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Идентификатор'
    ),
    Column(
        'login',
        String(255),
        unique=True,
        nullable=False,
        comment='Логин пользователя'
    ),
    Column(
        'password',
        String(255),
        nullable=False,
        comment='Пароль пользователя'
    ),
    Column(
        'email_address',
        String(255),
        nullable=False,
        comment='Почта'
    ),
    Column(
        'created_at',
        DateTime,
        default=func.now(),
        nullable=False,
        comment=
        'Когда была создана запись'
    ),
    Column(
        'is_admin',
        Boolean,
        default=False,
        nullable=False,
        comment='Является ли пользователем администратором'
    ),
    comment='Таблица для пользователей'
)

authors = Table(
    'authors',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Идентификатор'
    ),
    Column(
        'name',
        String(255),
        nullable=False,
        comment='Имя'
    ),
    Column(
        'surname',
        String(255),
        nullable=False,
        comment='Фамилия'
    ),
    Column(
        'middlename',
        String(255),
        nullable=False,
        comment='Отчество'
    ),
    Column(
        'created_at',
        DateTime,
        default=func.now(),
        nullable=False,
        comment=
        'Когда была создана запись'
    ),
    comment='Таблица для авторов'
)

books = Table(
    'books',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Идентификатор'
    ),
    Column(
        'title',
        String(255),
        nullable=False,
        comment='Название книги'
    ),
    Column(
        'created_at',
        DateTime,
        default=func.now(),
        nullable=False,
        comment='Когда была создана запись'
    ),
    Column(
        'author_id',
        ForeignKey(
            'authors.id',
            ondelete='SET NULL'
        ),
        comment='ID автора, написавшего книгу'
    ),
    comment='Таблица для книг'
)
