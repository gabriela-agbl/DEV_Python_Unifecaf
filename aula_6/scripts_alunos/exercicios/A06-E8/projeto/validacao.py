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
