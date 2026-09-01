from typing import TypedDict

class Pedido(TypedDict):
    id: int
    cliente: str
    status: str
    total: float

def processar_pedido(pedido: Pedido) -> float | None:
    if pedido["status"] == "pago":
        return pedido["total"]
    return None

# Imagine que veio de JSON, arquivo ou API.
pedido_externo = {
    "id": 1003,
    "cliente": "Bia",
    "status": "pago",
    "total": "100.00",
}

print("Valor recebido:", pedido_externo)
print("Tipo real de total:", type(pedido_externo["total"]).__name__)
print("Resultado da função:", processar_pedido(pedido_externo))  # type: ignore[arg-type]
