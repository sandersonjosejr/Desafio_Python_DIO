from typing import List, Optional
from models import Conta, Deposito, Saque

class FakeDB:
    def __init__(self):
        self.contas = []

    def add_conta(self, conta: Conta):
        self.contas.append(conta)

    def get_conta(self, numero: int) -> Optional[Conta]:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

db = FakeDB()