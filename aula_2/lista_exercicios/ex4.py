## Problema 4 - Intervalo e paridade

numero = int(input('Digite um número: '))

flag_intervalo = False
flag_par = False
flag_regras = False

if numero in range(10,50):
    flag_intervalo = True

if numero % 2 == 0:
    flag_par = True

if numero % 2 == 0 and numero in range(10,50):
    flag_regras = True

print(f'Está no intervalo: {flag_intervalo} \nÉ par: {flag_par} \nAtende às duas regras: {flag_regras}')