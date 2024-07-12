from typing import List
from core.entities import User
from ports.repositories import UserRepository

class UserService:

    def __init__(self, user_repository:UserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, name:str, fullname:str) ->None :
        user = User(id = None, name=name, fullname=fullname)
        self.user_repository.add_user(user)

    def get_all_users(self) -> List:
        return self.user_repository.list_users()    