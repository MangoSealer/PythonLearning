# função input
# essa função solicita informações pro usuário durante a execução do programa

nome = input("Insira seu nome: ")
# variavel = função input("Texto a ser exibido durante a solicitação do dado")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
# + nome + vai puxar o que você retornar ao sistema anteriormente
print("Você tem " + idade + " anos.")
print("função input")
print("-----------")


# por padrão, input sempre retorna str, se quiser usar int ou float precisa converter

idade = int(input("Insira sua idade: "))
# convertendo str pra int pra manipular a idade na estrutura condicional abaixo

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")

print("estrutura condicional c/ input")
print("-----------")