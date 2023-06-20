from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, username, password):
        self.id = 1  # Since we have only one user, set a static user ID
        self.username = username
        self.password = generate_password_hash(password)  # Hash the password during user creation

    @staticmethod
    def get(user_id):
        if user_id == 1:
            return User('admin', '1234')  # Return the user object for the static user ID
        return None  # Return None for other user IDs (not used in this example)

    def check_password(self, password):
        return check_password_hash(self.password, password)