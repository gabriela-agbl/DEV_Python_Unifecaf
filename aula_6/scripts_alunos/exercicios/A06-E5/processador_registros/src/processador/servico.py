from processador.validacao import registro_valido


def calcular_total(registros: list[dict[str, object]]) -> float:
    total = 0.0
    for registro in registros:
        if registro_valido(registro):
            total += float(registro["valor"])
    return total
