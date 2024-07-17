# para agregar cadas decimais utilize: "%.3f" % , o numero de casas decimais vem antes do 'f' como no exemplo: ("A Divisão dos Números é %.2f:" %div)
#Dispositivos de entrada: Input,o Input recebe valores como String, caso digite alguma numero converta antes do dispositivo de entrada 
#Para receber valores como inteiros ou floats, utilize como no exemplo: int(input(" informe o primeiro valor"))
"""
Import's

Import Math e o importe matematico.

Math.sqrt(4) retorno  a raiz quadrada 
Math.factorial(4) retorna o fatorial
math.modf(2.5) retorna o valor inteiro e o valor fracionario 
Math.log(20,10) logaritmo de 20 na base 10
Math.pi Constante de PI
Math,pow(2,3) 2 elevado a 3
Math.sin (45) retorna o Seno

Import Numpy as np ( "as" e para averbrimarmos o nome )
Numpy e uma biblioteca

"""
#Operadores Aritméticos
# Divisão inteira //
# Exponenciação **
# Resto da Divisão (mod) %

#Funções Prontas
#Float (x) -> Converte o valor x para float
#int(x)-> Converte o valor de x para inteiro
#str(x)-> Converte o valot de x para string
#Print(x)-> imprime os dados da tela
# x = input() -> recebe dados do teclado 

"""
    Estruturas Condicionais
    
    IF -> (se)
    : -> (então)
    ELSE -> (se não)
    ELIF-> (se não se)
    
    IF < Condição > :  
         <Comando>
    ELSE:
        <Comando>     
        
   caso tenha mais de uma condição      

IF < Condição > :  
         <Comando>
    ELIF:
        <Comando> 
    ELSE:
        <Comando>      

"""

"""

    Estrutura de Repetição 
    
    FOR -> (Para)
    IN -> (EM)
    : -> (então)
    
    FOR < Variavel > IN < Lista_de_Valores > :
    < Sequência_de_comandos >
    
    WHILE -> (ENQUANTO) 
    : -> (então)
    
    WHILE < Expressão-lógica >:
    < Sequencia_de_comandos >

"""

"""
    
    Sobre Arrays, lista, Tupla, Conjunto, Dicionário, 
    
    Para toda lista utilize []
    
    Funções de lista
    lista.append = Adiciona um item a lista
    lista.remove = Remove um item da lista 
    del lista [x] = Remove um item da posição x da lista
    lista.sort() = Ordena a Lista
    lista.reverse() = Inverte a lista
    enumerate = Retorna a posição e o item da posição conforma no exemplo
    
    lista =  ["maça", "banana", "morango", "uva"]
    
    for i, fruta in enumerate(lista):
        print("Posição:", i, " - Fruta:", fruta)
    
    sum(lista) = Soma os elementos da lista 
    len(lista) = Quantidade de elementos da lista 
    max(lista) = Maior elemento da lista
    min(lista) = Menor elemento da lista 
    lista.count(x) = Retorna quantas vezes o elemento x aparece na lista
    extend(listax) = Acrescenta os elementos da listax na lista original
    
   Tupla (),  é uma coleção de objstos python separados por Vírgulas. 
   Objetos aninhados e repetição, mas uma tupla e Imutavel, ao contrario de lista que são mutaveis
   Tuplas são imutaveis e tem menos funcionalidades.
   
    Conversão de Tuplas e listas
    
    litsa = [1,2,3,4,5]
    Converte para Tupla
    tupla = tuple(lista)
        print (tupla)
    Converte para lista   
    Nova_lista = list(tupla)
        print(nova_lista)
    
    Conjunto {}
    O conjunto e um tipo de dados sem elementos duplicados
    Usado para encontrar elementos únicos
    Usado para unir operações
    
    Dicionário 
    Em python e uma Coleção não ordenada de valores de dados
    É uma lista que podemos acessar seus elementos atraves de strings.
    Ex:
    Keys       Valeus 
    'a' ->     'alpha'
    'o' ->     'omega'
    'g' ->     'gamma'
    dict
    
    Dicionário contém Chave :  par de Valor.
    O valor da chave é fprnecido no dicionário para torná-lo mais otimizado.
    Ex :
    dict_estados = {"MG":"Minas Gerais","SP" : "São Paulo" }
        print(dict_estados["MG"])

"""
"""

    Criando uma função
    forma geral:

        def nome_função( < lista de parâmetros > ):
                    corpo da função
        return expressão
        
    Forma Geral Procedimento
    
       def nome_função( < lista de parâmetros > ):
                    corpo da função
        
"""