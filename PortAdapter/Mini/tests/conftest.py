import sys
sys.path.append('./PortAdapter/Mini/')

from adapters.orm_repositories import SQLAlchemyUserRepository
from application.use_cases import UserService
from infrastructure import database
from infrastructure.init_db import initialize_database

import pytest

@pytest.fixture
def session():
    initialize_database()
    tsession = database.SessionLocal()
    yield tsession
    tsession.close() 