## Problema 11 - Calculadora e retorno None

# Criando função calcular(Com parâmetros a, b e operacao)
def calcular(a, b, operacao):
    # Criando condição caso o operador seja igual a '+'
    if operacao == '+':
        # Retorna o resultado a + b
        return a + b

    # Criando condição caso o operador seja igual a '-'
    elif operacao == '-':
        # Retorna o resultado a - b
        return a - b

    # Criando condição caso o operador seja igual a '*'
    elif operacao == '*':
        # Retorna o resultado a * b
        return a * b

    # Criando condição caso o operador seja igual a '/'
    elif operacao == '/':
        # Criando condição caso o b seja igual a 0(Valida divisões por 0)
        if b == 0:
            # Retorna o resultado None
            return None

        # Retorna o resultado a / b caso b não seja 0
        return a / b

    # Criando condição caso nenhuma das operações válidas sejam atendidas
    elif operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/':
        # Retorna o resultado None
        return None

# Criando entradas de a, b e operacao
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
operacao = str(input("Digite uma operação(+, -, *, /): "))

# Criando variável resultado com valor sendo a função
resultado = calcular(a, b, operacao)

# Criando condição caso o resultado seja igual a None
if resultado == None:
    # Imprimindo que a operação é inválida para valor retornado None na função
    print("Operação inválida")

# Criando condição caso a última condição não tenha sido atendida
else:
    # Imprimindo o resultado(Como foi usado return dentro da função, ao imprimir ela vai retornar o valor que atendeu uma das condições)
    print(resultado)