# Problema 1 — Classificação da média nas fronteiras

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

classificacao = ""

media = round((nota1 + nota2 + nota3)/3)

if media < 4.0:
    classificacao = "Reprovado"

elif media >= 4.0 and media < 6.0:
    classificacao = "Recuperação"   

elif media >= 6.0 and media < 9.0:
    classificacao = "Aprovado"
    
elif media >= 9.0:
    classificacao = "Aprovado com destaque"

print(f"A média foi: {media:2f}. A classificação foi: {classificacao}")