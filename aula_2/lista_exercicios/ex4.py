## Problema 4 - Intervalo e paridade

# Criando entrada do número
numero = int(input('Digite um número: '))

# Criando variáveis booleanas com valor inicial False
flag_intervalo = False
flag_par = False
flag_regras = False

# Criando condição para a flag_intervalo True, caso número esteja entre 10 e 50
if numero in range(10,50):
    flag_intervalo = True

# Criando condição para a flag_par True, caso número seja par, ou seja, divisível por 2
if numero % 2 == 0:
    flag_par = True

# Criando condição para a flag_regras True, caso número atenda as outras duas condições, ou seja, seja divisível por 2 e está entre 10 e 50
if numero % 2 == 0 and numero in range(10,50):
    flag_regras = True

# Imprimindo os valores de cada flag(True ou False)
print(f'Está no intervalo: {flag_intervalo} \nÉ par: {flag_par} \nAtende às duas regras: {flag_regras}')

# MICRODEFESA: O and exige que as duas condições sejam verdadeiras ao mesmo tempo, já o or só precisa que uma seja verdadeira para funcionar, no caso da última regra o and deve ser usado, já que exige que as outras duas regras sejam atendidas