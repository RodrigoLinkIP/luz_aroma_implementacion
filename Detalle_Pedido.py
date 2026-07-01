from producto import *

class DetallePedido:
    """Representa una línea de un pedido: un producto y su cantidad."""

    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio_unitario

    def sub_total(self) -> float:
        return self.precio_unitario * self.cantidad

    def __repr__(self) -> str:
        return (
            f"DetallePedido(producto='{self.producto.nombre}', "
            f"cantidad={self.cantidad}, subtotal={self.sub_total()})"
        )
