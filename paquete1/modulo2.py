
base_datos={}
#crea diccionario para almacenar base de datos
def registrar_usuario(base_datos):
    usuario = input("Creá tu nombre de usuario: ")
    password = input("Creá tu contraseña: ")
    base_datos[usuario] = password
    print("Usuario registrado exitosamente.")

# Mostrar info almacenada
def mostrar_info(base_datos):
    print("Información de usuario almacenada:")
    for usuario, password in base_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {password}")

# Función para el login de usuarios
def login_usuario(base_datos):
    usuario = input("Ingresá tu nombre de usuario: ")
    if usuario in base_datos.keys():
        intentos = 2
        while intentos > 0:
            password = input("Ingresá tu contraseña: ")
            if base_datos[usuario] == password:
                return "Sesión Iniciada"
            else:
                intentos -= 1
                print(f"Contraseña incorrecta. Quedan {intentos} intentos.")
        return "Contraseña incorrecta. Volviendo al menú principal."
    else:
        return "Usuario no registrado"


if __name__ == "__main__":

    base_datos = {}

    while True:
        print("1) Crear usuario")
        print("2) Ver información de usuarios")
        print("3) Iniciar sesión")
        print("4) Finalizar")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            registrar_usuario(base_datos)
        elif opcion == "2":
            mostrar_info(base_datos)
        elif opcion == "3":
            resultado_login = login_usuario(base_datos)
            print(resultado_login)
        elif opcion == "4":
            print("¡Adiós!")
            break