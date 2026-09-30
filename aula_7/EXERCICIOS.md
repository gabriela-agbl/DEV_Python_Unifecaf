# Atividades — um projeto, três comportamentos

Leia `CONTRATO.md` antes de começar. Execute todos os comandos na raiz do projeto. Os arquivos nomeados abaixo acompanham este pacote integralmente.

## A07-E1 — construir a validação (40 minutos, incluindo apoio)
Objetivo: implementar uma regra pequena e explicar como conferiu o resultado.
Arquivos: `validacao.py` (complete), `main.py`, `io_dados.py`, `dados/estoque.json` (prontos). Dados: 8, 0 e -1. Conceitos: parâmetro, condição, retorno e exceção.
1. Leia o contrato e localize onde os dados são lidos e onde serão validados.
2. Antes de editar, escreva o resultado que espera para cada entrada.
3. Complete os TODOs em `validacao.py`. Retire o aviso de tarefa pendente.
4. Execute `python main.py`.
5. Compare sua previsão com a saída. Se discordarem, identifique a regra relevante.
6. Registre o código usado e como conferiu o resultado.
Entrega: arquivo `validacao.py` e seção A07-E1 de `MINHAS_EVIDENCIAS.md`. Não basta escrever “funcionou”.

## Primeira rodada — pytest (20 minutos)
Pré-requisito: acompanhar o exemplo resolvido da professora. Arquivos necessários: `validacao.py`, `tests_pytest/test_validacao.py`, `CONTRATO.md`. A função deve estar implementada; peça o checkpoint se necessário.

### A07-P1 — caso comum (5 minutos)
Objetivo: compare o retorno da função com o esperado pelo contrato. Conceito: teste do caso comum com pytest.
Entrada: `8`. Arquivo a completar: `tests_pytest/test_validacao.py`, função/método `test_comum`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use assert e pytest.raises conforme o comportamento avaliado.
3. Execute:
```bash
python -m pytest -q tests_pytest/test_validacao.py::test_comum
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.

### A07-P2 — caso limite (6 minutos)
Objetivo: confira se o menor valor permitido é aceito. Conceito: teste do caso limite com pytest.
Entrada: `0`. Arquivo a completar: `tests_pytest/test_validacao.py`, função/método `test_limite`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use assert e pytest.raises conforme o comportamento avaliado.
3. Execute:
```bash
python -m pytest -q tests_pytest/test_validacao.py::test_limite
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.

### A07-P3 — caso inválido (9 minutos)
Objetivo: verifique se ocorre a exceção prevista, usando um bloco de expectativa de exceção. Conceito: teste do caso inválido com pytest.
Entrada: `-1`. Arquivo a completar: `tests_pytest/test_validacao.py`, função/método `test_invalido`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use assert e pytest.raises conforme o comportamento avaliado.
3. Execute:
```bash
python -m pytest -q tests_pytest/test_validacao.py::test_invalido
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.


## Segunda rodada — unittest (20 minutos)
Pré-requisito: acompanhar a tradução do exemplo pela professora. Arquivos: `validacao.py`, `tests_unittest/test_validacao.py`, `CONTRATO.md`. Reutilize as previsões da rodada anterior.

### A07-U1 — caso comum (5 minutos)
Objetivo: compare o retorno da função com o esperado pelo contrato. Conceito: teste do caso comum com unittest.
Entrada: `8`. Arquivo a completar: `tests_unittest/test_validacao.py`, função/método `test_comum`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use self.assertEqual e self.assertRaises conforme o comportamento avaliado.
3. Execute:
```bash
python -m unittest -v tests_unittest.test_validacao.TestValidacao.test_comum
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.

### A07-U2 — caso limite (6 minutos)
Objetivo: confira se o menor valor permitido é aceito. Conceito: teste do caso limite com unittest.
Entrada: `0`. Arquivo a completar: `tests_unittest/test_validacao.py`, função/método `test_limite`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use self.assertEqual e self.assertRaises conforme o comportamento avaliado.
3. Execute:
```bash
python -m unittest -v tests_unittest.test_validacao.TestValidacao.test_limite
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.

### A07-U3 — caso inválido (9 minutos)
Objetivo: verifique se ocorre a exceção prevista, usando um bloco de expectativa de exceção. Conceito: teste do caso inválido com unittest.
Entrada: `-1`. Arquivo a completar: `tests_unittest/test_validacao.py`, função/método `test_invalido`.
1. Registre o resultado esperado, consultando o contrato.
2. Substitua apenas o aviso de tarefa pendente deste teste. Use self.assertEqual e self.assertRaises conforme o comportamento avaliado.
3. Execute:
```bash
python -m unittest -v tests_unittest.test_validacao.TestValidacao.test_invalido
```
4. Leia o relatório: registre se o teste passou, falhou ou encontrou um erro e explique por quê.
Entrega: código do teste e uma linha no quadro de evidências com ID, entrada, esperado, observado e justificativa.

## Fechamento — todos registram (durante o bloco final)
Depois da demonstração de alteração proposital, registre qual caso detectou a mudança e a relação entre a falha e o contrato. Informe qual ferramenta usou. Voluntários apresentam uma entrada, uma expectativa e a evidência observada. Se não executou, escreva NOT_RUN; não invente saída.

### Como ler os comandos individuais
No pytest, `arquivo.py::test_comum` seleciona uma função desse arquivo. No unittest, o caminho com pontos indica pacote, módulo, classe e método; não leva `.py` no final. `-v` mostra mais detalhes; `-q` mostra menos. Para executar os três testes de uma vez, use os comandos de pasta do COMECE_AQUI.
