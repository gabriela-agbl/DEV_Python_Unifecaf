# Enunciado — A06-E6 — Execução e registro de evidências

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

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de execução e diagnóstico.
A — AÇÃO: Ajude-me a registrar uma execução real e classificar eventual erro.
C — CONTEXTO: Tenho um projeto modular e preciso apresentar evidência, não apenas dizer que funcionou.
I — INSTRUÇÕES: Pergunte o diretório, o comando e a saída real. Nunca invente saída. Se houver erro, use a mensagem para separar caminho, importação, sintaxe ou tipo. Dê um próximo teste por vez.
F — FORMATO: Comando → saída real → categoria → hipótese → próximo teste → resultado.
```
