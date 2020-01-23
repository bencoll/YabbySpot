class CustomError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFoundError(CustomError):
    pass


class UserAlreadyRegisteredError(CustomError):
    pass


class InvalidEmailError(CustomError):
    pass


class IncorrectPasswordError(CustomError):
    pass
