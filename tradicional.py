

def validarUsuario (nombreUsuario,paswordUsuario):
    userDB ="user1234"
    paswordDB = "admin123"
    if paswordUsuario==paswordDB and nombreUsuario == userDB:
        return True
    else:
        return False



resultado= validarUsuario("juan","admin123")
print(resultado)

