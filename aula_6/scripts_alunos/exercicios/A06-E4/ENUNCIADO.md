# Enunciado — A06-E4 — Complete validacao.py

## A06-E4 — Complete `validacao.py`

Crie o arquivo `src/processador/validacao.py`. Copie o código e substitua somente `LACUNA_1`, `LACUNA_2`, `LACUNA_3` e `LACUNA_4`.

```python
def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.LACUNA_1("id")
    nome = registro.LACUNA_2("nome")

    tem_id = identificador is not LACUNA_3
    tem_nome = isinstance(nome, str) and bool(nome.LACUNA_4())

    return tem_id and tem_nome
```

Depois execute estas verificações:

```python
print(registro_valido({"id": 1, "nome": "Ana"}))
print(registro_valido({"id": 2, "nome": "   "}))
print(registro_valido({"nome": "Bia"}))
```

Entregue:

1. os quatro valores usados nas lacunas;
2. o código completo;
3. as três saídas observadas.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de Python básico.
A — AÇÃO: Ajude-me a completar quatro lacunas em uma função de validação.
C — CONTEXTO: Preciso usar um método de dicionário, o mesmo método para dois campos, o valor que representa ausência e um método de string que remove espaços externos.
I — INSTRUÇÕES: Trabalhe uma lacuna por vez. Dê a definição do recurso, peça minha resposta e solicite que eu execute os três casos. Não escreva a função final completa.
F — FORMATO: Lacuna → conceito necessário → minha tentativa → verificação.
```
