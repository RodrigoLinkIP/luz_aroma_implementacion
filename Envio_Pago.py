from producto import Estado

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