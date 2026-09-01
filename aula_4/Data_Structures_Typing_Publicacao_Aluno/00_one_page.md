# One Page — Dados com intenção

> Dados não têm apenas valores. Dados têm intenção.

## Estrutura → Shape → Type → Contrato

- **Estrutura**: como os dados estão organizados?
- **Shape**: quais campos existem?
- **Type**: que valores esperamos?
- **Contrato**: o que uma função promete receber e devolver?

```python
nomes: list[str]
tags: set[str]
notas: dict[str, float]
coordenada: tuple[float, float]
```

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

## TypedDict

```python
from typing import TypedDict

class Usuario(TypedDict):
    nome: str
    email: str
    idade: int
    papel: str
    ativo: bool
```

`dict` diz qual estrutura usamos. `TypedDict` diz qual shape esperamos.

## Regra crítica
Type hints ajudam leitura, autocomplete, análise estática, refactoring e comunicação de contrato.
Eles não substituem validação em runtime, regras de negócio ou testes.

## SHAPE
- **S — Semantics**: o que o dado significa?
- **H — How structured**: como está organizado?
- **A — Allowed values**: que tipos/valores esperamos?
- **P — Presence**: quais campos precisam existir?
- **E — Expectations**: o que as funções recebem e devolvem?
