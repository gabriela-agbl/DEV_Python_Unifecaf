# Enunciado — A06-E3 — Função e arquivo

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

## A06-E3 — Relacione função e arquivo

Vamos usar esta estrutura:

```text
src/processador/
├── __init__.py
├── io.py
├── validacao.py
├── servico.py
└── main.py
```

Complete com um dos arquivos: `io.py`, `validacao.py`, `servico.py` ou `main.py`.

1. `carregar_registros` vai para __________.
2. `registro_valido` vai para __________.
3. `calcular_total` vai para __________.
4. a função que coordena todas as chamadas vai para __________.
5. Explique em uma frase por que `registro_valido` não ficou em `io.py`.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de modularização para iniciantes.
A — AÇÃO: Ajude-me a relacionar funções aos quatro arquivos já definidos.
C — CONTEXTO: Não preciso inventar a estrutura; preciso reconhecer a responsabilidade de cada função.
I — INSTRUÇÕES: Para cada função, pergunte se ela lê/grava, valida, calcula ou coordena. Espere minha escolha. Não diga o nome do arquivo antes da tentativa. Termine pedindo que eu explique uma separação.
F — FORMATO: Função → ação principal → arquivo escolhido → justificativa curta.
```
