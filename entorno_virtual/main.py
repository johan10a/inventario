from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega
from gestion_stock import GestionStock
from consultas_reportes import ConsultasReportes

""" Crear categoría"""

categoria_limpieza = Categoria(nombre="Limpieza", descripcion="Artículos de limpieza")

"""Crear producto"""

producto_escoba = Producto(nombre="Escoba", descripcion="Escoba aspiradora", precio=2000, stock_inicial=20, categoria=categoria_limpieza)

"""Crear proveedor"""

proveedor_limpi_plus = Proveedor(nombre="Limpi Plus", direccion="Calle 5", telefono="4455667")

"""Asociar producto al proveedor"""

proveedor_limpi_plus.agregar_producto(producto_escoba)

"""Crear bodega"""

bodega_principal = Bodega(nombre="Bodega Principal", ubicacion="Centro", capacidad_maxima=500)

"""Asociar producto a la bodega"""

bodega_principal.agregar_producto(producto_escoba, 20)

"""Gestión de stock"""

gestion_stock = GestionStock()
gestion_stock.agregar_stock(producto_escoba, 10)  # Agregar más stock
"""gestion_stock.retirar_stock(producto_escoba, 5)"""   # Retirar stock
gestion_stock.calcular_valor_total_stock([producto_escoba])

""" Consultas y reportes"""
consultas_reportes = ConsultasReportes(
    productos={'Escoba': producto_escoba},
    categorias={'Limpieza': categoria_limpieza},
    proveedores={'Limpi Plus': proveedor_limpi_plus},
    bodegas={'Bodega Principal': bodega_principal}
)

"""Consultar información"""

consultas_reportes.consultar_informacion_producto("Escoba")
consultas_reportes.consultar_informacion_categoria("Limpieza")
consultas_reportes.consultar_informacion_proveedor("Limpi Plus")
consultas_reportes.consultar_informacion_bodega("Bodega Principal")

"""Generar informes"""

consultas_reportes.generar_informe_stock_total()
consultas_reportes.generar_informe_stock_por_categoria()
consultas_reportes.generar_informe_stock_por_proveedor()
consultas_reportes.generar_informe_stock_por_bodega()
