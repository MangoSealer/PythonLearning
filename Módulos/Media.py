def calcular_media(*numeros):
    """sintaxe pra usar = print("Média:", calcular_media(100, 50, 100))"""

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

