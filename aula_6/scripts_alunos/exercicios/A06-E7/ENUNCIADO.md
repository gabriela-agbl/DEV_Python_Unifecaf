# Enunciado — A06-E7 — Ambiente virtual passo a passo

## A06-E7 — Ambiente virtual passo a passo

Execute somente a coluna do seu sistema.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip --version
python -m pip list
```

### macOS ou Linux com bash/zsh

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip --version
python -m pip list
```

Depois responda:

1. Qual sistema e terminal você usou?
2. Qual saída apareceu em `python -m pip --version`?
3. O projeto utiliza pacote externo ou apenas `json` e `pathlib`?
4. O que deve existir em `requirements.txt` neste projeto?
5. Por que a pasta `.venv` não deve ser entregue?
6. Execute `deactivate` ao terminar.

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de ambientes virtuais Python.
A — AÇÃO: Acompanhe a sequência de comandos do meu sistema e ajude a interpretar a saída.
C — CONTEXTO: Os comandos já estão no exercício. Preciso executá-los e entender o que aconteceu.
I — INSTRUÇÕES: Pergunte meu sistema e terminal. Peça um comando e sua saída por vez. Não invente saídas, não troque meu sistema e não mande instalar pacote desnecessário. Diferencie biblioteca padrão e dependência externa.
F — FORMATO: Passo → comando fornecido → saída real → explicação em uma frase → próximo passo.
```
