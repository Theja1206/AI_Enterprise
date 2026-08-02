
class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "User Already Exists"
        super().__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self):
        self.message = "User not found"
        super().__init__(self.message)


class DatabaseException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


