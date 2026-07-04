from modulos.cliente import *
from modulos.pedido import *
from modulos.producto import *
from modulos.extras import *

clientes: list[Cliente] = []
categorias: list[Categoria] = []
estados: list[Estado] = []
productos: list[Producto] = []
pedidos: list[Pedido] = []

while True:
    limpiar_terminal()
    print("======== Sistema Luz y Aroma ========")
    print("1. Gestionar Clientes")
    print("2. Gestionar Categorias")
    print("3. Gestionar Estados")
    print("4. Gestionar Productos")
    print("5. Gestionar Pedidos")
    option = pedir_dato("Opción: ", int)
    
    match option:
        case 1:
            while True:
                limpiar_terminal()
                print("======== Clientes ========")
                print("1. Agregar cliente")
                print("2. Buscar cliente")
                print("3. Listar clientes")
                print("4. Eliminar cliente")
                print("0. Salir")
                option = pedir_dato("Opción: ", int)
                
                match option:
                    case 1:
                        limpiar_terminal()
                        print("Ingresa los datos del cliente")
                        agregar_lista(clientes, Cliente(
                            pedir_dato("DUI: "),
                            pedir_dato("Nombre: "),
                            pedir_dato("Telefono: "),
                            pedir_dato("Dirección: "),
                            pedir_dato("Referencia: ")
                        ))
                        print("Cliente agregado exitosamente")
                        input()
                    case 2:
                        limpiar_terminal()
                        if clientes:
                            print("Ingrese el DUI del cliente a buscar")
                            cliente = buscar_objeto(clientes, "dui", pedir_dato("DUI: "))
                            if cliente:
                                print(cliente)
                            else:
                                print("El cliente no existe")
                        else:
                            print("Todavia no se ha agregado ningún cliente")
                        input()
                    case 3:
                        limpiar_terminal()
                        if clientes:
                            print("Los clientes ingresados son:")
                            listar_datos(clientes)
                        else:
                            print("Todavia no se ha agregado ningún cliente")
                        input()
                    case 4:
                        limpiar_terminal()
                        if clientes:
                            print("Ingrese el DUI del cliente a eliminar")
                            cliente = buscar_objeto(clientes, "dui", pedir_dato("DUI: "))
                            if cliente:
                                print("Se eliminará el cliente: ", cliente)
                                eliminar_objeto(clientes, cliente)
                                print("Cliente eliminado exitosamente")
                            else:
                                print("El cliente no existe")
                        else:
                            print("Todavia no se ha agregado ningún cliente")
                        input()
                    case 0:
                        print("Saliendo de clientes...")
                        time.sleep(0.7)
                        break
                    case _:
                        print("Opción invalida")
                        time.sleep(0.5)
        case 2:
            while True:
                limpiar_terminal()
                print("======== Categorias ========")
                print("1. Agregar categoria")
                print("2. Buscar categoria")
                print("3. Listar categoria")
                print("0. Salir")
                option = pedir_dato("Opción: ", int)
                
                match option:
                    case 1:
                        limpiar_terminal()
                        print("Ingresa los datos de la categoria")
                        agregar_lista(categorias, Categoria(
                            asignar_id(categorias),
                            pedir_dato("Nombre: ")
                        ))
                        print("Categoria agregada exitosamente")
                        input()
                    case 2:
                        limpiar_terminal()
                        if categorias:
                            print("Ingrese el ID de la categoria a buscar")
                            categoria = buscar_objeto(categorias, "id", pedir_dato("ID: ", int))
                            if categoria:
                                print(categoria)
                            else:
                                print("La categoria no existe")
                        else:
                            print("Todavia no se ha agregado ninguna categoria")
                        input()
                    case 3:
                        limpiar_terminal()
                        if categorias:
                            print("Las categorias creadas son:")
                            listar_datos(categorias)
                        else:
                            print("Todavia no se ha agregado ninguna categoria")
                        input()
                    case 0:
                        print("Saliendo de categorias...")
                        time.sleep(0.7)
                        break
                    case _:
                        print("Opción invalida")
                        time.sleep(0.5)
        case 3:
            while True:
                limpiar_terminal()
                print("======== Estados ========")
                print("1. Agregar estado")
                print("2. Listar estados")
                print("0. Salir")
                option = pedir_dato("Opción: ", int)
                
                match option:
                    case 1:
                        limpiar_terminal()
                        print("Ingresa el nombre del estado")
                        agregar_lista(estados, Estado(
                            pedir_dato("Nombre: ")
                        ))
                        print("Estado agregado exitosamente")
                        input()
                    case 2:
                        limpiar_terminal()
                        if estados:
                            print("Los estados creados son:")
                            listar_datos(estados)
                        else:
                            print("Todavia no se ha agregado ningun estado")
                        input()
                    case 0:
                        print("Saliendo de estados...")
                        time.sleep(0.7)
                        break
                    case _:
                        print("Opción invalida")
                        time.sleep(0.5)
        case 4:
            while True:
                limpiar_terminal()
                print("======== Productos ========")
                print("1. Agregar producto")
                print("2. Buscar producto")
                print("3. Listar productos")
                print("4. Actualizar precio, stock o estado de producto")
                print("5. Eliminar producto")
                print("0. Salir")
                option = pedir_dato("Opción: ", int)
                
                match option:
                    case 1:
                        limpiar_terminal()
                        if categorias and estados:
                            print("Ingresa los datos del producto")
                            categoria = buscar_objeto(categorias, "id", pedir_dato("ID de la categoria: ", int))
                            estado = buscar_objeto(estados, "nombre", pedir_dato("Nombre del estado: "))
                            if categoria and estado:
                                agregar_lista(productos, Producto(
                                    asignar_id(productos),
                                    pedir_dato("Nombre: "),
                                    pedir_dato("Caracteristicas: "),
                                    pedir_dato("Aroma: "),
                                    pedir_dato("Tamaño: "),
                                    pedir_dato("Precio: ", float),
                                    pedir_dato("Costo: ", float),
                                    pedir_dato("Stock: ", int),
                                    estado,
                                    categoria
                                ))
                                print("Producto agregado exitosamente")
                            else:
                                print("Categoria o estado no encontrados")
                        else:
                            print("Debe haber al menos una categoria y un estado para agregar un producto")
                        input()
                    case 2:
                        limpiar_terminal()
                        if productos:
                            print("Ingrese el ID del producto a buscar")
                            producto = buscar_objeto(productos, "id", pedir_dato("ID: ", int))
                            if producto:
                                print(producto)
                            else:
                                print("El producto no existe")
                        else:
                            print("Todavia no se ha agregado ningún producto")
                        input()
                    case 3:
                        limpiar_terminal()
                        if productos:
                            print("Los productos creados son:")
                            listar_datos(productos)
                        else:
                            print("Todavia no se ha agregado ningún producto")
                        input()
                    case 4:
                        limpiar_terminal()
                        if categorias and estados and productos:
                            print("Ingrese el ID de la categoria a la que pertenece el producto a actualizar")
                            listar_datos(categorias)
                            print()
                            categoria = buscar_objeto(categorias, "id", pedir_dato("ID: ", int))
                            if categoria:
                                listar_datos([p for p in productos if p.categoria == categoria])
                                print("Ingrese el ID del producto a actualizar")
                                producto = buscar_objeto(productos, "id", pedir_dato("ID: ", int))
                                if producto:
                                    print("Producto encontrado: ", producto)
                                    print("1. Actualizar precio")
                                    print("2. Actualizar stock")
                                    print("3. Actualizar estado")
                                    option = pedir_dato("Opción: ", int)
                                    match option:
                                        case 1:
                                            nuevo_precio = pedir_dato("Nuevo precio: ", float)
                                            producto.actualizar_precio(nuevo_precio)
                                            print("Precio actualizado exitosamente")
                                        case 2:
                                            nuevo_stock = pedir_dato("Nuevo stock: ", int)
                                            producto.actualizar_stock(nuevo_stock)
                                            print("Stock actualizado exitosamente")
                                        case 3:
                                            listar_datos(estados)
                                            print()
                                            nuevo_estado_nombre = pedir_dato("Nuevo estado: ")
                                            nuevo_estado = buscar_objeto(estados, "nombre", nuevo_estado_nombre)
                                            if nuevo_estado:
                                                producto.actualizar_estado(nuevo_estado)
                                                print("Estado actualizado exitosamente")
                                            else:
                                                print("Estado no encontrado")
                                        case _:
                                            print("Opción invalida")
                                else:
                                    print("El producto no existe")
                            else:
                                print("La categoria no existe")
                        else:
                            print("Debe haber al menos una categoria, un estado y un producto para actualizar")
                        input()
                    case 5:
                        limpiar_terminal()
                        if productos:
                            print("Ingrese el ID del producto a eliminar")
                            producto = buscar_objeto(productos, "id", pedir_dato("ID: ", int))
                            if producto:
                                print("Se eliminará el producto: ", producto)
                                eliminar_objeto(productos, producto)
                                print("Producto eliminado exitosamente")
                            else:
                                print("El producto no existe")
                        else:
                            print("Todavia no se ha agregado ningún producto")
                        input()
                    case 0:
                        print("Saliendo de productos...")
                        time.sleep(0.7)
                        break
                    case _:
                        print("Opción invalida")
                        time.sleep(0.5)
        case 5:
            while True:
                limpiar_terminal()
                print("======== Pedidos ========")
                print("1. Crear pedido")
                print("2. Buscar pedido")
                print("3. Listar pedidos")
                print("4. Ver detalles de un pedido")
                print("0. Salir")
                option = pedir_dato("Opción: ", int)
                
                match option:
                    case 1:
                        limpiar_terminal()
                        if clientes and productos and estados:
                            print("Ingrese el DUI del cliente que realiza el pedido")
                            cliente = buscar_objeto(clientes, "dui", pedir_dato("DUI: "))
                            if cliente:
                                fecha = pedir_dato("Fecha del pedido (YYYY-MM-DD): ")
                                print("Ingrese los datos del envio")
                                direccion_envio = pedir_dato("Dirección de envio: ")
                                costo_envio = pedir_dato("Costo de envio: ", float)
                                estado_envio_nombre = pedir_dato("Estado del envio: ")
                                estado_envio = buscar_objeto(estados, "nombre", estado_envio_nombre)
                                if not estado_envio:
                                    print("Estado de envio no encontrado")
                                    input()
                                    continue
                                
                                print("Ingrese los datos del pago")
                                metodo_pago = pedir_dato("Método de pago: ")
                                monto_pago = pedir_dato("Monto del pago: ", float)
                                estado_pago_nombre = pedir_dato("Estado del pago: ")
                                estado_pago = buscar_objeto(estados, "nombre", estado_pago_nombre)
                                if not estado_pago:
                                    print("Estado de pago no encontrado")
                                    input()
                                    continue
                                
                                envio = Envio(direccion_envio, costo_envio, estado_envio)
                                pago = Pago(metodo_pago, monto_pago, estado_pago)
                                
                                pedido = Pedido(asignar_id(pedidos), fecha, cliente, envio, pago, Estado("Pendiente"))
                                
                                while True:
                                    print("Agregar productos al pedido:")
                                    listar_datos(productos)
                                    producto_id = pedir_dato("ID del producto a agregar (0 para terminar): ", int)
                                    if producto_id == 0:
                                        break
                                    producto = buscar_objeto(productos, "id", producto_id)
                                    if producto:
                                        cantidad = pedir_dato(f"Cantidad de {producto.nombre}: ", int)
                                        if producto.hay_stock() == False or cantidad > producto.stock:
                                            print(f"La cantidad solicitada supera el stock disponible ({producto.stock}) o el producto no tiene stock disponible.")
                                            continue
                                        else:
                                            pedido.agregar_producto(producto, cantidad)
                                            producto.disminuir_stock(cantidad)
                                            print(f"{cantidad} unidades de {producto.nombre} agregadas al pedido.")
                                    else:
                                        print("Producto no encontrado")
                                
                                pedidos.append(pedido)
                                print(f"Pedido #{pedido.id} creado exitosamente con total ${pedido.calcular_total():.2f}")
                            else:
                                print("Cliente no encontrado")
                        else:
                            print("Debe haber al menos un cliente, un producto y un estado para crear un pedido")
                        input()
                    case 2:
                        limpiar_terminal()
                        if pedidos:
                            print("Ingrese el ID del pedido a buscar")
                            pedido = buscar_objeto(pedidos, "id", pedir_dato("ID: ", int))
                            if pedido:
                                print(pedido)
                            else:
                                print("El pedido no existe")
                        else:
                            print("Todavia no se ha agregado ningún pedido")
                        input()
                    case 3:
                        limpiar_terminal()
                        if pedidos:
                            print("Los pedidos creados son:")
                            listar_datos(pedidos)
                        else:
                            print("Todavia no se ha agregado ningún pedido")
                        input()
                    case 4:
                        limpiar_terminal()
                        if pedidos:
                            listar_datos(pedidos)
                            print()
                            print("Ingrese el ID del pedido para ver sus detalles")
                            pedido = buscar_objeto(pedidos, "id", pedir_dato("ID: ", int))
                            if pedido:
                                print(f"Detalles del Pedido #{pedido.id}:")
                                for detalle in pedido.listar_productos():
                                    print(f"- {detalle.producto.nombre}: {detalle.cantidad} unidades, Subtotal: ${detalle.sub_total():.2f}")
                                print(f"Total del pedido: ${pedido.calcular_total():.2f}")
                            else:
                                print("El pedido no existe")
                        else:
                            print("Todavia no se ha agregado ningún pedido")
                        input()
                    case 0:
                        print("Saliendo de categorias...")
                        time.sleep(0.7)
                        break
                    case _:
                        print("Opción invalida")
                        time.sleep(0.5) 
        case 0:
            print("Saliendo del sistema...")
            time.sleep(0.7)
            break
        case _:
            print("Opción invalidad")
            time.sleep(0.5)