## Problema 12 - Potência por multiplicações sucessivas

def potencia(base, expoente):
    contador = 1
    resultado = 1

    while contador <= expoente:
        resultado = resultado*base

        contador = contador + 1

    return f'potencia({base}, {expoente}) = {resultado}'

base = float(input("Digite um número: "))
expoente = int(input("Digite um número(maior ou igual a 0): "))

potencia = potencia(base, expoente)

print(potencia)