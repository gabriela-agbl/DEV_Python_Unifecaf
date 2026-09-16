def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.get("id")
    nome = registro.get("nome")
    tem_id = identificador is not None
    tem_nome = isinstance(nome, str) and bool(nome.strip())
    return tem_id and tem_nome
