from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Transacao(BaseModel):
    numero_conta: int
    valor: float

class Deposito(Transacao):
    tipo: str = "Deposito"

class Saque(Transacao):
    tipo: str = "Saque"

class Extrato(BaseModel):
    tipo: str
    valor: float
    data: datetime

class Conta(BaseModel):
    numero: int
    saldo: float
    extrato: List[Extrato]