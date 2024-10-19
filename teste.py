print("Hello World!")
print("-----------")




idade1 = 25
print(idade1)
# no geral, não é necessário uso de ;
print("idade")
print("-----------")




nome = "ugly bastard"
print(nome)
# necessário declarar strings com " "
print("nome")
print("-----------")




if idade1 >= 18:
    print("Você é maior de idade")
    # > =
print("if idade >=")
print("-----------")




idade2 = 15
if idade2 >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    # testa primeiro o if, se não rolar testa o else
    print("teste de if, else com idade")
print("-----------")




nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muito bom")
elif nota >= 70:
    print("Bom")
else:
    print("Precisa melhorar")
# abre a estrutura condicional com if para testar o primeiro valor,
# elif (else if) para continuar os testes, e else pra testar se nada der certo
print("nota, if, elif e else")
print("-----------")




frutas = ["maçã", "banana", "laranja"]
# variável
for fruta in frutas:
    print(fruta)
    # loop, |for fruta| cria a variável fruta, |in| executa o loop com a
    # variavel criada na primeira linha, executando cada valor da variável em uma linha
print("teste loop for e in c/ frutas")
print("-----------")




contador = 0
while contador <= 5:
    print(contador)
    contador += 1
# |contador|, variavel declarada
# enquanto a variavel for |<= 5| vai cumprir o que for solicitado abaixo no codigo
# |+=| vai acrescentar a quantidade que colocar a direita, no caso +1 a cada print
# risco de loop infinito
print("teste loop while c/ contador += 1")
print("-----------")




print("numero ?")
for numero in range(1, 6):
    print(numero * 2)
    # |for| cria a variavel número, |in| cria o loop e |range| seta o intervalo em que essa conta vai ser feita
    # no caso, como é um loop cada vez a conta vai ser feita, assumindo um valor dentro do range e fazer a conta * 2,
    # como declarado no print, sempre excluindo o último número do range (?)
    # no caso o output vai ser 1*2, 2*2, etc, até o final do range que vai ser 5




    contador = 0

    while True:

        print(contador)
        contador += 1

        if contador == 5:
            break

# variavel declarada
# while True: vai rodar o while *indefinidamente*
# print como previamente visto
# if contador == (= declarar == comparar) 5
# break pra parar o while True, que seria infinito'''

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range().
# Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %.
# Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com
# que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado,
# apenas os números ímpares serão impressos.
# ^ entender e substituir


for i in range(5):
    pass

# pass não faz nada (?) usado pra quando quer criar um bloco e deixar reservado pra mais tarde (?)


frutas = ["maçã", "banana", "laranja"]
# [ cria uma variavel tipo lista (?) podendo ser acessada posteriormente
print(frutas[0])
# print (frutas) acessa a lista, [0] acessa o primeiro item da lista, no caso, maçã
print(frutas[-1])
# [-1] acessa o ultimo item da lista, [-2] acessaria o penúltimo...


# adicionar prints antes dos printout para organizar ASAP


# metodos de listas (ask abt methods)

'''append(elemento): adiciona um elemento ao final da lista.
insert(indice, elemento): insere um elemento em uma posição específica da lista.
remove(elemento): remove a primeira ocorrência de um elemento na lista.
????pop(indice): remove e retorna o elemento em uma posição específica da lista.
sort(): ordena os elementos da lista em ordem ascendente.
reverse(): inverte a ordem dos elementos na lista.'''
# ^ organizar

frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

# ^ entender, organizar


# Listas de compreensão
# As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente.
# Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

'''nova_lista = [expressão for elemento in sequência if condição]
Exemplo:

números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]
Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números.
 A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.'''

# ^ kkkkkkkkkkk alguém me mata por favor


ponto = (3, 4)
# entre parênteses deixa de ser lista, que é mutavel, pra Tupla (?) que é algo imutável
print(ponto[0])
# [0] sempre vai ser o "operador" que vai selecionar um item de uma lista ou Tupla


'''count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.'''
# ^ entender, organizar, transcrever

Minha_tupla = 1, 2, 3, 2, 4, 2

print(Minha_tupla.count(2))
print(Minha_tupla.index(2))
print(Minha_tupla.__len__())

pessoa = {"nome": "João", "idade": 25, "cidade": "Osasco"}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])
# tf is method get ()?


'''Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

keys(): retorna os "títulos" do dicionario
values(): retorna os "valores" do dicionario
items(): retorna uma visualização de todos os pares chave-valor do dicionário.
update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
Exemplo:'''

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.update({"profissao": "Engenheiro"})
print(pessoa)

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
'''Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).'''

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
# alguém me mata por favor, continuando...


'''Métodos de conjuntos 
conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos 
Alguns métodos comuns são:

add(elemento): adiciona um elemento ao conjunto.
remove(elemento): remove um elemento do conjunto
Se o elemento não existir, gera um erro.
discard(elemento): remove um elemento do conjunto se estiver presente.Se o elemento não existir, não faz nada.
clear(): remove todos os elementos do conjunto.
Exemplo:'''

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()

'''As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e
 manipular dados em nossos programas. As listas são úteis para coleções ordenadas e mutáveis, as tuplas para 
 coleções ordenadas e imutáveis, os dicionários para armazenar pares de chave valor e os conjuntos para coleções
  não ordenadas de elementos únicos.'''


def multiplicar(a, b):
    return a * b
print(multiplicar)


resultado = multiplicar(5, 3) + multiplicar(2, 4)