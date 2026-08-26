## Problema 10 - Função de classificação numérica

# Criando função classificar_numero(Com parâmetro numero)
def classificar_numero(numero):
    # Criando condição caso o numero seja maior que 0 e divisível por 2
    if numero > 0 and numero % 2 == 0:
        # Retorna o resultado positivo e par
        return 'positivo e par'

    # Criando condição caso o numero seja maior que 0 e não divisível por 2
    elif numero > 0 and numero % 2 != 0:
        # Retorna o resultado positivo e ímpar
        return 'positivo e ímpar'

    # Criando condição caso o numero seja menor que 0 e divisível por 2
    elif numero < 0 and numero % 2 == 0:
        # Retorna o resultado negativo e par
        return 'negativo e par'

    # Criando condição caso o numero seja menor que 0 e não divisível por 2
    elif numero < 0 and numero % 2 != 0:
        # Retorna negativo e ímpar
        return 'negativo e ímpar'

    # Criando condição caso o numero seja igual a 0
    elif numero == 0:
        # Retorna o resultado zero
        return 'zero'

# Criando entrada numero
numero = int(input("Digite um número: "))

# Criando variável resultado com valor sendo a função
resultado = classificar_numero(numero)

# Imprimindo o resultado(Como foi usado return dentro da função, ao imprimir ela vai retornar o valor que atendeu uma das condições)
print(resultado)