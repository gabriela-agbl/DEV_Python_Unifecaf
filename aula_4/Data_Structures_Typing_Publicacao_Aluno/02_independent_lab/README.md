# Independent Lab — Data Contract Review

Abra `orders_starter.py`.

## Parte A — Contract Discovery
1. Que campos existem em um pedido?
2. Quais tipos parecem esperados?
3. Quais campos são usados por `processar_pedido`?
4. O retorno pode assumir quais tipos?
5. Que conhecimento está implícito?

## Parte B — Model
Crie um `TypedDict` chamado `Pedido`.

## Parte C — Annotate
Tipar `processar_pedido` de modo que receba `Pedido` e retorne o total ou `None`.

## Parte D — Static Failure
Crie deliberadamente um `Pedido` cujo `total` seja `"100.00"` e observe o Pylance.

## Parte E — Runtime Trap
Execute `runtime_trap.py` e explique por que `TypedDict` não valida automaticamente dados externos.

## Parte F — Review
**CONTRACT** A função recebe pedido e retorna um float(total do pedido) ou nada(None)  
**STATIC EVIDENCE** Antes da execução, o total do pedido no dicionário está como String, mas foi definido no Type Hint como float 
**RUNTIME LIMIT**  
**DECISION: KEEP / REVISE**  
**WHY** — até 5 linhas  
**AI DISCLOSURE**
