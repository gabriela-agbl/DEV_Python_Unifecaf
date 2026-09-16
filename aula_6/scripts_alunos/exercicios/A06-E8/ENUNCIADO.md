# Enunciado — A06-E8 — Repetição com pequena mudança

## A06-E8 — Repita com uma pequena mudança

Agora a regra será mais específica: além de `nome`, o campo `categoria` também deve existir, ser texto e não pode conter somente espaços.

Você deve alterar **somente** `src/processador/validacao.py`.

Comece desta função:

```python
def texto_preenchido(valor: object) -> bool:
    return isinstance(valor, str) and bool(valor.strip())


def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.get("id")
    nome = registro.get("nome")
    categoria = registro.get("categoria")

    tem_id = identificador is not None
    tem_nome = texto_preenchido(nome)
    tem_categoria = LACUNA

    return tem_id and tem_nome and tem_categoria
```

Substitua `LACUNA` e execute:

```python
caso_1 = {"id": 1, "nome": "Ana", "categoria": "A"}
caso_2 = {"id": 2, "nome": "Bia", "categoria": "   "}
caso_3 = {"id": 3, "nome": "Caio"}

print(registro_valido(caso_1))
print(registro_valido(caso_2))
print(registro_valido(caso_3))
```

Entregue a linha preenchida e as três saídas. Depois complete: “`io.py` não mudou porque __________.”

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de repetição com pequena variação.
A — AÇÃO: Ajude-me a aplicar à categoria o mesmo padrão já usado para nome.
C — CONTEXTO: O arquivo e a função estão indicados. Preciso completar uma única lacuna e executar três casos.
I — INSTRUÇÕES: Peça que eu identifique a função auxiliar já disponível. Pergunte qual valor precisa ser verificado. Não escreva a linha final antes da minha tentativa. Depois confira comigo os três resultados e a explicação sobre io.py.
F — FORMATO: Padrão anterior → novo campo → minha linha → caso 1 → caso 2 → caso 3 → explicação.
```
