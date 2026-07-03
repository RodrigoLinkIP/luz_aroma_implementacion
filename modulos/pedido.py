from modulos.cliente import Cliente
from modulos.producto import Producto, Estado

class Pago:
    def __init__(self,metodo_pago: str, monto: float, estado: Estado):
        self.metodo_pago = metodo_pago
        self.monto = monto
        self.estado = estado
        
class Envio:
    def __init__(self, direccion: str, costo: float, estado: Estado):
        self.direccion = direccion
        self.costo = costo
        self.estado = estado
        
class DetallePedido:
    """Representa una línea de un pedido: un producto y su cantidad."""

    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio

    def sub_total(self) -> float:
        return self.precio_unitario * self.cantidad

    def __repr__(self) -> str:
        return (
            f"DetallePedido(producto='{self.producto.nombre}', "
            f"cantidad={self.cantidad}, subtotal={self.sub_total()})"
        )

class Pedido:
    def __init__(self, id: int, fecha: str, cliente: Cliente, envio: Envio, pago: Pago, estado: Estado):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self._detalles: list[DetallePedido] = []
        self.envio = envio
        self.pago = pago
        self.estado = estado
        
    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")
        
        detalle = DetallePedido(producto, cantidad)
        self._detalles.append(detalle)
        
    def calcular_total(self) -> float:
        return sum(detalle.sub_total() for detalle in self._detalles)
    
    def listar_productos(self) -> list[DetallePedido]:
        return list(self._detalles)
    
    def __str__(self):
        return f"Pedido # {self.id} - {self.fecha} - Cliente: {self.cliente} - Total: ${self.calcular_total():.2f}"