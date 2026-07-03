from modulos.cliente import *
from modulos.pedido import *
from modulos.producto import *

class LuzAroma:
    def __init__(self):
        self.registro_cliente = RegistroCliente()
        self.catalogo = Catalogo()
        self._pedidos = list[Pedido] = []
        
    def agregar_pedido(self, pedido: Pedido):
        self._pedidos.append(pedido)
        
    def buscar_pedido(self, id_pedido: int):
        for pedido in self._pedidos:
            if pedido.id == id_pedido:
                return pedido
        return None
    
    def listar_pedido(self):
        return self._pedidos