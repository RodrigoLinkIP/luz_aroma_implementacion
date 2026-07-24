import requests

BASE_URL = "http://127.0.0.1:5000"

def mostrar_respuesta(respuesta):
    print(f"Estado: {respuesta.status_code}")
    if respuesta.content:
        try:
            print(respuesta.json())
        except ValueError:
            print(respuesta.text)
    print("-" * 50)
    
if __name__ == "__main__":
    print("========== CLIENTES ==========")

    print("1. Obtener todos los clientes")
    mostrar_respuesta(requests.get(f"{BASE_URL}/clientes", timeout=10))

    # Crear cliente
    # nuevo_cliente = {
    #     "dui": "01234567-8",
    #     "nombre": "Rodrigo López",
    #     "telefono": "7777-7777",
    #     "direccion": "San Salvador",
    #     "referencia": "Plaza Mundo"
    # }
    # print("2. Crear cliente")
    # mostrar_respuesta(
    #     requests.post(
    #         f"{BASE_URL}/clientes",
    #         json=nuevo_cliente,
    #         timeout=10
    #     )
    # )

    # Buscar cliente
    # print("3. Buscar cliente")
    # mostrar_respuesta(
    #     requests.get(
    #         f"{BASE_URL}/clientes/01234567-8",
    #         timeout=10
    #     )
    # )

    # Actualizar cliente
    # cambios = {
    #     "telefono": "7888-9999"
    # }
    # print("4. Actualizar cliente")
    # mostrar_respuesta(
    #     requests.put(
    #         f"{BASE_URL}/clientes/01234567-8",
    #         json=cambios,
    #         timeout=10
    #     )
    # )

    # Eliminar cliente
    # print("5. Eliminar cliente")
    # mostrar_respuesta(
    #     requests.delete(
    #         f"{BASE_URL}/clientes/01234567-8",
    #         timeout=10
    #     )
    # )
    
    print("========== CATEGORÍAS ==========")

    print("1. Obtener todas las categorías")
    mostrar_respuesta(
        requests.get(f"{BASE_URL}/categorias", timeout=10)
    )

    # Crear categoría
    # nueva_categoria = {
    #     "nombre": "Velas Aromáticas"
    # }
    # 
    # print("2. Crear categoría")
    # mostrar_respuesta(
    #     requests.post(
    #         f"{BASE_URL}/categorias",
    #         json=nueva_categoria,
    #         timeout=10
    #     )
    # )

    # Buscar categoría por ID
    # print("3. Buscar categoría")
    # mostrar_respuesta(
    #     requests.get(
    #         f"{BASE_URL}/categorias/1",
    #         timeout=10
    #     )
    # )

    # Actualizar categoría
    # cambios = {
    #     "nombre": "Velas Premium"
    # }
    #
    # print("4. Actualizar categoría")
    # mostrar_respuesta(
    #     requests.put(
    #         f"{BASE_URL}/categorias/1",
    #         json=cambios,
    #         timeout=10
    #     )
    # )

    # Eliminar categoría
    # print("5. Eliminar categoría")
    # mostrar_respuesta(
    #     requests.delete(
    #         f"{BASE_URL}/categorias/1",
    #         timeout=10
    #     )
    # )
    
    print("========== PRODUCTOS ==========")

    print("1. Obtener todos los productos")
    mostrar_respuesta(
        requests.get(f"{BASE_URL}/productos", timeout=10)
    )

    # Crear producto
    # nuevo_producto = {
    #     "nombre": "Vela de Lavanda",
    #     "caracteristicas": "Cera de soya",
    #     "aroma": "Lavanda",
    #     "tamannio": "Grande",
    #     "precio": 15.50,
    #     "costo": 8.75,
    #     "stock": 20,
    #     "id_estado": 1,
    #     "id_categoria": 1
    # }
    # 
    # print("2. Crear producto")
    # mostrar_respuesta(
    #     requests.post(
    #         f"{BASE_URL}/productos",
    #         json=nuevo_producto,
    #         timeout=10
    #     )
    # )

    # Buscar producto
    # print("3. Buscar producto")
    # mostrar_respuesta(
    #     requests.get(
    #         f"{BASE_URL}/productos/1",
    #         timeout=10
    #     )
    # )

    # Actualizar producto
    # cambios = {
    #     "precio": 17.50,
    #     "stock": 35
    # }
    #
    # print("4. Actualizar producto")
    # mostrar_respuesta(
    #     requests.put(
    #         f"{BASE_URL}/productos/1",
    #         json=cambios,
    #         timeout=10
    #     )
    # )

    # Eliminar producto
    # print("5. Eliminar producto")
    # mostrar_respuesta(
    #     requests.delete(
    #         f"{BASE_URL}/productos/1",
    #         timeout=10
    #     )
    # )
    
    # VALIDAR REQUEST INCORRECTAS
    # categoria_invalida = {
    #     "nombre": ""
    # }
    #
    # print("Categoría inválida")
    # mostrar_respuesta(
    #     requests.post(
    #         f"{BASE_URL}/categorias",
    #         json=categoria_invalida,
    #         timeout=10
    #     )
    # )