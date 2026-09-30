# Consulta rápida — conceitos para acompanhar o projeto

## Vocabulário
- **Arquivo:** conteúdo salvo no computador. O nosso JSON contém uma lista de números.
- **JSON:** formato de texto usado para representar dados. O leitor fornecido transforma esse texto em uma lista Python.
- **Função:** trecho de código com nome que pode receber dados e devolver um resultado.
- **Parâmetro:** nome usado pela função para receber uma entrada. Neste projeto, `quantidade`.
- **Retorno:** resultado devolvido pela função para quem a chamou.
- **Condição:** expressão avaliada como verdadeira ou falsa para decidir o próximo passo.
- **Exceção:** sinal que interrompe o fluxo normal de uma chamada. Neste contrato, `ValueError` indica um valor proibido.
- **Teste automatizado:** código que executa uma ação e verifica uma expectativa.
- **Caso de teste:** uma situação com entrada, ação e resultado esperado.
- **Regressão:** mudança que faz um comportamento antes correto deixar de atender à regra.

## Validar e testar são ações diferentes
Validar é aplicar uma regra aos dados. Testar é conferir se o código aplica a regra como deveria. A função de validação pertence à aplicação. Os testes verificam essa função. Antes de executar um teste, precisamos saber o resultado esperado a partir do contrato.

A leitura e a validação estão separadas, retomando a organização modular da aula anterior. Testar a função diretamente permite trabalhar com um valor de cada vez. Esses testes não demonstram que o arquivo será sempre encontrado ou que todo JSON será lido corretamente.

## Ler os comandos Python
`def` define uma função. O nome antes dos parênteses identifica a função; dentro dos parênteses ficam seus parâmetros. Os dois-pontos iniciam o bloco, que deve ter recuo.

`if` executa um bloco quando sua condição é verdadeira. `<` significa menor que; `<=` significa menor ou igual. A diferença importa quando o valor está na fronteira da regra.

`return` devolve um resultado e encerra a chamada. `print` mostra uma mensagem; mostrar não é o mesmo que devolver.

`raise` lança uma exceção. `ValueError` é uma exceção usada para valores inadequados. A mensagem entre parênteses explica o motivo.

`from validacao import validar_quantidade` disponibiliza a função definida no módulo `validacao.py`. Importar não equivale a chamar a função.

## assert e comparação
`=` atribui um valor. `==` compara dois valores. `assert` exige que uma condição seja verdadeira na execução normal. Se for falsa, ocorre `AssertionError`.

Exemplo independente do exercício:
```python
resultado = 2 + 3
assert resultado == 5
```
A primeira linha calcula e guarda o resultado. A segunda compara esse resultado com 5. Quando essa verificação passa, o assert sozinho não imprime uma mensagem. A ferramenta de testes apresenta o relatório.

Não use a opção `-O` para executar estes exemplos: ela pode remover asserts da linguagem. Na aplicação, use a validação explícita ensinada pela professora. [Referência Python](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement).

## pytest: funções pequenas e assert
pytest é uma ferramenta instalada separadamente. Ele encontra e executa testes conforme convenções de nomes, como funções iniciadas por `test_`. Nesta atividade, cada função de teste verifica uma situação. O comando e a pasta escolhida determinam quais testes executar. [Introdução oficial](https://docs.pytest.org/en/stable/getting-started.html).

## Esperar uma exceção
Leia `with pytest.raises(ValueError):` como: “dentro deste bloco, espero que uma chamada lance ValueError”.

- `with` delimita o bloco acompanhado pela ferramenta.
- `pytest.raises` verifica a ocorrência da exceção esperada.
- `ValueError` informa o tipo esperado; um subtipo também é aceito.
- Os dois-pontos e o recuo indicam quais linhas estão dentro do bloco.
- Se a chamada terminar sem a exceção, essa expectativa falha.
- Uma exceção de outro tipo não satisfaz essa expectativa.

O bloco não cria a validação nem transforma a entrada em inválida. Ele verifica o que a função realmente faz. Aqui, não estamos verificando o texto da mensagem, apenas o tipo da exceção.

## unittest: mesma intenção, outra escrita
unittest acompanha Python. Nesta atividade os testes ficam em métodos de uma classe baseada em `unittest.TestCase`. A estrutura já está fornecida. `self` identifica a instância usada pelo método; `self.assertEqual(obtido, esperado)` compara resultados; `with self.assertRaises(ValueError):` verifica a exceção da chamada dentro do bloco. [Referência oficial](https://docs.python.org/3/library/unittest.html).

Escolha conforme o projeto: siga o padrão existente da equipe. unittest evita instalar outra ferramenta; pytest oferece funções simples com assert direto. O importante é manter o comportamento esperado e a verificação correta, independentemente da escrita.

## Interpretar a evidência
Um teste aprovado significa que suas verificações foram satisfeitas naquela execução. Uma falha pede comparação entre a regra e o observado. Um erro pode envolver código incompleto, importação ou exceção inesperada. Não altere a expectativa apenas para obter aprovação.

Os testes desta atividade são unitários: verificam a função isolada. Verificações de integração envolvem componentes conectados, como leitura e validação. Verificações de ponta a ponta percorrem o fluxo completo de uso. Após mudar a regra, repita os testes; ao alterar conexões e formatos, confira também o fluxo integrado. Três casos não provam ausência de todos os defeitos.

## IA e qualidade — ao final
Uma IA pode sugerir outro caso ou ajudar a interpretar uma mensagem. Confira a sugestão com o contrato, faça sua previsão e execute o teste. Registre o que observou. A resposta da IA não substitui a execução nem sua explicação.
