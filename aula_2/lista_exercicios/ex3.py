## Problema 3 - Maior e menor com empates parciais

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

maior_valor = ''
menor_valor = ''
classificacao = ''

if a == b and a == c and b == c:
  classificacao = 'Todos iguais' 

elif a > b and a > c and b > c:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif b > a and b > c and a > c:
  maior_valor = b
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif c > a and c > b and a > b:
  maior_valor = c
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif a > b and a > c and c > b:
  maior_valor = a
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif b > a and b > c and c > a:
  maior_valor = b
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif c > a and c > b and b > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif a == b and a > c:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif a > b and a == c:
  maior_valor = a
  menor_valor = b

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif c == b and c > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif a == b and c > a:
  maior_valor = c
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif a == c and b > a:
  maior_valor = b
  menor_valor = a

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

elif c == b and a > b:
  maior_valor = a
  menor_valor = c

  classificacao = f'Maior: {maior_valor}, Menor: {menor_valor}'

print(classificacao)