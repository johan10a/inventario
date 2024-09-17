# bodega.py

class Bodega:
    """
    Clase que representa una bodega de almacenamiento.
    
    Atributos:
    - nombre: El nombre de la bodega.
    - ubicacion: La ubicación de la bodega.
    - capacidad_maxima: La capacidad máxima de almacenamiento.
    - productos: Diccionario de productos almacenados y sus cantidades.
    """
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = {}  # Diccionario que mapea productos a sus cantidades

    def agregar_producto(self, producto, cantidad):
        """Agrega una cantidad de un producto a la bodega, verificando la capacidad."""
        if self.espacio_disponible() >= cantidad:
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
        else:
            print(f"No hay suficiente espacio en la bodega '{self.nombre}' para almacenar {cantidad} unidades de {producto.nombre}.")

    def retirar_producto(self, producto, cantidad):
        """Retira una cantidad de un producto de la bodega, verificando el stock disponible."""
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            if self.productos[producto] == 0:
                del self.productos[producto]  # Elimina el producto si el stock llega a 0
        else:
            print(f"No hay suficiente stock de {producto.nombre} en la bodega '{self.nombre}' para retirar {cantidad} unidades.")

    def espacio_disponible(self):
        """Calcula el espacio disponible en la bodega."""
        espacio_ocupado = sum(self.productos.values())
        return self.capacidad_maxima - espacio_ocupado







































































































#     def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
#         self.nombre = nombre
#         self.descripcion = descripcion
#         self.precio = precio
#         self.stock_inicial = stock_inicial
#         self.categoria = categoria

# # los productos
# portatil = Producto("portatil", "usado garantia 3 meses", 1500000, 10, "gamer")
# televisor = Producto("televisor", "nuevo garantia 1 año", 2000000, 100, "4k")

# # Creamos una lista para almacenar los productos
# productos = [portatil, televisor]

# # Imprimimos los productos guardados en la lista, con sus atributos nombre, descripción, precio, stock inicial y categoría a la que pertenece
# for producto in productos:

#     print(f"Producto: {producto.nombre}")
#     print(f"Descripción: {producto.descripcion}")
#     print(f"Precio: ${producto.precio}")
#     print(f"Stock: {producto.stock_inicial} unidades")
#     print(f"Categoría: {producto.categoria}\n")



