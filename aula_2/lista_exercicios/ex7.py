## Problema 7 - Fatorial e os casos 0! e 1!

n = int(input("Digite um número(maior ou igual a 0): "))

acumulador = 1

for i in range(1,n+1):
    acumulador *= i

    print(i)

print(acumulador)