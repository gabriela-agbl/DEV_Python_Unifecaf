# Enunciado — A06-E2 — Previsão e conferência da saída

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

## A06-E2 — Preveja e confira a saída

Sem alterar o código:

1. Marque quais registros serão aceitos: id 1, id 2 e id 3.
2. Some os valores dos registros aceitos.
3. Escreva a saída que você espera ver.
4. Execute o programa.
5. Copie a saída real.
6. Compare: a saída prevista foi igual à saída real? Responda **sim** ou **não**. Se não, explique a diferença em uma frase.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de rastreamento de código.
A — AÇÃO: Ajude-me a acompanhar a execução do código registro por registro.
C — CONTEXTO: Preciso prever a saída antes de executar.
I — INSTRUÇÕES: Pergunte primeiro o resultado de registro_valido para cada registro. Depois peça a soma. Só então peça a saída formatada. Não calcule por mim antes da minha tentativa e não invente a saída da execução.
F — FORMATO: Registro → válido? → valor incluído? → total acumulado → saída prevista → saída real.
```
