# Guided Lab — Make the Contract Visible

## Cenário
Temos usuários representados por dicionários. O código funciona, mas o contrato está quase todo implícito.

## Regra
Não altere o comportamento da função inicialmente. Primeiro torne o contrato visível.

## Parte A — Predict
1. O que `buscar_ativos` aparentemente recebe?
2. O que devolve?
3. Quais campos parecem obrigatórios?
4. Quais tipos você infere?
5. O que precisou descobrir lendo a implementação?

## Parte B — Model
Crie um `TypedDict` chamado `Usuario`.

## Parte C — Annotate
Adicione type hints à função `buscar_ativos`.

## Parte D — Break the contract
Abra `guided_pylance_demo.py`, descomente `usuario_invalido` e observe o Pylance.

Responda:
- qual incompatibilidade foi sinalizada?
- o programa precisou executar?

## Parte E — Limit
O que o typing ainda não consegue garantir?

## Entrega
**BEFORE** — o que estava implícito?  
**AFTER** — o que ficou explícito?  
**STATIC SIGNAL** — que problema apareceu antes da execução?  
**LIMIT** — o que typing não garante?  
**AI DISCLOSURE** — se usou IA, o que aceitou, modificou ou rejeitou?
