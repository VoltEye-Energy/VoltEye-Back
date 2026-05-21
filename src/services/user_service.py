


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def create_user(self, user_data):
        return self.user_repository.create_user(user_data)