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

#Ex6
#Faça um algoritmo que dado um número inteiro, verifique e mostre se ele é par ou ímpar

numero =  int(input("informe um número:"))
#Verificar se é par, se não ímpar
if numero % 2 == 0 :
    print("O número é par")
else :
    print("O número é impar")
    
#Ex7
#Faça um algoritmo que dado um número, verifique e mostre se o número é positivo ou negativo.

numero = int(input("informe um número:"))
#verifique se o numero digitado e positivo, zero ou negativo
if numero >= -1 and numero > 0: # se o numero for maior igual a -1 e maior que 0 positivo, se for igual a 0, zero, se não negativo
    print(" Positivo ")
elif numero == 0:
    print(" zero ")
else :
    print(" Negativo")

#Ex8
#Faça um algoritmo que receba duas idades e mostre a idade da pessoa mais nova 

idade1 = int(input("informe a primeira idade:"))
idade2 = int(input("informe a segunda  idade:"))

if idade1 < idade2:
    print("A pessoa mais nova é a que tem a Idade", idade1)
elif idade2 < idade1:
    print("A pessoa mais nova é a que tem a Idade", idade2)
elif idade1 == idade2:
    print("As duas pessoas tem a mesma idade")
    
#Ex9
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
    
    