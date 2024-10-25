print("Hello World!")
print("-----------")

idade1 = 25
print(idade1)
# no geral, não é necessário uso de ;, não é necessário definir o tipo de dados da variável
# somente em casos especiais, no geral, python decide sozinho
print("primeira variavel criada e idade")
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
print("teste loop |for e in| c/ frutas")
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

for numero in range(6):
    print(numero * 2)
    # |for| cria a variavel número, |in| cria o loop e |range| seta o intervalo em que essa conta vai ser feita
    # no caso, como é um loop cada vez a conta vai ser feita, assumindo um valor dentro do range e fazer a conta * 2,
    # como declarado no print, sempre excluindo o último número do range (?)
    # no caso o output vai ser 1*2, 2*2, etc, até o final do range que vai ser 5
print("loop for, in simples")
print("-----------")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

# |contador = 0| = variavel sendo declarada
# while True: vai rodar o while *indefinidamente*
# print sem ""
# |contador += 1| vai adicionar 1 a contagem a cada print do loop
# if contador == (= declarar == comparar) 5
# break em conjunto com o if acima pra parar o while True, que seria infinito
print("teste loop indefinido 'while True' c/ break")
print("-----------")

for contagem in range(10):

    if contagem % 2 == 0:
        continue
    print(contagem)

# for contagem in range(10): seta o loop, o (10) é a mesma coisa que (0, 10)
# if contagem % 2 == 0: usa o operador modulo (% ≠ /) pra ver se o número é par
# % verifica qual o resto da conta do segundo operando - o primeiro, ex.
# 5 % 2 = 1, pois, 5 - 2 - 2 = 1, ou, 4 % 2 = 0, pois 4 - 2 - 2 = 0
# 7 % 4 = 3, pois, 7 - 4 = 3
# |continue| linkado ao if pula essa interação, no caso desse bloco, tudo que for % 2 == 0 vai ser pulado
# nesse caso, print(contagem) vai imprimir numeros impares de 0 até 9
print("teste loop if, operador módulo % e continue")
print("-----------")

for i in range(5):
    pass
# pass não faz nada (?) usado pra quando quer criar um bloco e deixar reservado pra mais tarde (?)
print("teste pass")
print("-----------")

frutas = ["maçã", "banana", "laranja"]
# [ cria uma lista podendo ser acessada posteriormente
print(frutas[0])
# print (frutas) acessa a lista, [0] acessa o primeiro item da lista, no caso, maçã
print(frutas[-1])
# [-1] acessa o ultimo item da lista, [-2] acessaria o penúltimo...
print("teste lista e indice")
print("-----------")

# Sintaxe = lista.metodo

frutas = ['maçã', "banana", "laranja", "pera"]
# lista


print(frutas)
# |.append| adiciona um elemento ao final da lista
print("método .append")
print("-----------")

frutas.insert(1, "uva")
print(frutas)
# |.insert (indice, elemento) adiciona um elemento em uma posição especifica da lista
print("método .insert")
print("-----------")

frutas.remove("banana")
print(frutas)
# |.remove| remove a primeira incidência do elemento mencionado
print("método .remove")
print("-----------")

fruta_removida = frutas.pop(2)
# |fruta_removida| tá criando uma variavel, |frutas.pop| remove um item especifico com base no indice |(2)|
print(frutas)
# imprimindo a lista normalmente
print(fruta_removida)  # Imprime "laranja"
# imprimindo a variavel que acabou de criar
print("método .pop")
print("-----------")

frutas.sort()
print(frutas)
# organiza a lista em ordem crescente
print("método. sort")
print("-----------")

frutas.reverse()
print(frutas)
# inverte a ordem atual dos itens da lista
print("método .reverse")
print("-----------")

frutas.sort(reverse=True)
print(frutas)
# |.sort(reverse=True)| faz o mesmo que |.sort()|, mas em ordem decrescente
print("método .sort descendente")
print("-----------")

# lista de compreensão é quando você pega uma lista normal e aplica uma condição ou transformação geralmente em uma
# ou poucas linhas

# Exemplo:

numeros = [1, 2, 3, 4, 5]  # lista normal sendo criada
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
# nessa linha tá transformando em lista de compreensão, |x ** 2| tá usando o operador exponenciador, que
# é igual a exponenciação normal (2 ** 3 = {2 x 2 x 2 = 8}),
# logo em seguida um loop tá sendo criado |for x (variavel sendo criada, usando a condição mencionada antes)|
# |in numeros| ta utilizando a lista mencionada acima, |if x % 2 == 0| tá testando se o numero é par
print(quadrados)
print("lista de compreensão")
print("-----------")

# Tuplas

ponto = (3, 4)
# [] cria uma lista, onde os valores são mutáveis, () cria uma Tupla, que não é mutável
print(ponto[0])
# [0] sempre vai ser o indice que vai pra um item de uma lista ou Tupla
print("introdução a Tuplas")
print("-----------")

Minha_tupla = (1, 2, 3, 2, 4, 2)

print(Minha_tupla.count(2))
# |(Tupla.count(index))| diz quantas vezes o item aparece na tupla
print(Minha_tupla.index(2))
# |(Tupla.index(index))| diz qual numero do index o item aparece a primeira vez na tupla
print(Minha_tupla.__len__())
# |(Tupla.len())| short for lenght
print("métodos de Tuplas")
print("-----------")

# Dicionários

pessoa = {"nome": "João", "idade": 25, "cidade": "Osasco"}
# {} cria um dicionario, separa as chave-valor com :, sempre utilizando " "
print(pessoa["nome"])
# sintaxe basica pra dar o output, print(dicionario["chave"])
print(pessoa["idade"])
print(pessoa["cidade"])
print("dicionários")
print("-----------")

# outra forma de dar o output de um dicionario é usar o metodo get(), usando a sintaxe basica
# caso não exista a chave vai gerar um erro no código, caso o metodo get() não
# encontre a chave ele vai retornar "None", mas também é possivel selecionar a mensagem de retorno
# caso não encontre a chave, exemplos e sintaxe do metodo:

print(pessoa.get("nome"))
# print normal com valor valido
print(pessoa.get("altura"))
# print com valor invalido, suposto a retornar None
print(pessoa.get("altura", "Inválido"))
print("dicionários c/ metodo get()")
print("-----------")

# métodos de dicionários

print(pessoa.keys())
# retorna todas as 'chaves' ou 'titulos' do dicionário

print(pessoa.values())
# retorna todos os 'valores' do dicionário

print(pessoa.items())
# retorna todos os pares 'chave-valor' do dicionário

pessoa.update({"profissao": "Engenheiro"})
# adiciona uma chave-valor ao dicionário
print(pessoa)
print("métodos de dicionários")
print("-----------")

# Conjuntos (é igual lista ou Tupla, mas com suas peculiaridades)

frutas = {"maçã", "banana", "laranja"}
# sintaxe basica pra criar um conjunto

numeros = set([1, 2, 3, 4, 5])
# sintaxe para criar um conjunto utilizando a função set( )


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# operadores de conjuntos

uniao = (conjunto1 | conjunto2)
# uniao criando um novo conjunto, | vai unir os dois
# o 3 nao vai repetir no output pq nos conjuntos valores nao podem repetir
print(uniao)

intersecao = (conjunto1 & conjunto2)
# operador & retorna valores que os dois conjuntos tenham em comum
print(intersecao)

diferenca = conjunto1 - conjunto2
# faz a subtração dos itens do segundo que já estão no primeiro conjunto
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2
# cria um conjunto somente com as diferenças entre os conjuntos, se houver elementos presente
# nos dois  vai ser ignorado
print(diferenca_simetrica)
print("operadores de conjuntos")
print("-----------")

# métodos de conjuntos

# noinspection PyRedeclaration
frutas = {"maçã", "banana", "laranja"}
# conjunto setado

frutas.add("pera")
# adiciona o valor no slot [1]
print(frutas)

frutas.remove("banana")
# metodo pra remover valores do conjunto, caso o valor nao exista vai gerar um erro
print(frutas)

frutas.discard("uva")
# outro metodo pra remover valores do conjunto, nese não vai retornar erro caso o valor não exista no conjunto
print(frutas)

frutas.clear()
# limpa a variável
print(frutas)
print("métodos de conjuntos")
print("-----------")

print("fim da parte 1")