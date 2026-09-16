# Enunciado — A06-E5 — Complete main.py

## A06-E5 — Complete `main.py`

Considere que as funções já existem nos módulos indicados. Crie `src/processador/main.py` e complete as quatro lacunas.

```python
from processador.LACUNA_1 import carregar_registros
from processador.LACUNA_2 import calcular_total


def main() -> None:
    registros = LACUNA_3("data/entrada.json")
    total = LACUNA_4(registros)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
```

Entregue:

1. os quatro valores das lacunas;
2. o código completo;
3. uma frase explicando o papel de `main()`.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de importações e fluxo principal.
A — AÇÃO: Ajude-me a completar imports e chamadas em main.py.
C — CONTEXTO: carregar_registros pertence a io.py e calcular_total pertence a servico.py.
I — INSTRUÇÕES: Faça-me relacionar função e módulo; depois função importada e chamada. Não complete todas as lacunas de uma vez. Termine perguntando o que main coordena.
F — FORMATO: Função necessária → módulo → import → chamada → explicação.
```
