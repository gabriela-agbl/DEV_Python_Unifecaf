## Problema 6 - Soma de múltiplos sem divisor zero

# Criando entradas do limite e divisor
limite = int(input("Digite um limite(maior ou igual a 1): "))
divisor = int(input("Digite um divisor(diferente de 0): "))

# Criando variável do acumulador, iniciando como 0
acumulador = 0

# Criando condição para validar se o limite é maior ou igual a 1 e divisor é diferente de 0
if limite >= 1 and divisor != 0:
    # Criando laço em que para cada número dentro do intervalo de 1 e limite + 1(Para também pegar o limite)
    for numero in range(1,limite+1):
        # Criando condição para o número sendo divisível pelo divisor
        if numero % divisor == 0:
            # Adicionando o número no acumulador para fazer a soma incremental
            acumulador += numero

            # Imprimindo o número atual do laço
            print(f'{numero}')

# Imprimindo a soma final do acumulador
print(f'Soma: {acumulador}')