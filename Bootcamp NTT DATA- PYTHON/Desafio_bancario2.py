import re

Menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuario
[5] Nova Conta
[6] Sair

=> '''
list_deposito = []
list_saque = []
list_extrato= []
List_usuario = []
List_conta=[]

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3
AGENCIA = "0001"

def criar_usuario(List_usuario):
    cpf = input("Digite o CPF do Usuário: ")
    usuario = buscar_usuario(cpf,List_usuario)

    if usuario:
        print("O usuário já possui uma conta")
        return  # Encerra a função se o CPF já estiver cadastrado

    # Se o CPF não estiver cadastrado, prossegue com o cadastro
    nome = input("Digite o nome do Usuário: ")
    data_de_nascimento = input("Digite a data de nascimento do Usuário: ")
    
    # Solicitando o endereço no formato correto
    endereco = input("Digite o endereço no formato: logradouro, nro, bairro, cidade e sigla do estado entre (): ")

    # Usando regex para separar os componentes do endereço
    padrao = r"^(.*?),\s*(\d+),\s*(.*)\s+(.+)\s\((\w+)\)$"
    match = re.match(padrao, endereco)

    if not match:
        print("Endereço no formato incorreto! Por favor, siga o formato: logradouro, nro, bairro, cidade e sigla do estado entre ()")
        return
    
    logradouro = match.group(1)
    numero = match.group(2)
    bairro = match.group(3)
    cidade = match.group(4)
    estado = match.group(5)
    
    # Adiciona o novo usuário à lista
    List_usuario.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado})

    print("Usuário cadastrado com sucesso!")

    
def buscar_usuario(cpf,List_usuario):
    filtrar_usuario = [usuario for  usuario in List_usuario if usuario["cpf"] == cpf]
    return filtrar_usuario[0] if filtrar_usuario else None
    
def criar_conta(agencia, numero_conta, List_usuario):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, List_usuario)
    
    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
    print(" Usuário não encontrado")

def deposito(saldo,valor,extrato,/):
    if valor >= 0:
        saldo += valor
        list_deposito.append(valor)
        print(f"Depósito de {valor} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")
        
    return saldo,extrato
        
def sacar(*,valor, saldo, extrato,limite,numero_saques, limite_saque):
    
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
        
    return saldo, extrato

def listar_extrato(saldo,/,*,extrato):
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
            
        saldo, extrato = deposito(saldo, valor, extrato)
            
    elif opcao == '2':
        print("Saque")
        valor = float(input("Digite o valor que deseja sacar: "))
        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saque = LIMITE_SAQUE,
        )
    elif opcao == '3':
        listar_extrato(saldo, extrato= extrato)
    elif opcao == '4':
        criar_usuario(List_usuario)
    elif opcao == '5':
        numero_conta = len(List_conta)+1
        conta = criar_conta(AGENCIA, numero_conta, List_usuario)
        
        if conta:
            List_conta.append(conta)
        
    elif opcao == '6':
        break
    else:
        print("Opção inválida, por favor escolha uma opção válida.")
            

