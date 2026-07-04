# Sistema de Gestión "Luz y Aroma"

## Descripción

Este sistema permite administrar la información de una tienda llamada **Luz y Aroma**, encargada de la venta de productos aromáticos. Desde el menú principal es posible gestionar clientes, categorías, estados, productos y pedidos.

---

# Menú Principal

Al iniciar el programa se muestran las siguientes opciones:

1. Gestionar Clientes
2. Gestionar Categorías
3. Gestionar Estados
4. Gestionar Productos
5. Gestionar Pedidos
6. Salir

Cada opción dirige al módulo correspondiente.

---

# Gestión de Clientes

Permite administrar los clientes registrados.

### Agregar cliente

Solicita:

* DUI
* Nombre
* Teléfono
* Dirección
* Referencia

Una vez ingresados los datos, el cliente queda almacenado en el sistema.

### Buscar cliente

Busca un cliente utilizando su DUI.

### Listar clientes

Muestra todos los clientes registrados.

### Eliminar cliente

Solicita el DUI del cliente y lo elimina del sistema si existe.

---

# Gestión de Categorías

Permite administrar las categorías de los productos.

### Agregar categoría

Cada categoría recibe automáticamente un ID y únicamente se solicita su nombre.

### Buscar categoría

Busca una categoría mediante su ID.

### Listar categorías

Muestra todas las categorías registradas.

---

# Gestión de Estados

Los estados son utilizados para indicar la disponibilidad de productos y el estado de envíos y pagos.

### Agregar estado

Solicita únicamente el nombre del estado.

Ejemplos:

* Disponible
* Agotado
* Enviado
* Pendiente
* Pagado

### Listar estados

Muestra todos los estados registrados.

---

# Gestión de Productos

Para crear productos es necesario haber registrado previamente al menos una categoría y un estado.

### Agregar producto

Solicita:

* ID de la categoría
* Nombre
* Características
* Aroma
* Tamaño
* Precio
* Costo
* Stock
* Estado

Si la categoría y el estado existen, el producto se registra correctamente.

### Buscar producto

Busca un producto mediante su ID.

### Listar productos

Muestra todos los productos registrados.

### Actualizar producto

Permite modificar:

* Precio
* Stock
* Estado

Primero se selecciona la categoría y luego el producto que se desea actualizar.

### Eliminar producto

Solicita el ID del producto y lo elimina si existe.

---

# Gestión de Pedidos

Para crear un pedido deben existir:

* Clientes registrados.
* Productos registrados.
* Estados registrados.

### Crear pedido

El proceso consiste en:

1. Seleccionar el cliente mediante su DUI.
2. Ingresar la fecha del pedido.
3. Registrar la información del envío.
4. Registrar la información del pago.
5. Agregar uno o varios productos indicando la cantidad deseada.
6. Finalizar ingresando **0** como ID del producto.

Durante este proceso el sistema verifica que exista suficiente stock antes de agregar cada producto y descuenta automáticamente las unidades vendidas.

Al finalizar se muestra el total del pedido.

### Buscar pedido

Busca un pedido mediante su ID.

### Listar pedidos

Muestra todos los pedidos registrados.

### Ver detalles de un pedido

Presenta:

* Productos incluidos.
* Cantidad de cada producto.
* Subtotal por producto.
* Total del pedido.

---

# Consideraciones

* Los IDs de categorías, productos y pedidos se generan automáticamente.
* Las búsquedas se realizan utilizando el identificador correspondiente (DUI, ID o nombre, según el caso).
* El stock de un producto disminuye automáticamente cuando este se agrega a un pedido.
* Si no existen los datos necesarios (clientes, categorías, estados o productos), el sistema notificará al usuario y no permitirá realizar la operación correspondiente.
* Toda la información se mantiene únicamente mientras el programa permanece en ejecución.

* (Todos los derechos de este README estan dirigidos al amigo de todos los niños,
* pesé a entender el proyecto, la forma más rápida y concisa de explicarlo se hizo con él)