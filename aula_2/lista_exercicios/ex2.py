## Problema 2 — Ano bissexto: o caso 1900

ano = int(input("Digite um ano: "))

classificacao = ""

def classificar_ano():
    if ano % 400 == 0:
        classificacao = "Bissexto"
        return classificacao
    
    elif ano % 100 == 0 and ano % 400 != 0:
        classificacao = "não bissexto"
        return classificacao
    
    elif ano % 4 == 0 and ano % 100 != 0:
        classificacao = "bissexto"
        return classificacao
    
    else:
        classificacao = "não bissexto"
        return classificacao

print(f'Ano: {ano}. Classificação: {classificar_ano()}')