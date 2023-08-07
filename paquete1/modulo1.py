class Cliente:
    def __init__(self, nombre, correo, telefono, direccion):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.productos_comprados = []

    def agregar_producto(self, producto):
        self.productos_comprados.append(producto)

    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre}\n"
        info += f"Email: {self.correo}\n"
        info += f"Telefono: {self.telefono}\n"
        info += f"Dirección: {self.direccion}\n"
        info += "Productos comprados:\n"
        for producto in self.productos_comprados:
            info += f" - {producto}\n"
        return info

    def __str__(self):
        return f"Cliente: {self.nombre}"