# producto.py

class Producto:
    """
    Clase que representa un producto en el inventario.
    
    Atributos:
    - nombre: El nombre del producto.
    - descripcion: Una descripción del producto.
    - precio: El precio unitario del producto.
    - stock: La cantidad de unidades disponibles.
    - categoria: La categoría a la que pertenece el producto.
    """
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria
        categoria.agregar_producto(self)  # Asocia el producto a una categoría

    def agregar_stock(self, cantidad):
        """Agrega una cantidad especificada de stock al producto."""
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        """Retira una cantidad especificada de stock del producto si hay suficiente."""
        if cantidad > self.stock:
            print(f"No hay suficiente stock de {self.nombre} para retirar {cantidad} unidades.")
        else:
            self.stock -= cantidad
