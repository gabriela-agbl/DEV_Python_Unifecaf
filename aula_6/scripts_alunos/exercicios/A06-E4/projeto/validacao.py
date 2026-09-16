def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.LACUNA_1("id")
    nome = registro.LACUNA_2("nome")

    tem_id = identificador is not LACUNA_3
    tem_nome = isinstance(nome, str) and bool(nome.LACUNA_4())

    return tem_id and tem_nome
