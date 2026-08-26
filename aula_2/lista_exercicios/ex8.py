## Problema 8 - Sequência definida por passo

# Criando entradas do inicio, passo e quantidade
inicio = int(input("Digite um início: "))
passo = int(input("Digite um passo: "))
quantidade = int(input("Digite uma quantidade(maior ou igual a 1): "))

# Criando variável acumulador, com valor igual a inicio(Para separar um do outro, o inicio será usado antes do laço)
acumulador = inicio
# Criando variável acumulador_qtd, com valor inicial 1
acumulador_qtd = 1

# Criando condição para validar se a quantidade é maior ou igual a 1
if quantidade >= 1:
    # Imprimindo valor inicial antes de começar o laço
    print(inicio)

    # Criando laço que se repete enquanto o acumulador_qtd for menor que a quantidade
    while acumulador_qtd < quantidade: 
        # Inserindo dentro do acumulador ele mesmo + o passo
        acumulador = acumulador + passo
        # Inserindo dentro do acumulador_qtd ele mesmo + 1
        acumulador_qtd = acumulador_qtd + 1

        # Imprimindo o resultado do acumulador a cada passo
        print(acumulador)