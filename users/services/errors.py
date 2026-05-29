class UserServiceError(Exception):
    pass


class UserAlreadyExist(UserServiceError):
    pass
