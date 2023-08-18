from models.entities.usuario import usuario

class ModelUsuarios():

    @classmethod
    def login(self, conn,user):
        print("estoy en modelusuario")
        try:
            cursor = conn.cursor()
            # Es mejor invocar un SP
            query = """
                SELECT *
                FROM usuarios
                WHERE username = '{}'
            """.format(user.username)
            cursor.execute(query)
            row = cursor.fetchone()
            print(row)
            if row != None:
                user = usuario(row[1], usuario.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex) 