# Problema 1 — Classificação da média nas fronteiras

# Criando entradas das notas
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

# Criando variável para definir a classificação
classificacao = ""

# Criando variável com o valor da média(como seu cálculo é feito)
media = round((nota1 + nota2 + nota3)/3)

# Criando a condição para a classificação reprovado, ou seja, se a média for menor que 4
if media < 4.0:
    classificacao = "Reprovado"

# Criando a condição para a classificação recuperação, ou seja, se a média for maior ou igual a 4 e menor que 6
elif media >= 4.0 and media < 6.0:
    classificacao = "Recuperação"   

# Criando a condição para a classificação aprovado, ou seja, se a média for maior ou igual a 6 e menor que 9
elif media >= 6.0 and media < 9.0:
    classificacao = "Aprovado"

# Criando a condição para a classificação aprovado com destaque, ou seja, se a média for maior ou igual a 9
elif media >= 9.0:
    classificacao = "Aprovado com destaque"

# Imprimindo a média e sua classificação
print(f"A média foi: {media:2f}. A classificação foi: {classificacao}")