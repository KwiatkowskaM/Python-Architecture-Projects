from infrastructure import database as db
from adapters.orm_repositories import start_mappers


def initialize_database():
    db.metadata.create_all(db.engine)
    # start_mappers()
