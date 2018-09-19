class UserError(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectAuthCodeCode(UserError):
    pass

class UserDoesNotExistError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass

class LoginInvalidError(UserError):
    pass

class UserAlreadyRegistered(UserError):

    pass
class InvalidEmailError(UserError):
    pass
class PoorPasswordError(UserError):
    pass
