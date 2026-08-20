## Problema 8 - Sequência definida por passo

inicio = int(input("Digite um início: "))
passo = int(input("Digite um passo: "))
quantidade = int(input("Digite uma quantidade(maior ou igual a 1): "))

acumulador = inicio
acumulador_qtd = 1

print(inicio)

while acumulador_qtd < quantidade: 
    acumulador = acumulador + passo
    acumulador_qtd = acumulador_qtd + 1
    print(acumulador)