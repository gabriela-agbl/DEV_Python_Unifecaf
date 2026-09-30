# COMECE AQUI — validar dados e testar comportamento

Development with Python • Aula 7 

Abra esta pasta inteira no VS Code. Extraia o ZIP antes de executar. Os comandos abaixo são digitados no terminal do VS Code, aberto nesta pasta, onde está `main.py`. Código Python é escrito nos arquivos `.py`, não nesse terminal.

## Preparar uma vez, antes da atividade
Python precisa estar instalado. Pacote validado na versão registrada no relatório da professora; use Python 3.12 para reproduzir a validação deste pacote. Sistemas e versões não executados estão explicitados no relatório.

No macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
No Windows, escolha o terminal **Prompt de Comando (cmd)** no VS Code:
```bat
py -m venv .venv
.venv\Scripts\activate.bat
```
Depois da ativação, nos dois sistemas:
```bash
python -m pip install --no-index --find-links wheels -r requirements.txt
python verificar_ambiente.py
```
A instalação acima usa os arquivos incluídos em `wheels`, sem Internet. Se precisar instalar pela Internet:
```bash
python -m pip install -r requirements.txt
```
Não instale unittest: ele já acompanha Python. Se não houver Python no computador, trabalhe em dupla com um ambiente disponível. Instalar Python não faz parte dos 40 minutos da atividade.

## O que cada comando significa
- `python3` (macOS/Linux) e `py` (Windows): iniciam o Python disponível no sistema. Se não forem encontrados, peça apoio; não copie comandos aleatórios.
- `-m`: pede ao Python que execute um módulo, um componente identificado pelo nome.
- `venv`: cria um ambiente separado para as dependências deste projeto.
- `.venv`: nome da pasta que recebe esse ambiente. Não é arquivo para entregar.
- `source .venv/bin/activate` e `.venv\Scripts\activate.bat`: ajustam o terminal para usar o ambiente criado. Cada comando vale para seu sistema/terminal.
- `pip install`: instala dependências no ambiente usado por esse Python.
- `--no-index`: não consulta o catálogo online; `--find-links wheels`: procura pacotes na pasta local `wheels`.
- `-r requirements.txt`: lê a lista de dependências deste arquivo.
- `python verificar_ambiente.py`: executa o diagnóstico e mostra versão e caminho do Python. Não testa sua função.
- `python main.py`: executa o fluxo que lê os dados e chama sua função.
- `python -m pytest -q tests_pytest`: executa os testes dessa pasta; `-q` reduz o texto do relatório.
- `python -m unittest discover -s tests_unittest -v`: procura testes (`discover`) na pasta indicada por `-s`; `-v` mostra o nome e o resultado de cada teste.

## Siga esta ordem
1. Leia `CONTRATO.md`. Ele define o comportamento esperado.
2. Faça A07-E1 em `EXERCICIOS.md`: complete `validacao.py` em até 40 minutos, com os momentos de apoio da professora.
3. Execute `python main.py`. Registre sua previsão e o que observou em `MINHAS_EVIDENCIAS.md`.
4. Após o exemplo com pytest, complete os três testes em `tests_pytest/test_validacao.py`.
5. Execute `python -m pytest -q tests_pytest`.
6. Após o exemplo com unittest, complete os três testes em `tests_unittest/test_validacao.py`.
7. Execute `python -m unittest discover -s tests_unittest -v`.
8. Participe da comparação e complete seu registro individual.

As linhas com `NotImplementedError` avisam que existe uma tarefa pendente. Substitua cada uma pelo código da respectiva tarefa. Uma mensagem PENDENTE ou um teste com erro nesta versão inicial não é defeito da instalação. Não use `pass` apenas para fazer a execução ficar verde: ele não verifica nada.

## Arquivos e responsabilidades
| Arquivo | Para que serve | Você altera? |
|---|---|---|
| dados/estoque.json | Lista de quantidades fictícias | Só na exploração acompanhada |
| io_dados.py | Lê JSON e verifica a estrutura | Não |
| validacao.py | Aplica a regra de estoque | Sim, A07-E1 |
| main.py | Liga leitura, validação e mensagens | Não |
| tests_pytest/test_validacao.py | Três testes com pytest | Sim, A07-P1 a P3 |
| tests_unittest/test_validacao.py | Os mesmos casos com unittest | Sim, A07-U1 a U3 |
| MINHAS_EVIDENCIAS.md | Previsões, resultados e justificativas | Sim |

## Problemas frequentes
- `No module named pytest`: confirme o ambiente com o verificador e execute a instalação local acima.
- `No module named validacao`: abra o terminal na raiz do projeto e use exatamente os comandos acima.
- `IndentationError`: confira os recuos, normalmente quatro espaços por bloco; dentro do método unittest há dois níveis.
- `0 tests` ou `no tests ran`: isso não é aprovação. Confira pasta e nomes dos arquivos/funções iniciados por `test_`.
- `AssertionError`/`FAIL`: compare entrada, regra e resultado; não mude o esperado apenas para esconder a falha.
- `ValueError` dentro do bloco que espera essa exceção pode significar teste aprovado. Uma exceção fora desse bloco tem outro significado.

Guarde os arquivos que alterou e `MINHAS_EVIDENCIAS.md`. Não envie `.venv`, `wheels` ou caches. Destino, prazo e nota: não informados. A professora orientará a entrega. O trabalho pode ser em dupla, mas o registro final é individual.
