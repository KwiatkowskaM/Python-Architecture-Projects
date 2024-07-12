from abc import ABC, abstractmethod
from typing import List

from core.entities import User

class UserRepository(ABC):
    
    
    @abstractmethod
    def add_user(self, user:User) -> None: 
        pass

    @abstractmethod
    def list_users(self) -> List:
        pass