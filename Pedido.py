from Cliente import Cliente
from producto import Producto, Estado
from Envio_Pago import Envio, Pago
from Detalle_Pedido import DetallePedido

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