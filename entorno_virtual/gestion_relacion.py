from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

class GestionRelacion:
    def __init__(self, categorias, proveedores, bodegas):
        self.categorias = categorias  # Diccionario de categorías por nombre
        self.proveedores = proveedores  # Diccionario de proveedores por nombre
        self.bodegas = bodegas  # Diccionario de bodegas por nombre

    def agregar_producto_a_categoria(self, nombre_categoria, producto):
        """Agregar un producto a una categoría existente."""
        categoria = self.categorias.get(nombre_categoria)
        if categoria:
            categoria.agregar_producto(producto)
            print(f"Producto '{producto.nombre}' agregado a la categoría '{nombre_categoria}'.")
        else:
            print(f"Categoría '{nombre_categoria}' no encontrada.")

    def eliminar_producto_de_categoria(self, nombre_categoria, producto):
        """Eliminar un producto de una categoría existente."""
        categoria = self.categorias.get(nombre_categoria)
        if categoria:
            categoria.eliminar_producto(producto)
            print(f"Producto '{producto.nombre}' eliminado de la categoría '{nombre_categoria}'.")
        else:
            print(f"Categoría '{nombre_categoria}' no encontrada.")

    def agregar_producto_a_proveedor(self, nombre_proveedor, producto):
        """Agregar un producto a la lista de productos suministrados por un proveedor existente."""
        proveedor = self.proveedores.get(nombre_proveedor)
        if proveedor:
            proveedor.agregar_producto(producto)
            print(f"Producto '{producto.nombre}' agregado a la lista de productos del proveedor '{nombre_proveedor}'.")
        else:
            print(f"Proveedor '{nombre_proveedor}' no encontrado.")

    def eliminar_producto_de_proveedor(self, nombre_proveedor, producto):
        """Eliminar un producto de la lista de productos suministrados por un proveedor existente."""
        proveedor = self.proveedores.get(nombre_proveedor)
        if proveedor:
            proveedor.eliminar_producto(producto)
            print(f"Producto '{producto.nombre}' eliminado de la lista de productos del proveedor '{nombre_proveedor}'.")
        else:
            print(f"Proveedor '{nombre_proveedor}' no encontrado.")

    def agregar_producto_a_bodega(self, nombre_bodega, producto, cantidad):
        """Agregar un producto a la lista de productos almacenados en una bodega existente."""
        bodega = self.bodegas.get(nombre_bodega)
        if bodega:
            if bodega.capacidad_maxima >= cantidad:
                bodega.agregar_producto(producto, cantidad)
                print(f"Producto '{producto.nombre}' agregado a la bodega '{nombre_bodega}' con {cantidad} unidades.")
            else:
                print(f"No hay suficiente espacio en la bodega '{nombre_bodega}' para agregar {cantidad} unidades del producto '{producto.nombre}'.")
        else:
            print(f"Bodega '{nombre_bodega}' no encontrada.")

    def retirar_producto_de_bodega(self, nombre_bodega, producto, cantidad):
        """Retirar un producto de la lista de productos almacenados en una bodega existente."""
        bodega = self.bodegas.get(nombre_bodega)
        if bodega:
            try:
                bodega.retirar_producto(producto, cantidad)
                print(f"Producto '{producto.nombre}' retirado de la bodega '{nombre_bodega}' con {cantidad} unidades.")
            except ValueError as e:
                print(e)
        else:
            print(f"Bodega '{nombre_bodega}' no encontrada.")

    def consultar_disponibilidad_en_bodega(self, nombre_bodega, producto):
        """Consultar la disponibilidad de un producto en una bodega específica."""
        bodega = self.bodegas.get(nombre_bodega)
        if bodega:
            cantidad_disponible = bodega.consultar_disponibilidad(producto)
            print(f"Cantidad disponible del producto '{producto.nombre}' en la bodega '{nombre_bodega}': {cantidad_disponible}")
            return cantidad_disponible
        else:
            print(f"Bodega '{nombre_bodega}' no encontrada.")
            return 0

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de categorías, proveedores y bodegas
    categoria_electronica = Categoria(nombre="Electrónica", descripcion="Dispositivos electrónicos")
    producto_televisor = Producto(nombre="Televisor", descripcion="Televisor 4K", precio=500, stock_inicial=20, categoria=categoria_electronica)
    
    proveedor_amazon = Proveedor(nombre="Amazon", direccion="123 Amazon St", telefono="555-1234")
    
    bodega_central = Bodega(nombre="Bodega Central", ubicacion="Av. Principal", capacidad_maxima=1000)
    
    # Crear instancia de gestión de relaciones
    relaciones = GestionRelacion(
        categorias={'Electrónica': categoria_electronica},
        proveedores={'Amazon': proveedor_amazon},
        bodegas={'Bodega Central': bodega_central}
    )

    # Agregar y eliminar productos
    relaciones.agregar_producto_a_categoria('Electrónica', producto_televisor)
    relaciones.eliminar_producto_de_categoria('Electrónica', producto_televisor)
    
    relaciones.agregar_producto_a_proveedor('Amazon', producto_televisor)
    relaciones.eliminar_producto_de_proveedor('Amazon', producto_televisor)
    
    relaciones.agregar_producto_a_bodega('Bodega Central', producto_televisor, 30)
    relaciones.retirar_producto_de_bodega('Bodega Central', producto_televisor, 10)
    
    relaciones.consultar_disponibilidad_en_bodega('Bodega Central', producto_televisor)
