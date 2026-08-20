## Problema 2 — Ano bissexto: o caso 1900

ano = int(input("Digite um ano: "))

classificacao = ""

if ano % 400 == 0:
    classificacao = "Bissexto"
 
elif ano % 100 == 0 and ano % 400 != 0:
    classificacao = "não bissexto"
    
elif ano % 4 == 0 and ano % 100 != 0:
    classificacao = "bissexto"
    
else:
    classificacao = "não bissexto"
        
print(f'Ano: {ano}. Classificação: {classificacao}')