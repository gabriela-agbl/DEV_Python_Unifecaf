## Problema 2 — Ano bissexto: o caso 1900

ano = int(input("Digite um ano: "))

classificacao = ""

def classificar_ano():
    if ano % 400 > 0:
        classificacao = "Bissexto"
        return classificacao
    
    elif ano % 100 > 0 and ano % 400 is None:
        classificacao = "não bissexto"
        return classificacao
    
    elif ano% 4 > 0 and ano % 100 is None:
        classificacao = "bissexto"
        return classificacao
    
    else:
        classificacao = "não bissexto"
        return classificacao