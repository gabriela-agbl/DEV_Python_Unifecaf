# Enunciado — A06-E9 — Montagem do projeto final

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

---

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

---

## A06-E6 — Execute e registre evidências

Complete a versão modular antes de executar.

Crie `src/processador/io.py` e copie:

```python
import json
from pathlib import Path


def carregar_registros(caminho: str) -> list[dict[str, object]]:
    texto = Path(caminho).read_text(encoding="utf-8")
    return json.loads(texto)
```

Crie `src/processador/servico.py` e copie:

```python
from processador.validacao import registro_valido


def calcular_total(registros: list[dict[str, object]]) -> float:
    total = 0.0
    for registro in registros:
        if registro_valido(registro):
            total += float(registro["valor"])
    return total
```

Crie também um arquivo vazio chamado `src/processador/__init__.py`. Use `validacao.py` do A06-E4, `main.py` do A06-E5 e `data/entrada.json` exibido no começo desta seção.

Abra o terminal na pasta `processador_registros`. Execute somente o comando do seu sistema:

### Windows PowerShell

```powershell
$env:PYTHONPATH="src"
python -m processador.main
```

### macOS ou Linux com bash/zsh

```bash
PYTHONPATH=src python -m processador.main
```

Execute o projeto com o arquivo `data/entrada.json` fornecido e preencha:

1. comando usado para executar: __________;
2. diretório em que o comando foi executado: __________;
3. saída exibida: __________;
4. quantos registros foram aceitos: __________;
5. qual registro foi rejeitado: __________;
6. qual regra provocou a rejeição: __________.

Se aparecer erro, copie a mensagem completa e marque uma categoria: **caminho**, **importação**, **sintaxe**, **tipo** ou **não identificado**.

---

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

---

## A06-E9 — Monte o projeto final com checklist

Crie esta estrutura exatamente:

```text
processador_registros/
├── README.md
├── requirements.txt
├── data/
│   └── entrada.json
└── src/
    └── processador/
        ├── __init__.py
        ├── io.py
        ├── validacao.py
        ├── servico.py
        └── main.py
```

Use:

- em `io.py`, a função `carregar_registros` do código-base;
- em `validacao.py`, a função concluída no A06-E8;
- em `servico.py`, a função `calcular_total` copiada no A06-E6, incluindo a importação de `registro_valido`;
- em `main.py`, o código concluído no A06-E5;
- em `entrada.json`, acrescente `categoria` aos três registros;
- em `requirements.txt`, registre somente dependências externas reais;
- no `README.md`, copie os comandos de criação/ativação do ambiente usados no A06-E7 e o comando de execução usado no A06-E6.

Execute o projeto e entregue:

1. árvore de arquivos;
2. conteúdo dos quatro módulos;
3. conteúdo de `requirements.txt`;
4. trecho de instalação e execução do README;
5. comando usado;
6. saída observada;
7. uma frase para cada módulo: “este módulo existe para...”.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como conferente de montagem de projeto Python básico.
A — AÇÃO: Ajude-me a montar o projeto usando somente os blocos já escritos nos exercícios anteriores.
C — CONTEXTO: A árvore, os arquivos e as funções estão indicados. Preciso copiar conscientemente, conferir importações e executar.
I — INSTRUÇÕES: Use o checklist do enunciado. Confira um arquivo por vez e peça que eu explique seu papel. Não gere o projeto inteiro. Se houver erro, peça mensagem e diretório antes de sugerir correção. Termine verificando árvore, dependências, comando e saída.
F — FORMATO: Arquivo → bloco usado → importações → execução parcial → papel do módulo → concluído/ajustar.
```
