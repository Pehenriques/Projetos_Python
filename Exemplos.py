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