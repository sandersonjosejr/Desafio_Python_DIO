from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List
from models import Conta, Transacao, Deposito, Saque, ContaCorrente, TransacaoModel, ExtratoModel
from auth import verify_token
from database import get_db, db

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/transacoes/", response_model=TransacaoModel)
async def criar_transacao(transacao: TransacaoModel, token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    conta = db.get_conta(transacao.numero_conta)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if isinstance(transacao, Deposito):
        conta.depositar(transacao.valor)
    elif isinstance(transacao, Saque):
        conta.sacar(transacao.valor)
    else:
        raise HTTPException(status_code=400, detail="Tipo de transação inválido")

    return transacao

@app.get("/extrato/{numero_conta}", response_model=List[ExtratoModel])
async def exibir_extrato(numero_conta: int, token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    conta = db.get_conta(numero_conta)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    return conta.historico.gerar_relatorio()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/contas/")
async def criar_conta(conta: ContaCorrente):
    db.add_conta(conta)
    return conta