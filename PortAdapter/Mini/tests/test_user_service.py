import pytest
import sys
sys.path.append('./PortAdapter/Mini/')

from adapters.orm_repositories import SQLAlchemyUserRepository
from application.use_cases import UserService
from core.entities import User

@pytest.fixture
def user_service(session):
    user_repository = SQLAlchemyUserRepository(session)
    user_service = UserService(user_repository)
    return user_service


def test_add_user(user_service):
    user_service.create_user(name="TestUser", fullname="TestUser")

    expected = [User(id=1, name='TestUser', fullname='TestUser')]

    users = user_service.get_all_users()

    assert users == expected

