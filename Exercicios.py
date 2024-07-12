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