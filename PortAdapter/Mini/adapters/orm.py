from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import registry
from core.entities import User


# Define the table schema
def create_table(metadata):
    user_table = Table(
        'user_account', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('fullname', String, nullable=True),
    )
    return user_table

def map_table(mapper_registry, user_table):
    mapper_registry.map_imperatively(User, user_table)