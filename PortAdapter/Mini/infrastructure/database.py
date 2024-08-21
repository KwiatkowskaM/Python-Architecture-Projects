from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, registry
from adapters import orm

class DB:

    def __init__(self, connection:str) -> None:
        self.engine = create_engine(connection, echo=False)
        self.metadata = MetaData()
        self.mapper_registry = registry()

    def create_user_table(self) -> Table:
        user_table = orm.create_table(metadata=self.metadata)
        return user_table

    def create_user_session(self):
        user_table = self.create_user_table()
        orm.map_table(self.mapper_registry, user_table=user_table)

# engine = create_engine('sqlite:///:memory:', echo=False)

# metadata = MetaData()
# mapper_registry = registry()

# user_table = orm.create_table(metadata=metadata)
# orm.map_table(mapper_registry, user_table=user_table)

SessionLocal = sessionmaker(bind=engine)