import hashlib
class User:

    def __init__(self, user_name, password):
        self.user_name= user_name
        self.password= self._encrypt_password(password)
        self.status = False

    def check_password(self, password) -> bool:
        encrypted_password = self._encrypt_password(password)
        return  encrypted_password == self.password

    def _encrypt_password(self,password) -> str:
        """"
        crypte le mot de passe en utilisant l'algorithme sha256
        """
        password_encoded = password.encode('utf-8')
        return  hashlib.sha256(password_encoded).hexdigest()
user= User('shadowsod','password')
print(user.check_password('password'))