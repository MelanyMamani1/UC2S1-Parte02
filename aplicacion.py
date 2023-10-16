# Función para validar el login y clave
def validar_credenciales(login, clave):
    try:
        with open("login.txt", "r") as login_file, open("clave.txt", "r") as clave_file:
            logins = login_file.read().splitlines()
            claves = clave_file.read().splitlines()
    except FileNotFoundError:
        print("Error: No se encontraron los archivos de credenciales.")
        return False

    if login in logins and clave in claves:
        return True
    else:
        return False

# Función para mostrar el menú
def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

# Intentos permitidos
intentos = 6

while intentos >= 0:
    usuario_login = input("Ingrese su login: ")
    usuario_clave = input("Ingrese su clave: ")

    if validar_credenciales(usuario_login, usuario_clave):
        print("Inicio de sesión exitoso.")
        mostrar_menu()
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Credenciales incorrectas. Le quedan {intentos} intentos.")
        else:
            print("Número máximo de intentos alcanzado. El programa terminará.")
            break