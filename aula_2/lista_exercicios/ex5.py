## Problema 5 - Contagem regressiva seletiva

n = int(input("Digite um número(maior ou igual a 0): "))

n = n+1

if n >= 0:
    while n > 0:
        n = n - 1

        if n > 0 and n % 5 == 0:
            print(f'{n} é divisível por 5')

        else:
            print(n)