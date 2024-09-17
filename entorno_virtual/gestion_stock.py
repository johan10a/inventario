# gestion_stock.py

from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

class GestionStock:
    """
    Clase que gestiona las operaciones de stock como agregar y retirar productos, así como calcular el valor total.
    """
    def agregar_stock(self, producto, cantidad):
        """Agrega stock a un producto existente."""
        producto.agregar_stock(cantidad)
        print(f"Se han agregado {cantidad} unidades de {producto.nombre}. Stock actual: {producto.stock}")

    def retirar_stock(self, producto, cantidad):
        """Retira stock de un producto existente."""
        producto.retirar_stock(cantidad)
        print(f"Se han retirado {cantidad} unidades de {producto.nombre}. Stock actual: {producto.stock}")

    def calcular_valor_total_stock(self, productos):
        """Calcula el valor total del stock disponible en productos."""
        valor_total = 0
        for producto in productos:
            valor_total += producto.precio * producto.stock
        print(f"El valor total del stock es: ${valor_total}")
