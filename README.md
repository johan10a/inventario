# Sistema de Gestión de Inventario

**Autor:** Johan Alexis Chara  
**Profesor:** Diego Fernando Marín  
**Curso:** Lenguaje de Programación Avanzado 1

## Descripción

Este proyecto es un sistema de gestión de inventario que permite registrar productos, categorías, proveedores y bodegas. Además, gestiona el stock de los productos y proporciona diversas consultas y reportes.

## Estructura del Proyecto

- **`bodega.py`**, **`categoria.py`**, **`producto.py`**, **`proveedor.py`**: Contienen las clases o funciones para representar y gestionar bodegas, categorías, productos y proveedores, respectivamente.
- **`consultas_reportes.py`**: Se encarga de realizar consultas a las estructuras de datos y generar reportes.
- **`gestion_relacion.py`**, **`gestion_stock.py`**: Manejan las relaciones entre las entidades (por ejemplo, qué productos pertenecen a qué categorías) y la gestión del stock.
- **`main.py`**: Es el punto de entrada de la aplicación. Al ejecutar `python main.py`, se inicia la ejecución del código a partir de este archivo.
## Documentación 
El listado de requerimientos, y diagrama de clases (UML) se encuentran en la ca carpeta docs

## Cómo Ejecutar el Proyecto

Sigue estos pasos para ejecutar el sistema de gestión de inventario:
   ```bash

 1. Navega a la ruta del entorno virtual:
 
   cd inventario/entorno_virtual
   ```

2. Ejecuta el archivo principal:

python main.py

## Requisitos

Versión de Python: 3.12.5
