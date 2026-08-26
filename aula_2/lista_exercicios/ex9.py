## Problema 9 - Número primo sem interrupção antecipada

# Criando entrada do número n
n = int(input("Digite um número(maior que 1): "))

# Criando variável contador, com valor inicial 0
contador = 0

# Criando condição para validar se o n é maior que 1
if n > 1:
    # Criando laço em que para cada i dentro do intervalo de 1 e n+1
    for i in range(1,n+1):
        # Criando condição caso o n seja divisível pelo i
        if n % i == 0:
            # Inserindo dentro do contador ele mesmo + 1
            contador = contador + 1

    # Criando condição, fora do laço, caso o resultado final do contador seja igual a 2
    if contador == 2:
        # Imprimindo o resultado do n como primo
        print(f"{n} é primo")

    # Criando condição, fora do laço, caso o resultado final do contador seja maior que 2
    elif contador > 2:
        # Imprimindo o resultado do n como não primo
        print(f"{n} não é primo")