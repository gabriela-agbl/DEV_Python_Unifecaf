## Problema 11 - Calculadora e retorno None

def calcular(a, b, operacao):
    if operacao == '+':
        return a + b
    
    elif operacao == '-':
        return a - b

    elif operacao == '*':
        return a * b
    
    elif operacao == '/':
        if b == 0:
            return None
        
        return a / b
    
    elif operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/':
        return None

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
operacao = str(input("Digite uma operação(+, -, *, /): "))

resultado = calcular(a, b, operacao)

if resultado == None:
    print("Operação inválida")
else:
    print(resultado)