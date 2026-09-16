# Enunciado — A06-E0 — Diagnóstico: entrada, processamento e saída

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

## A06-E0 — Marque entrada, processamento e saída

Copie e complete:

1. `data/entrada.json` é __________.
2. `carregar_registros(...)` realiza leitura da __________.
3. `registro_valido(...)` faz parte do __________.
4. `calcular_total(...)` faz parte do __________.
5. `print(f"Total: {total:.2f}")` produz uma __________.

Use somente: **entrada**, **processamento** ou **saída**.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de Python básico.
A — AÇÃO: Ajude-me a distinguir entrada, processamento e saída no código fornecido.
C — CONTEXTO: Preciso completar cinco lacunas sem receber as respostas prontas.
I — INSTRUÇÕES: Pergunte, para cada linha, o que entra, o que é transformado ou o que fica disponível ao final. Espere minha tentativa. Corrija apenas explicando o papel da linha. Não complete as lacunas por mim.
F — FORMATO: Item → minha resposta → pergunta de verificação → justificativa revisada.
```
