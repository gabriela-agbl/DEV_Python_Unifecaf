# Aula 06 — Exercícios práticos E0 a E9

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

---

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

---

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

---

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

---

# Enunciado — A06-E4 — Complete validacao.py

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

## Prompt PACIF de orientação

```text
P — PAPEL: Atue como tutor de Python básico.
A — AÇÃO: Ajude-me a completar quatro lacunas em uma função de validação.
C — CONTEXTO: Preciso usar um método de dicionário, o mesmo método para dois campos, o valor que representa ausência e um método de string que remove espaços externos.
I — INSTRUÇÕES: Trabalhe uma lacuna por vez. Dê a definição do recurso, peça minha resposta e solicite que eu execute os três casos. Não escreva a função final completa.
F — FORMATO: Lacuna → conceito necessário → minha tentativa → verificação.
```

---

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

---

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

---

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

---

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

---

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
