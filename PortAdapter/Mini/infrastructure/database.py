from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, registry
from adapters import orm

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
mapper_registry = registry()

user_table = orm.create_table(metadata=metadata)
orm.map_table(mapper_registry, user_table=user_table)

SessionLocal = sessionmaker(bind=engine)