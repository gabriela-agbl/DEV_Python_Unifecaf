# Exit Check — Individual

## Q1
```python
def buscar_usuario(email: str) -> Usuario | None:
    ...
```
O que `Usuario | None` comunica?

Comunica que a função pode retornar o resultado de Ususario ou não retornar nada, com o None.

## Q2
```python
idade: int = "19"
```
A anotação `int` garante que o runtime do Python impedirá automaticamente essa atribuição? Explique.

Não impedirá. Ao rodar esse código ele vai fazer a atribuição normalmente, o type hint serve como um comunicador, ou seja, ele vai deixar mais explícito o tipo de uma variável e, no caso de uma função, oque entra e sai dela.

## Q3
Qual é uma função importante dos type hints?

A. Garantir validação de runtime.  
B. Tornar contratos explícitos e permitir análise estática.X  
C. Substituir testes.  
D. Converter valores automaticamente.
