# Contrato — o que a função deve fazer

Contexto didático fictício: uma importação de estoque recebe quantidades em um arquivo JSON. Uma quantidade negativa precisa ser rejeitada. Estoque igual a zero é permitido.

`validar_quantidade(quantidade)` recebe um número inteiro já lido do arquivo.

- Quantidade maior ou igual a zero: devolve `True`.
- Quantidade menor que zero: lança `ValueError` com a mensagem `quantidade negativa`.
- A função não abre arquivos, não escreve arquivos e não imprime.
- O leitor pronto garante uma lista de inteiros. Textos, booleanos, números decimais e campos ausentes não são exercícios desta aula. Chamar diretamente a função com esses tipos está fora deste contrato.

Os três casos obrigatórios são 8 (comum), 0 (limite) e -1 (inválido). O resultado esperado deve ser deduzido desta regra antes da execução.

`dados/estoque.json` contém `[8, 0, -1]`. São dados fictícios, sem informações pessoais. O arquivo inteiro não é descartado ao encontrar um negativo: o programa mostra a rejeição e continua com o próximo item.

A aula anterior separou responsabilidades. Aqui, a leitura continua separada da regra. Os seis testes da atividade verificam a regra isoladamente, sem abrir o arquivo. Executar `main.py` verifica manualmente o fluxo conectado. Três casos aprovados não comprovam todos os possíveis comportamentos do programa.
