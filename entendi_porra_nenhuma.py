"""

Quando escrevemos programas, é comum nos depararmos com situações inesperadas ou erros durante a execução.
Python fornece um mecanismo para lidar com esses erros de maneira controlada utilizando o tratamento de exceções.
Isso nos permite capturar e lidar com erros específicos sem que o programa pare abruptamente.
Erro de sintaxe (SyntaxError)
Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.
def minha_funcao() # Faltam os dois pontos
    print("Olá")

Erro de nome (NameError)
Ocorre quando se faz referência a uma variável ou função que não foi definida.

print(variavel_nao_definida)

Erro de tipo (TypeError)
Ocorre quando se realiza uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.
resultado = 5 + "10"

Erro de índice (IndexError)
Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.
lista = [1, 2, 3]
print(lista[3])  # O índice 3 está fora do intervalo"""

"""6.1. Manejo de exceções

O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try,
except e opcionalmente finally.

Try
O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de
 execução é transferido para o bloco except correspondente.

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

Except
O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos
blocos except para lidar com diferentes tipos de exceções.


try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")


Finally
O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não.
É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção"""

"""6.2. Exceções personalizadas

Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas.
Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde
da classe base Exception ou de uma de suas subclasses.

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

Neste exemplo, define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e, se for
    satisfeita, gera-se uma exceção utilizando a declaração raise. Em vez de criar uma classe personalizada,
    utiliza-se diretamente a classe base Exception para gerar a exceção.

Depois, utiliza-se um bloco try-except para capturar e lidar com a exceção.
A variável e é utilizada para acessar a descrição do erro fornecida ao gerar a exceção.

O tratamento de erros e exceções é uma parte fundamental da programação em Python.
Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.

Quando ocorre um erro no seu código, o Python gera uma exceção. Ao utilizar blocos try-except,
você pode capturar e lidar com essas exceções de maneira adequada. Pode especificar diferentes blocos except
para lidar com diferentes tipos de exceções e realizar ações específicas em cada caso.

Além disso, o bloco finally permite executar código de limpeza ou liberação de recursos,
independentemente de ter ocorrido uma exceção ou não. Isso é útil para garantir que certas ações
sejam sempre realizadas, como fechar arquivos ou conexões de banco de dados."""

"""A função input() sempre retorna uma cadeia de texto.
 Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, 
 deve realizar uma conversão explícita utilizando funções como int() ou float()."""

"https://lms.santanderopenacademy.com/courses/822/pages/7-dot-1-leitura-e-escrita-de-arquivos?module_item_id=6705"


