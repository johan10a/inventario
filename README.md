# Sistema de Gestión de Inventario

**Autor:** Johan Alexis Chara  
**Profesor:** Diego Fernando Marin  
**Curso:** Lenguaje de Programación Avanzado

## Descripción

Este proyecto es un sistema de gestión de inventario que permite registrar productos, categorías, proveedores y bodegas. Además, gestiona el stock de los productos y proporciona diversas consultas y reportes.

## Estructura del Proyecto

- `bodega.py`, `categoria.py`, `producto.py`, `proveedor.py`: Contienen las clases o funciones para representar y gestionar bodegas, categorías, productos y proveedores, respectivamente.
- `consultas_reportes.py`: Se encarga de realizar consultas a las estructuras de datos y generar reportes.
- `gestion_relacion.py`, `gestion_stock.py`: Manejan las relaciones entre las entidades (por ejemplo, qué productos pertenecen a qué categorías) y la gestión del stock.
- `main.py`: Es el punto de entrada de la aplicación. Al ejecutar `python main.py`, se inicia la ejecución del código a partir de este archivo.

## Cómo Ejecutar el Proyecto

Para iniciar el sistema de gestión de inventario, ejecuta el siguiente comando en tu terminal:

```bash
python main.py
