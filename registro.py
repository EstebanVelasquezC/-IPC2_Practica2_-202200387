from typing import List
from cliente import Cliente

class RegistroClientesApp:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente: Cliente) -> str:
        if self.verificar_existencia(cliente.nit):
            return "Error: El cliente ya existe."
        self.clientes.append(cliente)
        return "Cliente agregado correctamente."

    def verificar_existencia(self, nit: str) -> bool:
        return any(cliente.nit == nit for cliente in self.clientes)

    def obtener_clientes(self) -> List[Cliente]:
        return self.clientes
