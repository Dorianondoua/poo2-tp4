from authenticator import Authenticator
class Authorizor:
    permission_key =1
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}
    

    def add_permission(self, permission_name):
        if permission_name not in self.permission:
            self.permission[self.permission_key]= permission_name
            self.permission_key += 1

authenticator= Authenticator()
authenticator.add_user('dorian','12345')
authorizor= Authorizor(authenticator)
authorizor.add_permission('AJOUTER')
authorizor.add_permission('Supprimer')
print(authorizor.permission)