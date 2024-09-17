# categoria.py

class Categoria:
    """
    Clase que representa una categoría de productos.
    
    Atributos:
    - nombre: El nombre de la categoría.
    - descripcion: Una descripción de la categoría.
    - productos: Lista de productos que pertenecen a esta categoría.
    """
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []  # Inicializa la lista de productos

    def agregar_producto(self, producto):
        """Agrega un producto a la categoría."""
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        """Elimina un producto de la categoría."""
        self.productos.remove(producto)
