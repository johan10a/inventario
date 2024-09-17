# consultas_reportes.py

from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

class ConsultasReportes:
    """
    Clase que gestiona consultas sobre productos, categorías, proveedores y bodegas, y genera informes de stock.
    """
    def __init__(self, productos, categorias, proveedores, bodegas):
        self.productos = productos
        self.categorias = categorias
        self.proveedores = proveedores
        self.bodegas = bodegas

    def consultar_informacion_producto(self, nombre_producto):
        """Consulta la información de un producto por su nombre."""
        producto = self.productos.get(nombre_producto)
        if producto:
            print(f"Producto: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: ${producto.precio}")
            print(f"Stock: {producto.stock}")
            print(f"Categoría: {producto.categoria.nombre}")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")

    def consultar_informacion_categoria(self, nombre_categoria):
        """Consulta la información de una categoría por su nombre."""
        categoria = self.categorias.get(nombre_categoria)
        if categoria:
            print(f"Categoría: {categoria.nombre}")
            print(f"Descripción: {categoria.descripcion}")
            print("Productos:")
            for producto in categoria.productos:
                print(f" - {producto.nombre}")
        else:
            print(f"Categoría '{nombre_categoria}' no encontrada.")

    def consultar_informacion_proveedor(self, nombre_proveedor):
        """Consulta la información de un proveedor por su nombre."""
        proveedor = self.proveedores.get(nombre_proveedor)
        if proveedor:
            print(f"Proveedor: {proveedor.nombre}")
            print(f"Dirección: {proveedor.direccion}")
            print(f"Teléfono: {proveedor.telefono}")
            print("Productos suministrados:")
            for producto in proveedor.productos:
                print(f" - {producto.nombre}")
        else:
            print(f"Proveedor '{nombre_proveedor}' no encontrado.")

    def consultar_informacion_bodega(self, nombre_bodega):
        """Consulta la información de una bodega por su nombre."""
        bodega = self.bodegas.get(nombre_bodega)
        if bodega:
            print(f"Bodega: {bodega.nombre}")
            print(f"Ubicación: {bodega.ubicacion}")
            print(f"Capacidad máxima: {bodega.capacidad_maxima}")
            print("Productos almacenados:")
            for producto, cantidad in bodega.productos.items():
                print(f" - {producto.nombre}: {cantidad} unidades")
        else:
            print(f"Bodega '{nombre_bodega}' no encontrada.")

    def generar_informe_stock_total(self):
        """Genera un informe del stock total en todas las bodegas."""
        total_stock = sum(producto.stock for producto in self.productos.values())
        print(f"Stock total en todas las bodegas: {total_stock}")

    def generar_informe_stock_por_categoria(self):
        """Genera un informe del stock por categoría."""
        for categoria in self.categorias.values():
            total_categoria = sum(producto.stock for producto in categoria.productos)
            print(f"Stock total en la categoría '{categoria.nombre}': {total_categoria} unidades.")

    def generar_informe_stock_por_proveedor(self):
        """Genera un informe del stock por proveedor."""
        for proveedor in self.proveedores.values():
            total_proveedor = sum(producto.stock for producto in proveedor.productos)
            print(f"Stock total suministrado por el proveedor '{proveedor.nombre}': {total_proveedor} unidades.")

    def generar_informe_stock_por_bodega(self):
        """Genera un informe del stock por bodega."""
        for bodega in self.bodegas.values():
            total_bodega = sum(cantidad for cantidad in bodega.productos.values())
            print(f"Stock total en la bodega '{bodega.nombre}': {total_bodega} unidades.")
