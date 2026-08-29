## Problema 2 — Ano bissexto: o caso 1900

# Criando entrada do ano
ano = int(input("Digite um ano: "))

# Criando variável para a classificação
classificacao = ""

# Criando a condição para a classificação de bissexto caso o ano for divisível por 400
if ano % 400 == 0:
    classificacao = "Bissexto"

# Criando a condição para a classificação de bissexto caso o ano for divisível por 4 mas não por 100
elif ano % 4 == 0 and ano % 100 != 0:
    classificacao = "bissexto"

# Criando a condição para a classificação de não bissexto caso o ano for divisível por 100 mas não por 400
elif ano % 100 == 0 and ano % 400 != 0:
    classificacao = "não bissexto"

# A classificação caso nenhuma das outras condições for atendida
else:
    classificacao = "não bissexto"

# Imprimindo o ano e sua classificação    
print(f'Ano: {ano}. Classificação: {classificacao}')

# MICRODEFESA: Testar só ano % 4 == 0 no caso do ano 1900 estaria errado, pois, 1900 é divisível por 4 e 100 mas não por 400, ou seja, seguindo a regra e usando and, 1900 cumpre as condições de ano % 100 == 0 and ano % 400 != 0(não bissexto)