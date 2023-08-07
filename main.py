from paquete1.modulo1 import  Cliente
from paquete1.modulo2 import *  

def main():
    #Crear objetos Cliente
    cliente1 = Cliente("Agustina Perez", "agustina@mail.com", "1560027777", "Calle 123")
    cliente2 = Cliente("Juan Gomez", "juang@mail.com", "1550227777", "Avenida 1560")

    # Agrega a los clientes los  productos comprados
    cliente1.agregar_producto("Masaje Thai")
    cliente1.agregar_producto("Sesión Reiki")
    cliente2.agregar_producto("Sesion Reiki")
    cliente2.agregar_producto("Terapia Sacrouterina")

    # Mostrar información de los clientes
    print(cliente1)
    print(cliente1.mostrar_informacion())

    print(cliente2)
    print(cliente2.mostrar_informacion())

if __name__ == "__main__":
    main()