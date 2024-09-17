# proveedor.py

class Proveedor:
    """
    Clase que representa un proveedor.
    
    Atributos:
    - nombre: El nombre del proveedor.
    - direccion: La dirección del proveedor.
    - telefono: El número de teléfono del proveedor.
    - productos: Lista de productos suministrados por el proveedor.
    """
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []  # Lista de productos suministrados

    def agregar_producto(self, producto):
        """Agrega un producto a la lista de productos suministrados."""
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        """Elimina un producto de la lista de productos suministrados."""
        self.productos.remove(producto)


'''

#Productos
portatil = Producto("Portatil", "usado garantia 3 meses", 1500000, 10, "gamer")
televisor = Producto("televisor", "nuevo garantia 1 año", 2000000, 100, "4k")

#Lista para almacenar los productos
Productos =[portatil, televisor]
'''