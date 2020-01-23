from typing import Dict

from common import CustomErrors, Database, Utils
import uuid


class User:
    COLLECTION = 'users'

    def __init__(self, first_name: str, last_name: str, email: str, password: str, _id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def register_user(cls, first_name: str, last_name: str, email: str, password: str):
        # check if email already exists
        try:
            cls.find_by_email(email)
            # email already exists
            raise CustomErrors.UserAlreadyRegisteredError('A user with that email has already been registered.')
        except CustomErrors.UserNotFoundError:
            # email not taken
            if Utils.validate_email(email):
                new_user = cls(first_name, last_name, email, Utils.hash_password(password))
                Database.insert(cls.COLLECTION, new_user.json())
            else:
                raise CustomErrors.InvalidEmailError('The email you have entered is invalid.')

    @classmethod
    def attempt_login(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise CustomErrors.IncorrectPasswordError('The username or password you have entered is incorrect.')

        return True

    @classmethod
    def find_by_email(cls, email):
        try:
            return cls(**Database.find_one(cls.COLLECTION, {'email': email}))
        except TypeError:
            raise CustomErrors.UserNotFoundError(f"A user with the email '{email}' could not be found.")
