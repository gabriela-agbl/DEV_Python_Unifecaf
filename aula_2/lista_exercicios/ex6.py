## Problema 6 - Soma de múltiplos sem divisor zero

limite = int(input("Digite um limite(maior ou igual a 1): "))
divisor = int(input("Digite um divisor(diferente de 0): "))

acumulador = 0

for numero in range(1,limite+1):
    if numero % divisor == 0:
        acumulador += numero

        print(f'{numero}')

print(f'Soma: {acumulador}')