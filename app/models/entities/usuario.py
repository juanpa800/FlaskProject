from werkzeug.security import check_password_hash #, generate_password_hash

class usuario():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)

# print(generate_password_hash("clave"))
# pbkdf2:sha256:600000$fHuUkFdthHxyR0e9$73ffc124fb8d77336cc29463be95d894bc47381bc92228ba5f967d5f20dc1efd