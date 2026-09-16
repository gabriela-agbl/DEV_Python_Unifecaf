# Enunciado — A06-E1 — Leitura guiada do código-base

## Código-base usado nos exercícios A06-E0 a A06-E3

Leia este código. Você não precisa criá-lo do zero.

```python
import json
from pathlib import Path


def carregar_registros(caminho: str) -> list[dict[str, object]]:
    texto = Path(caminho).read_text(encoding="utf-8")
    return json.loads(texto)


def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.get("id")
    nome = registro.get("nome")
    return identificador is not None and isinstance(nome, str) and bool(nome.strip())


def calcular_total(registros: list[dict[str, object]]) -> float:
    total = 0.0
    for registro in registros:
        if registro_valido(registro):
            total += float(registro["valor"])
    return total


def main() -> None:
    registros = carregar_registros("data/entrada.json")
    total = calcular_total(registros)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
```

Use este conteúdo em `data/entrada.json`:

```json
[
  {"id": 1, "nome": "Ana", "valor": 10.0},
  {"id": 2, "nome": "   ", "valor": 20.0},
  {"id": 3, "nome": "Bia", "valor": 15.5}
]
```

## A06-E1 — Leia e localize partes do código

Responda usando os nomes exatamente como aparecem no código-base:

1. Qual função abre o arquivo?
2. Qual função decide se um registro pode ser usado?
3. Qual função soma os valores?
4. Qual função coordena a execução?
5. Qual linha chama `main()` somente quando o arquivo é executado diretamente?
6. Qual módulo da biblioteca padrão interpreta o JSON?

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de leitura de código Python.
A — AÇÃO: Ajude-me a localizar funções, chamadas e importações no código-base.
C — CONTEXTO: Sou iniciante e preciso treinar a leitura do que já está escrito.
I — INSTRUÇÕES: Faça uma pergunta por vez. Peça que eu aponte a linha ou nome antes de comentar. Se eu errar, indique apenas a região do código. Não dê a lista final de respostas.
F — FORMATO: Pergunta → linha que escolhi → pista → confirmação explicada.
```
