from user import User
from auth_exeption import UsernameAlreadyExists
from auth_exeption import PasswordTooshort

class Authenticator:
    def __init__(self):
        self.users= {}

    def add_user(self,username, password):
        if username in self.users:
           raise UsernameAlreadyExists(username)

        if len(password) < 4 :
            raise PasswordTooshort(username)
        self.users[username]= User(username,password)

    def logout(self, username):
        if username in self.users:
            self.users[username].status = False



authenticator= Authenticator()

authenticator.add_user('dorian','1234')

print(authenticator.users)