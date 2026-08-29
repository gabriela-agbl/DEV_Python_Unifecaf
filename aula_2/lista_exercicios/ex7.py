## Problema 7 - Fatorial e os casos 0! e 1!

# Criando entrada do número n
n = int(input("Digite um número(maior ou igual a 0): "))

# Criando variável do acumulador, com valor inicial 1(Não começa com 0, pois, ele posteriormente vai ser usado em uma multiplicação para calcular o fatorial do n)
acumulador = 1

# Criando condição para validar se o n é maior ou igual a 0
if n >= 0:
    # Criando laço em que para cada i dentro do intervalo de 1 e n+1(Para também considerar o próprio n)
    for i in range(1,n+1):
        # Inserindo no acumulador a sua multiplicação com cada i de forma incremental
        acumulador *= i

        # Imprimindo cada elemento do intervalo
        print(i)

# Imprimindo valor final do acumulador(Valor do n!)
print(acumulador)

# MICRODEFESA: Iniciar o acumulador em 0 zeraria o resultado, pois, qualquer multiplicação por 0 dá 0, por isso começa em 1