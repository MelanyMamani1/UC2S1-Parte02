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

# Función para listar personas
def listar_personas():
    try:
        with open("dni.txt", "r") as dni_file, open("nombre.txt", "r") as nombre_file, open("apellido.txt", "r") as apellido_file:
            dni_list = dni_file.read().splitlines()
            nombre_list = nombre_file.read().splitlines()
            apellido_list = apellido_file.read().splitlines()

        if len(dni_list) == len(nombre_list) == len(apellido_list):
            for i in range(len(dni_list)):
                print(f"DNI: {dni_list[i]}, Nombre: {nombre_list[i]}, Apellido: {apellido_list[i]}")
        else:
            print("Error: Los archivos no tienen la misma cantidad de registros.")
    except FileNotFoundError:
        print("Error: Archivos de datos no encontrados.")

# Función para agregar personas
def agregar_personas():
    nuevo_dni = input("Ingrese el DNI de la nueva persona: ")
    nuevo_nombre = input("Ingrese el nombre de la nueva persona: ")
    nuevo_apellido = input("Ingrese el apellido de la nueva persona: ")

    try:
        with open("dni.txt", "a") as dni_file, open("nombre.txt", "a") as nombre_file, open("apellido.txt", "a") as apellido_file:
            dni_file.write(nuevo_dni + "\n")
            nombre_file.write(nuevo_nombre + "\n")
            apellido_file.write(nuevo_apellido + "\n")
        print("Nueva persona agregada exitosamente.")
    except Exception as e:
        print(f"Error al agregar la persona: {str(e)}")

# Intentos permitidos
intentos = 6

while intentos >= 0:
    usuario_login = input("Ingrese su login: ")
    usuario_clave = input("Ingrese su clave: ")

    if validar_credenciales(usuario_login, usuario_clave):
        print("Inicio de sesión exitoso.")
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                listar_personas()
            elif opcion == '2':
                agregar_personas()
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Credenciales incorrectas. Le quedan {intentos} intentos.")
        else:
            print("Número máximo de intentos alcanzado. El programa terminará.")
            break
