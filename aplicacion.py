usuario_txt = open('login.txt','r')
usuarioR= usuario_txt.read();
clave_txt = open('clave.txt','r')
claveR= clave_txt.read();

menu = ("Datos Personales: \n 1. Listar personas \n 2. Agregar personas \n 3. Salir")

def validar_credenciales():
    intentos = 0
    while intentos < 2:
        login = input("Ingrese su login: ")
        clave = input("Ingrese su clave: ")

        if login == usuarioR and clave == claveR:
            return True
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
            intentos += 1

    print("Demasiados intentos incorrectos.")
    return False

if validar_credenciales() :
    print(menu) 
