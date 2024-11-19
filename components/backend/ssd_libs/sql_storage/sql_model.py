from sqlalchemy.orm import declared_attr
from sqlmodel import SQLModel


class SQLModelSSD(SQLModel):

    class ConfigTable:
        table_name = None

    @declared_attr
    def __tablename__(cls) -> str:
        if cls.ConfigTable.table_name is None:
            table_name = cls.__name__.replace('-', ' ').replace('_', ' ').title().replace(' ', '')
        else:
            table_name = cls.ConfigTable.table_name
        return table_name
