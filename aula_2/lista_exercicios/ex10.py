## Problema 10 - Função de classificação numérica

def classificar_numero(numero):
    if numero > 0 and numero % 2 == 0:
        return 'positivo e par'

    elif numero > 0 and numero % 2 != 0:
        return 'positivo e ímpar'

    elif numero < 0 and numero % 2 == 0:
        return 'negativo e par'

    elif numero < 0 and numero % 2 != 0:
        return 'negativo e ímpar'

    elif numero == 0:
        return 'zero'

numero = int(input("Digite um número: "))

resultado = classificar_numero(numero)

print(resultado)