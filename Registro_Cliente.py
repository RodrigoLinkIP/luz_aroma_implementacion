from Cliente import Cliente


class RegistroCliente:

    def __init__(self):
        self._clientes: list[Cliente] = []

    def agregar_cliente(self, cliente: Cliente) -> None:
        self._clientes.append(cliente)

    def buscar_cliente(self, dui: str) -> Cliente | None:
        for cliente in self._clientes:
            if cliente.dui == dui:
                return cliente
        return None

    def listar_clientes(self) -> list[Cliente]:
        return list(self._clientes)

    def eliminar_cliente(self, dui: str) -> bool:
        cliente = self.buscar_cliente(dui)

        if cliente is None:
            return False

        self._clientes.remove(cliente)
        return True