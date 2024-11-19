
class AuthExeption(Exception):
    def __init__(self, username, user=None):
        super().__init__(self, username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthExeption):
    pass

class PasswordTooshort (AuthExeption):
    pass

class InvalidUsername (AuthExeption):
    pass

class InvalidPassword (AuthExeption):
    pass

class NoPermission (AuthExeption):
    pass

