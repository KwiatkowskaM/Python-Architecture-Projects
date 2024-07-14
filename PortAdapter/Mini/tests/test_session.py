import pytest
import sys
sys.path.append('./PortAdapter/Mini/')

from sqlalchemy import inspect
from infrastructure import database as db



def test_session_creation(session):
    assert session.is_active

def test_table_mapping(session):
    table_columns = db.user_table.columns.keys()

    expected_columns = ["id", "name", "fullname"]
    assert table_columns == expected_columns


def test_correct_mapping(session):
    engine = session.get_bind()
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()

    for schema in schemas:
        for table_name in inspector.get_table_names(schema=schema):
            col_list = [str(column) for column in inspector.get_columns(table_name, schema=schema)]
    
    excepted = ["{'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'primary_key': 1}",
                "{'name': 'name', 'type': VARCHAR(), 'nullable': False, 'default': None, 'primary_key': 0}",
                "{'name': 'fullname', 'type': VARCHAR(), 'nullable': True, 'default': None, 'primary_key': 0}"]
    
    assert col_list == excepted
