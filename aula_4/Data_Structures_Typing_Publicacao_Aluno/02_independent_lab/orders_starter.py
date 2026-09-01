pedidos = [
    {"id": 1001, "cliente": "Ana", "status": "pago", "total": 129.90},
    {"id": 1002, "cliente": "Leo", "status": "pendente", "total": 80.00},
]

def processar_pedido(pedido):
    if pedido["status"] == "pago":
        return pedido["total"]
    return None

if __name__ == "__main__":
    for pedido in pedidos:
        print(processar_pedido(pedido))
