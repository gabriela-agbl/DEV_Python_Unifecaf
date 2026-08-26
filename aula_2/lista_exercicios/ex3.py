## Problema 3 - Maior e menor com empates parciais

# Criando entradas dos 3 números
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

# Criando variável do maior número
maior_valor = ''

# Criando variável do menor número
menor_valor = ''

# Criando variável para a classificação
classificacao = ''

# Criando condição caso todos os números sejam iguais
if a == b and a == c and b == c:
  classificacao = 'Todos iguais' 

# Criando condição caso o a seja o maior número e o c o menor número
elif a > b and a > c and b > c:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o b seja o maior número e o c o menor número
elif b > a and b > c and a > c:
  maior_valor = b
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o c seja o maior número e o b o menor número
elif c > a and c > b and a > b:
  maior_valor = c
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o a seja o maior número e o b o menor número
elif a > b and a > c and c > b:
  maior_valor = a
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o b seja o maior número e o a o menor número
elif b > a and b > c and c > a:
  maior_valor = b
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o c seja o maior número e o a o menor número
elif c > a and c > b and b > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o a seja igual ao b e maior que o c
elif a == b and a > c:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o a seja igual ao c e maior que o b
elif a > b and a == c:
  maior_valor = a
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o c seja igual ao b e maior que o a
elif c == b and c > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o a seja igual ao b e menor que o c
elif a == b and c > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o a seja igual ao c e menor que o b
elif a == c and b > a:
  maior_valor = b
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Criando condição caso o c seja igual ao b e menor que o a
elif c == b and a > b:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

# Imprimindo a classificação
print(classificacao)