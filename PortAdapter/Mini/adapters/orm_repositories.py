from typing import List
from sqlalchemy.orm import Session
from core.entities import User
from ports.repositories import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def list_users(self) -> List[User]:
        return self.session.query(User).all()