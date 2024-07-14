from infrastructure.database import SessionLocal
from adapters.orm_repositories import SQLAlchemyUserRepository
from application.use_cases import UserService
from infrastructure.init_db import initialize_database


initialize_database()

def main():
    session = SessionLocal()
    user_repository = SQLAlchemyUserRepository(session)
    user_service = UserService(user_repository)

    # Add a new user
    user_service.create_user(name="Krzys", fullname="Krzysztof")
    user_service.create_user(name='Adaś', fullname='Adam')

    # Query the database to verify the user was added
    users = user_service.get_all_users()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()


