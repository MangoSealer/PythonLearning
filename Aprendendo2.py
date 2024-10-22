# funções
from socket import SocketIO


# resumidamente, é um bloco de código que age como um macro

def saudacao():
    # def cria uma função, saudacao é o nome da função, finaliza a sintaxe com ():
    print("Hello World!")


# logo abaixo, vai as funções da função, não esquecer da indentação
# esse print não vai estar sendo executado até a função ser chamada

saudacao()
# pra executar ou "chamar" uma função é só utilizar "função()"
print("primeira função, saudação")
print("-----------")


# parametros e argumentos em funções

def saudacao2(nome):
    # nesse caso, utiliza-se (nome) como parametro, como se fosse um espaço reservado
    # a ser preenchido quando a função for chamada
    print(f"Olá, {nome}!")
    # o "f" (f-string) permite que o {nome} seja substituido pelo nome chamado na função


saudacao2("Danilo")
print("parametros e argumentos em funções")
print("-----------")


def soma(a, b):
    # criando a função soma, dizendo que o que dá pra ser usado nela é valor A e B
    return a + b
    # dizendo o que a função vai fazer


resultado = soma(3, 4)
# variavel = função sendo chamada(valor1, valor2)
print(resultado)
print("parametros e argumentos em funções")
print("-----------")

# função lambda
# utilizada quando só vai utilizar a função uma unica vez, criada de forma rapida

quadrado = lambda x: x ** 2
# função = função tipo lambda, valor de X = X elevado a 2ª potência
print(quadrado(5))
# print (função(X))
print("função lambda")
print("-----------")


# quando uma variável é criada dentro de uma função ela é chamada
# de variável local, só pode ser utilizada dentro da função, mas quando é criada
# fora da função ela pode ser utilizada na função

def funcao():
    variavel_local = 10
    # variavel simples sendo criada
    print(variavel_local)
    # vai funcionar, já que a variavel foi criada dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)
    # também vai funcionar, já que a variavel_global não faz parte da função2


funcao()
funcao2()
print(variavel_global)
# funciona, por motivos óbvios
# print(variavel_local) não funcionaria
print("váriaveis locais e globais")
print("-----------")


def calcular_media(*numeros):
    # em (*numeros) o * remove a necessidade de dizer quantos parâmetros vão ser utilizados
    # na função, ao invés disso ele deixa em aberto essa questão
    Soma = sum(numeros)
    # Parametro soma criado, = sum(numeros) tá dizendo que ela vai somar os numeros da função e guardar em uma variavel
    quantidade = len(numeros)
    # = len vai criar uma variável com quantos valores tem no parametro
    media = Soma / quantidade
    # média é um novo parametro, depois do = é só a operação
    return media
    # return libera pra você usar e manipular o valor que vai ser o output da função


print("Média:", calcular_media(100, 50, 100))
# necessário utilizar virgula após as aspas pra declarar que acabou o texto
print("função de calcular média")
print("-----------")


def somar_3(x):
    return x + 3


print("Soma de 3 e 5 =", somar_3(5))

print("função completa pra somar + 3")
print("-----------")

Somar = lambda x: x + 3
print("Somar 3 a 10 =", Somar(10))
print("Função lambda pra somar +3")
print("-----------")

def somar (a,b):
    """ teste de docstring
    linha 2 do teste
    linha 3 do teste"""
    return a + b
# se utilizar """ """ dentro de funções, classes ou módulos vai criar uma docstring, que é basicamente
# a explicação do que o elemento em si faz

print(somar.__doc__)
# (função.doc) pra imprimir a docstring do mesmo
print("teste de docstrings")
print("-----------")


def soma_variavel(*numeros):
    total = 0
    # declarando uma variavel pra ser utilizada em seguida
    for numero in numeros:
        # loopzinho padrão
        total += numero
        # nesse loop o total, que começa em 0 nesse caso, vai ser somado a cada numero utilizado como argumento
    return total


print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))
print("função com numero variado de argumentos e loop simples for/in")
print("-----------")