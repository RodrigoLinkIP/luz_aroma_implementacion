class Cliente:

    def __init__(
        self,
        dui: str,
        nombre: str,
        telefono: str,
        direccion: str,
        referencia: str
    ):
        self.dui = dui
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.referencia = referencia