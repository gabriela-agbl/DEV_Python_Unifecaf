## Problema 4 - Intervalo e paridade

numero = int(input('Digite um número: '))

flag_intervalo = False
flag_par = False
flag_regras = False

def classificar_numero():
    if numero % 2 == 0 and numero in range(10,50):
        flag_regras = True
        return print(f'Atende ás duas regras: {flag_regras}')

    elif numero in range(10,50):
        flag_intervalo = True
        return print(f'Está no intervalo: {flag_intervalo}')

    elif numero % 2 == 0:
        flag_par = True
        return print(f'É par: {flag_par}')

print(classificar_numero())