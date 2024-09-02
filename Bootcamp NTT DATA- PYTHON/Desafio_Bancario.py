Menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> ''' 

list_deposito = []
list_saque = []
list_extrato= []

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

def deposito(valor):
    global saldo
    if valor >= 0:
        saldo += valor
        list_deposito.append(valor)
        print(f"Depósito de {valor} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")
        
def sacar(valor):
    global saldo, numero_saques

    if numero_saques >= LIMITE_SAQUE:
        print("Não é possível realizar mais saques.")
    elif valor > saldo:
        print(f"O valor de saque {valor} é maior que o saldo disponível.")
    elif valor > limite:
        print(f"O valor {valor} é maior que o limite de saque de {limite}.")
    else:
        saldo -= valor
        numero_saques += 1
        list_saque.append(valor)
        print(f"Saque de {valor} realizado com sucesso! Saldo atual: {saldo}")

def listar_extrato():
    total_depositos = len(list_deposito)
    total_saques = len(list_saque)
    
    print("Extrato:")
    print("===================================")
    print(f"Total de depósitos realizados: {total_depositos}")
    for deposito in list_deposito:
        print(f"Depósito: R${deposito}")
    
    print(f"Total de saques realizados: {total_saques}")
    for saque in list_saque:
        print(f"Saque: R${saque}")

    print(f"Saldo atual: R${saldo}")
    print("===================================")



while True:
    opcao = input(Menu)
    
    if opcao == '1':
        valor = float(input("Digite o valor a ser depositado: "))
        deposito(valor)
    elif opcao == '2':
        print("Saque")
        valor = float(input("Digite o valor que deseja sacar: "))
        sacar(valor)
    elif opcao == '3':
       listar_extrato()
    elif opcao == '4':
        break
    else:
        print("Opção inválida, por favor escolha uma opção válida.")