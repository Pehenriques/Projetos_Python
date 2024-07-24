import matplotlib.pyplot as plt
import math
from random import randint
from time import sleep
#Programa para calcular Dados Numericos 
#Ex1

#Dados de Entrada
numero1= int(input(" informe o primeiro Número"))
numero2= int(input(" informe o segundo Número"))
#Dados de Processamento 
soma = numero1 + numero2
#Dados de Saida 
print(" A somas dos Numeros é: ", soma)

#Ex2
# Faça um progrmaa Python que dado dois numeros, calcule e mostre a soma, a multiplicação, a divisão e a subtração destes números

N1 = int(input(" informe o primeiro Número: " ))
N2 = int(input(" informe o segundo Número: " ))

soma= N1 + N2
sub= N1 - N2
mult= N1 * N2
div= N1 / N2

print(" A Soma dos Números é:", soma)
print(" A Subtração dos Números é:", sub)
print(" A Multiplicação dos Números é:", mult)
print(" A Divisão dos Números é %.2f:" %div)

#Ex3
#Faça um algoritmo que receba três notas. calcule e mostre a média aritmética entre elas. Sabendo - se que:
#                                MEDIA_ARITMETICA = (NOTA1 + NOTA2 + NOTA3)/3

nota1 = int(input(" Digite sua primera nota: " ))
nota2 = int(input(" Digite sua segunda nota: " ))
nota3 = int(input(" Digite sua terceira nota: " ))

mediaA= (nota1+nota2+nota3)/3

print(" A média aritmética das suas notas é:", mediaA)

#Ex4
#Elabora um algoritmo que solicite ao usuário as seguintes informações de uma pessoa: peso e altura.
#O programa deverá calcular o índice de massa copórea(IMC = peso/(altura*altura)).
#O progframa deverá exibir na tela o resultado do IMC.

peso = int(input("Informe seu Peso para o calculo de IMC: " ))
altura = int(input(" Informe sua Altura para o calculo de IMC: " ))

imc= peso/(altura*altura)
 
print(" Seu IMC e de %.3f:" %imc)

#Ex5
#Faça um algoritmo que calcule e mostre a área de um triângulo. Sabendo -se que: 
#                                    Área=(base*altura)/2                 


base = int(input(" Digite o valor da Base do triangulo: " ))
altura = int(input(" Digite o valor da Altura do triangulo: " ))

area = (base*altura)/2

print(" A Área deste triangule é", area)

#Ex6
#Faça um algortimo que receba o salário de um funcionário,calcule e mostre o novo salário, 
# Sabendo - se que este sofreu um de 25%

salarioM =int(input(" Informe seu novo salario: " ))


SalarioN = (salarioM*0.25) + salarioM

print("O salario atual com o reajuste é de:", SalarioN)

#Ex7
#Faça um algoritmo que dado um número inteiro, verifique e mostre se ele é par ou ímpar

numero =  int(input("informe um número:"))
#Verificar se é par, se não ímpar
if numero % 2 == 0 :
    print("O número é par")
else :
    print("O número é impar")
    
#Ex8
#Faça um algoritmo que dado um número, verifique e mostre se o número é positivo ou negativo.

numero = int(input("informe um número:"))
#verifique se o numero digitado e positivo, zero ou negativo
if numero >= -1 and numero > 0: # se o numero for maior igual a -1 e maior que 0 positivo, se for igual a 0, zero, se não negativo
    print(" Positivo ")
elif numero == 0:
    print(" zero ")
else :
    print(" Negativo")

#Ex9
#Faça um algoritmo que receba duas idades e mostre a idade da pessoa mais nova 

idade1 = int(input("informe a primeira idade:"))
idade2 = int(input("informe a segunda  idade:"))

if idade1 < idade2:
    print("A pessoa mais nova é a que tem a Idade", idade1)
elif idade2 < idade1:
    print("A pessoa mais nova é a que tem a Idade", idade2)
elif idade1 == idade2:
    print("As duas pessoas tem a mesma idade")
    
#Ex10
#Faça um algoritmo que receba a idades e o nome de duas pessoase mostre a idade da pessoa mais velho 
    
idade1 = int(input("informe a idade da primeira pessoa:"))
nome1= input("informe nome da primeira pessoa:")

idade2 = int(input("informe a idade da segunda pessoa:"))
nome2= input("informe nome da segunda pessoa:")

if idade1 > idade2:
    print("A pessoa mais velha é o(a)", nome1)
elif idade2 > idade1:
    print("A pessoa mais velha é o(a)", nome2)
elif idade1 == idade2:
    print( nome1, " e ", nome2,"tem a mesma idade")


#Ex 1050 do Beecrowd, If, else ...
DDD = int( input())

if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("São Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else :
    print("DDD não cadastrado")
    
#Ex 1052 do Beecrowd, If, else ...

Valor = int( input())

if Valor == 1:
    print("January")
elif Valor == 2:
    print("February")
elif Valor == 3:
    print("March")
elif Valor == 4:
    print("April")
elif Valor == 5:
    print("May")
elif Valor == 6:
    print("June")
elif Valor == 7:
    print("July")
elif Valor == 8:
    print("August")
elif Valor == 9:
    print("September")
elif Valor == 10:
    print("October")
elif Valor == 11:
    print("November")
elif Valor == 12:
    print("December")

#Ex
#Desenvolva um programa que mostre todos os numeros de 1 à 100 de For para While
for contador in range(1,101):
    print(contador)

#Em While
contador = 1

while contador <= 100:
    print(contador)
    contador = contador +1

#Ex
#Faça um programa que leia valores numéricos ate que um zero seja lido e mostre a quantidade de números lidos
quantidade = 0

numero = int(input("Informe um número"))

while numero !=0:
    quantidade = quantidade + 1
    numero = int(input("Informe um número"))
    
print("A quantidade de números digitados é:", quantidade)

#Ex
#Desenvolva um programa que mostre todos os números de 20 até 1 em FOR
for contador in range(20, 0, -1):
    print(contador)
    
#Ex
#Faça um programa que lê um conjunto de valores até que um zero seja lido. Determine e imprime a soma dos valores lidos
soma = 0

numero = int(input("Informe um número"))

while numero !=0:
    soma = soma + numero #A variavel Soma recebe o numero digitado, quarda ele e soma com o proximo numero
    numero = int(input("Informe um número"))

print("A soma dos números digitados é:", soma)

#Varendo uma lista

lista = ["maçã", "banana", "morango", "uva"]

for fruta in lista:
    print(fruta)
    
#Ex
# Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

#ler uma lista de 5 números 
i = 0
lista = []

for i in range(5):
    lista.append(input("Informe um número:"))
    
#mostra número e posição na lista
for posicao, elemento in enumerate(lista):
    print("Posição:", posicao,"Número:", elemento)

#Ex
#ler uma lista de 10 números reais e mostre os na ordem inversa.

#ler uma lista de 10 números 
i = 0
lista = []

for i in range(10):
    lista.append(input("Informe um número:"))
#inverte a ordem digitada
lista.reverse()
print("A ordem inversa da digitada é:", lista)

#Ex
#ler uma lista com 4 notas, em seguida o progroma deve exibir as notas e a media

notas = []

for i in range(4):
    nota = int(input("Digite uma nota : "))
    notas.append(nota)
quant = len(notas)
total = sum(notas)
media = total/len(notas)

print("As notas são:", notas)
print("A media das notas é", media)

#Ex
#Ler um vetor com 20 idades e exibir a maior e menor

idades = []

for i in range(20):
    idade = int(input("Digite uma idade : "))
    idades.append(idade)
maior = max(idades)
menor = min(idades)

print("A maior idade é", maior," e o menor é", menor)

#Ex
"""
   Faça um programa que leia um número indeterminado de notas até digitaar um número negativo. Após esta entrada de dados, faça o seguinte :
   - Mostre a quantidade de notas que foram lidas.
   - Exiba todas as notas da ordem em que foram informadas uma abaixo do outra.
   - Calcule e mostre a soma das notas.
   - Calcule e mostre a média das notas.
   - Calcule e mostre a quantidade de notas acima da média calculada. 
"""

notas = []

quant_notas = int(input("Quantas notas você deseja inserir? "))

for i in range(quant_notas):
   nota = float(input("Digite uma nota : "))
   notas.append(nota)
   notas.sort()
   
quant = len(notas)
soma = sum(notas)
media = soma/quant

# Exibe as notas na ordem em que foram informadas
print("As notas informadas são;")
for nota in notas:
    print("%.2f:" %nota)
    
print("A quantidade de notas informadas é", quant)   
print("A soma das notas são %.2f:" %soma)
print("A soma das notas são %.2f:" %media)

#Ex
#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def fun_quant_digitos(numero):
    texto = str(numero)
    return len(texto)

#entrada de dados 
n = int(input(" Informe um número:"))
#chamada da função 
cont =  fun_quant_digitos(n)
#mostra resultado
print("Aquantidade de digitos é",cont)

#Ex
#Escreva  uma função que retorne o menor entre dois números
def fun_return_M(numeros):
    return numeros

numero1 = int(input("Informe o primeiro número"))
numero2 = int(input("Informe o segundo número"))

#chamada da função 
n1 = fun_return_M(numero1)
n2 = fun_return_M(numero2) 

#mostra resultado
if numero1 > numero2:
    print("O numero menor é ", n2)
elif numero2 > numero1:
    print("O numero menor é ", n1)
else:
    print(" Os numeros são iguais")
    
#Ex
#Crie uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume (v= 4/3*pi*(raio*3))
def calcula_volume_esfera(raio):
    # Fórmula do volume da esfera: V = (4/3) * pi * raio^3
    volume = (4/3) * math.pi * (raio**3)
    return volume


raio = 3
volume = calcula_volume_esfera(raio)

print("O volume da esfera é:",volume)

#Ex
#Faça um programa Pythom contendo uma função que retorne True se número digitado for par ou Falso se o número for impar.

def fun_par_impar(par, impar):
    return par,impar

numero = int(input(" digite um numero"))

par= fun_par_impar(True, False)[0]
impar = fun_par_impar(True, False)[1]

if numero % 2 == 0:
    print(par)
else:
    print(impar)
    
#Ex
#Faça um procedimento que lê 5 valores  interios e mostre a soma desses números.
def proc ():
    soma = 0
    for i in range(5):
        x = int(input("Informe um número"))
        soma = soma + x
        print(" A soma é", soma)
        
proc ()

#Ex
#Classe Retangulo: crie uma classe que modele um retângulo.Teste o programa.
# - Atributos: base e altura
# - Métodos: calcular área e calcular perímetro. 

class Retangulo():
    base = 0
    altura = 0
    
def calcularArea(self):
    return self.base * self.altura

def calcularPerimetro(self):
    return 2 * self.base + 2 * self.altura

Retangulo = Retangulo()
Retangulo.base = 2
Retangulo.altura = 4
print("A área do é %.2f" %Retangulo.calcularArea())
print("O perimentro e %.2f" %Retangulo.calcularPerimetro())

#Ex 
"""
Classe Pessoa: crie uma Classeque modele uma Pessoa:
 - Atributos: nome, idade, peso e altura 
 - Métodos: envelhecer, engordar, emagrecer, crescer.

Obs: por padrão, a cada ano que a nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm
Teste o programa
"""

class Pessoa:
    nome='' 
    idade=0
    peso=0.0
    altura=0.0
    
    def envelhecer(self):
        if self.idade <= 21:
            self.altura += 0.05
        self.idade += 1
        return self.idade

    def engordar(self, peso):
        self.peso += peso
        return self.peso

    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso

    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.5
        return self.altura

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

pessoa = Pessoa()
pessoa.nome = nome 
pessoa.idade = idade
pessoa.peso = peso
pessoa.altura = altura

print(pessoa.nome, "você mais velho, agora com", pessoa.envelhecer(), "\033[0;37m Anos. \033[m")
print(pessoa.nome, "você mais gordo, agora com", pessoa.engordar(2.5), "\033[0;31m Kg. \033[m")
print(pessoa.nome, "você mais magro, agora com", pessoa.emagrecer(1.0), "\033[0;34m Kg. \033[m")
print(pessoa.nome, "você mais alto, agora com", pessoa.crescer(), "\033[0;32m M. \033[m")

#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#no final, mostre a matriz na tela, com a formatação correta.
#a) A soma de todos os valores pares digitados.
#b) A soma dos valores da terceira coluna.
#c) O maior valor da segunda tabela.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somac = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        #aqui ira entrar os valores [0,0] ate [2,2] sendo 3x3 a mastriz
        matriz[linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        # print para organização
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        #aqui nossa matriz sera organiza com 5 casas dentro do [0,0] caso tenho numeros ate 5 casas e ficara alinhada (^5 e o alinhamento da matriz)
        print(f"[{matriz[linha][coluna]:^5}]",end='')
        if matriz[linha][coluna]% 2 == 0 :
            soma += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f" A soma dos valores pares é {soma}")
for linha in range(0, 3):
    somac += matriz[linha][2]
print(f"a soma dos valores da terceira coluna é {somac}")
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da segunda linha é o {maior}")

#faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.

#from random import randint
#from time import sleep

lista = list()
jogos = list()
print("        JOGANDO NA MEGA CENA         ")
quant = int(input('Quantos jogos você quer que eu sorteie ?'))
total = 0
while total <= quant -1:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f"    SORTEANDO {quant} JOGOS     ")
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f"        BOA SORTE         ")