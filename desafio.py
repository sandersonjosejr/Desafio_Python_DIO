menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque_realizado = 0
deposito_realizado = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito < 0:
            print("Valor de deposito não pode ser negativo, tente com um novo valor!")
        else:
            deposito_realizado += valor_deposito
            saldo += valor_deposito
            print(f"Depósito no valor de R$ {valor_deposito:,.2f} realizado com sucesso!")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if numero_saques > LIMITE_SAQUES:
            print("Você ultrapassou o seu limite de saques diarios, volte amanhã para fazer uma nova retirada!")
        elif valor_saque > limite:
            print("Valor acima do limite por saque, tente um novo valor!")
        elif valor_saque < 0 or valor_saque > saldo:
            print("Valor de saque impossivel, tente novamente com um novo valor!")
        else:
            saque_realizado += valor_saque
            numero_saques += 1
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:,.2f} realizado com sucesso!")

    elif opcao == "e":
        print(f"Extrato \n Valor depositado na conta: R$ {deposito_realizado:,.2f}\n Valor sacado: R$ {saque_realizado:,.2f}\n Saldo restante: R$ {saldo:,.2f}")

    elif opcao == "q":
        print("Muito obrigado por escolher nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")