## Problema 5 - Contagem regressiva seletiva

# Criando entrada do número n
n = int(input("Digite um número(maior ou igual a 0): "))

# Definindo n como sendo ele mesmo + 1, para na hora da repetição também considerar ele
n = n+1

# Criando condição para validar se o n é maior ou igual a 0
if n >= 0:
    # Criando laço de repetição para quando o n for maior que 0
    while n > 0:
        # Enquanto o n for maior que 0, continue diminuindo o n por 1
        n = n - 1

        # Criando condição para colocar que um número é divisível por 5 ao seu lado, caso o mesmo seja divisível por 5 e maior que 0
        if n > 0 and n % 5 == 0:
            print(f'{n} é divisível por 5')

        # Imprime o próprio número caso a condição anterior não tenha sido atendida
        else:
            print(n)