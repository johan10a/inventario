# Diagramas del Proyecto

## Diagrama de Clases (UML)

### Clases Principales:

- **Producto**: 
  Representa un artículo que se vende o almacena. Tiene los siguientes atributos:
  - **Atributos**: nombre, descripción, precio, stock, categoría.
  - **Operaciones**: agregar o retirar stock, mostrar información del producto.

- **Categoría**: 
  Define el tipo de producto (por ejemplo, electrónica, ropa, alimentos).
  - **Atributos**: nombre, descripción.
  - **Operaciones**: agregar, eliminar y mostrar productos asociados a la categoría.

- **Bodega**: 
  Representa un lugar físico donde se almacenan los productos.
  - **Atributos**: nombre, ubicación, capacidad máxima.
  - **Operaciones**: agregar o retirar productos, calcular capacidad disponible, agregar nuevas bodegas.

- **Proveedor**: 
  Representa la entidad que suministra los productos.
  - **Atributos**: nombre, dirección, teléfono.
  - **Operaciones**: agregar o eliminar proveedores, agregar o eliminar productos asociados a un proveedor.

### Relaciones Entre Clases:

- **Producto - Categoría (1,n)**: 
  Un producto pertenece a una sola categoría (**1**), mientras que una categoría puede tener muchos productos (**n**). Relación de **uno a muchos**.

- **Producto - Bodega (n,n)**: 
  Un producto puede estar en varias bodegas (**n**), y una bodega puede tener muchos productos (**n**). Relación de **muchos a muchos**.

- **Producto - Proveedor (n,n)**: 
  Un producto puede ser suministrado por varios proveedores (**n**), y un proveedor puede suministrar muchos productos (**n**). Relación de **muchos a muchos**.

- **Bodega - Proveedor (n,n)**: 
  Una bodega puede recibir productos de varios proveedores (**n**), y un proveedor puede suministrar productos a varias bodegas (**n**). Relación de **muchos a muchos**.

### Interpretación del Diagrama:

Este diagrama ilustra cómo el sistema gestiona un inventario de productos clasificados por categorías, almacenados en diferentes bodegas y suministrados por varios proveedores. Cada producto:
- Pertenece a una única categoría.
- Puede estar en varias bodegas.
- Puede ser suministrado por varios proveedores.

### Diagrama UML:

![Diagrama UML](img/diagrama%20de%20clases%20(UML).png)
