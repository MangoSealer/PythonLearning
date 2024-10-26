"""
Erros Comuns em Python:

Erro de Sintaxe(SyntaxError)
Errou algo na Sintaxe

Erro de nome(NameError)
Errou o nome ou chamou alguma função / variavel que não existe

Erro de tipo(TypeError)
Tentou realizar uma operação com dois tipos de dados diferentes, por exemplo int e str

Erro de Índice(IndexError)
Tentou acessar um índice fora do intervalo
"""

'''
Manejo de Exceções:

Manejo de exceções é quando você prevê que um erro pode acontecer e especifica algo pra acontecer
caso esse erro especifico possa ocorrer em um bloco especifico.

O manejo é divido em blocos, o primeiro bloco vai ser o possivel bloco que vai gerar um erro, 
Começa usando o seguinte comando (?) uma linha acima do bloco
try:

Nele vai enquadrar toda a operação, como por exemplo
resultado = 10 / 0
print(resultado)
Seguindo, o segundo bloco onde você vai mencionar qual / quais possiveis erros podem ocorrer no 
bloco try seguindo a seguinte Sintaxe

except (possivel erro com a sintaxe certa)
e em seguida o print com qual mensagem vai acontecer se de fato o erro do bloco try acontecer, segue exemplo:

except ZeroDivisionError: 
print("Erro: Divisão por zero")

Existe um terceiro bloco, que vai ser executado sempre, mesmo se não acontecer nenhum erro no bloco try.
É normalmente utilizado para realizar tarefas de limpeza ou liberação de recursos.
A Sintaxe é a mesma do bloco Try
finally:

bloco de exemplo de uso:
def processar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")
        dados = arquivo.read()
        # Processa dados
    except FileNotFoundError:
        print("Arquivo não encontrado")
    finally:
        print("Finalizando operação...")
        arquivo.close()  # nesse caso vai fechar o arquivo independentemente de erros apos o final da função


'''

"""
Nesse caso abaixo:

def funcao():
    if condicao:
        raise Exception("Descrição do erro")
# condição não existe, logo, a linha abaixo não vai fazer nada, então a função vai seguir para o bloco try

try:
    funcao()
except Exception as e: 
# nesse caso, |except| cria o bloco, |Exception| e coleta qualquer erro tipo exception que ocorreria
|as e| coleta o erro e guarda na variável e, na forma de string
    print(f"Erro: {str(e)}")
# aqui vamos ter o output "Erro: name 'condicao' is not defined"
"""