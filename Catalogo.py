from producto import *

class Catalogo:

    def __init__(self):
        self._productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self._productos.append(producto)

    def obtener_producto(self, id_producto: int) -> Producto | None:
        for producto in self._productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.obtener_producto(id_producto)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True