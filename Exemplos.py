import matplotlib.pyplot as plt
mensagem = "exemplo de mensagem"
n = 25
pi = 3.141592

print( type (mensagem) )
print(type (n))
print(type (pi))

nota1 = 10.0
nota2 = 8.0
media = ( nota1 + nota2)/2

print( " A media das notas é", media)

x =  input(" Informe o primeiro numero:")
y =  input(" Informe o segundo numero:")
soma = float(x) + float(y)

print(" a Soma dos números é:", soma)


nota = float(input("Digite sua nota:"))

if nota >= 6.0:
    print(" Aluno aprovado")
elif nota >=4 and nota < 6:
    print("Aluno de Recuperação")
else :
    print("Aluno reprovado")
    
#Repete de 0 até 9
for contador in range(10):
    print(contador)
    
#Repete de 1 até 10
for contador in range(1,11):
    print(contador)

#Repete de 10 até 1 ( O -1 é o passo )
for contador in range(10, 0, -1):
    print(contador)
    
#Mostra lista de frutas 
for contador in ("Banana", "Maçã", "Morango"):
    print(contador)
else:
    print("laço chegou ao fim")
    

contador = 1 

while contador <= 10:
    print(contador)
    contador = contador +1
    
#Importa uma Biblioteca
import numpy as np 

#Cria um Vetor
vetor = np.array([1,1.5,2,2.5])
print(vetor)

#Cria uma matriz
matriz = np.array([ [1, 2, 3], [3, 2, 1]])
print(matriz)

#Exemplos de Listas 

lista = []
print(lista)

lista = ['O carro', ' peixe', 123, 111]
print(lista)

nova_lista = [ 'pedra', lista]
print(nova_lista) 

#Criando um Dicionário
d = {}
d["João"] = 25
d["José"] = 15
d["Maria"] = 21
print(d)

#Função dict
novo_d = dict(a = 10, b = 20, c = 30)
print(novo_d)
print(novo_d["a"])

#Exemplo de criação de função
def fun_soma(a,b):
     return a + b
 
numero1= int(input("informe o primeiro número"))
numero2= int(input("informe o segundo número"))

soma = fun_soma(numero1,numero2)

print(" o resultado da soma é:", soma)

#exemplo de f(X) = x2
def f(x):
    return x*x

print(f(2))

#Exemplo
#Função para calculo de horas extras

def calculo_pagamento(quant_horas, valor_hora):
    horas = float(quant_horas)
    taxa = float(valor_hora)
    
    if horas <= 40:
        salario = horas*taxa
    else:
        h_exced = horas - 40
        salario = 40*taxa +(h_exced*(1.5*taxa))
    
    return salario
    
horas = int(input("informe as horas trabalhadas"))
taxa = int(input("informe o valor da hora trabalhada"))
total_salario = calculo_pagamento(horas,taxa)
print("O salario deste funcionario é", total_salario)

#Exemplo de função sem retorno
def hello(nome):
    print("Olá",nome)
    
n = input("Qual é o nome ?")
hello(n)

#Exemplo simples do exercício abaixo 
#Faça um programa Pythom contendo uma função que retorne True se número digitado for par ou Falso se o número for impar.

def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número: "))

if eh_par(numero):
    print("O número é par.")
else:
    print("O número é ímpar.")
    
#Exemplo da Matplotlib
plt.plot ([1,2,3,4] , [4,7,8,12])
plt.show ()

#Exemplo 2
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']
valores = [105235,107697,110256,109236,108859,109986]
plt.plot (meses,valores)
plt.show ()

#Exemplo 3meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']
valores = [105235,107697,110256,109236,108859,109986]
plt.title("faturamento no primeiro semestre de 2022")
plt.xlabel("meses")
plt.ylabel("Faturamento em R$")
plt.plot (meses,valores)
plt.show ()

#exemplos de tupla
lanche = ("hamburguer","suco", "pizza","pudim")
#print(lanche)
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
    
#for cont in range(0, len(lanche)):
    #print(lanche[cont])
