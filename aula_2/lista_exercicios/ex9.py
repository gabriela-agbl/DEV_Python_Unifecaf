## Problema 9 - Número primo sem interrupção antecipada

n = int(input("Digite um número(maior que 1): "))

contador = 0

for i in range(1,n+1):
    if n % i == 0:
        contador = contador + 1

if contador == 2:
    print(f"{n} é primo")
elif contador > 2:
    print(f"{n} não é primo")