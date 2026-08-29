## Problema 12 - Potência por multiplicações sucessivas

# Criando função potencia(Com parâmetros base e expoente)
def potencia(base, expoente):
    # Criando variável contador com valor 1
    contador = 1
    # Criando variável resultado com valor 1
    resultado = 1

    # Criando laço para se repetir enquanto o contador for menor ou igual ao expoente
    while contador <= expoente:
        # Inserindo dentro de resultado ele mesmo multiplicado pela base
        resultado = resultado*base

        # Inserindo dentro de contador ele mesmo + 1
        contador = contador + 1

    # Retornando resultado potencia ({base}, {expoente}) = {resultado}
    return f'potencia({base}, {expoente}) = {resultado}'

# Criando entradas base e expoente
base = float(input("Digite um número: "))
expoente = int(input("Digite um número(maior ou igual a 0): "))

# Criando condição para validar se o expoente é maior ou igual a 0
if expoente >= 0:
    # Criando variável potencia com valor sendo a função
    potencia = potencia(base, expoente)

    # Imprimindo a potencia(Como foi usado return dentro da função, ao imprimir ela vai retornar o valor que foi retornado)
    print(potencia)

# MICRODEFESA: O resultado inicial precisa ser 1 para que possa realizar as multiplicações e, no caso de expoente 0, retornar o resultado 1(já que no while a multiplicação apenas ocorre se o contador(1) for menor ou igual ao expoente)