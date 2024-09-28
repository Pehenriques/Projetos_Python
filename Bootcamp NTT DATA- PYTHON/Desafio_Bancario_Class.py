from abc import ABC, abstractproperty,abstractclassmethod
from datetime import datetime

clientes = []
depositos = []
saques = []

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico ()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def egencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print(" Deposito realizado com Sucesso!!! ")
            self._historico.adicionar_transacao(f"Depósito de R${valor}")
        else:
            print("Operação falhou, por favor informe um valor valido")
            return False
        return True

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print(" Operação encerrada! Saldo infuciente")
        elif valor <= self._saldo:
            self._saldo -= valor
            print(" Saque realizado com sucesso")
            self._historico.adicionar_transacao(f"Saque de R${valor}")
            return True
        else:
            print("Saldo insuficiente")
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite, limite_saque):
        super().__init__( numero, cliente, )
        self.limite = limite
        self.limite_saque = limite_saque
        
    def sacar(self, valor):
        numero_saques = len(Transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__)
        
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque
        
        if excedeu_limite:
            print(" O valor do saque excedeu o limite de saques")
        elif excedeu_saques:
            print("Número de saques excedido ")
        else:
            return super().sacar(valor)
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        conta.depositar(self._valor)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor


    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = self.validar_data(data_nascimento)

    def validar_data(self, data_nascimento):
        try:
            data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data_formatada
        except ValueError:
            print("Data no formato incorreto. Use DD/MM/AAAA.")
            return None

def buscar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

# Exemplo de criação de cliente e conta
nome = input("Digite seu Nome: ")
cpf = input("Digite seu CPF: ")    
data_nascimento = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
endereco = input("Digite seu endereço: ")

# Exemplo de busca de cliente
cpf_procurado = input("Digite o CPF do cliente que deseja buscar: ")
cliente_encontrado = buscar_cliente(cpf_procurado, clientes)

if cliente_encontrado:
    print(f"Cliente encontrado: {cliente_encontrado.nome}, CPF: {cliente_encontrado.cpf}")
else:
    print("Cliente não encontrado!")


