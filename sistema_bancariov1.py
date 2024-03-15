menu = """
    [1] Sacar
    [2] Depositar
    [3] Ver Extrato
    [0 Sair]

==>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Saque")
        
        valor = float(input("Quanto deseja sacar? "))

        if valor <= 0:
            print("Valor Inválido!")
        elif valor > limite:
            print("Operação Inválida. O seu limite por saque é de R$500,00.")
        elif numero_saques == LIMITE_SAQUES:
            print("Operação Inválida, o seu limite de saques diários foi atingido")
        elif valor > saldo:
            print("Operação Inválida. Você não possui saldo suficiente!")
        else:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            print(f"Saque Realizado com sucesso! Você sacou R${valor:.2f}")
    elif opcao == 2:
        print("Depósito")

        valor = float(input("Quanto deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito Realizado com sucesso! Você depositou R${valor:.2f}")
        else:
            print("Valor Inválido, tente novamente.")
    elif opcao == 3:
        print("==============Extrato==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O seu saldo atual é de R${saldo}")
        print("===================================")
    elif opcao == 0:
        break
    else:
        print("Operação Inválida! Por fabor, selecione novamente a operação desejada.")    