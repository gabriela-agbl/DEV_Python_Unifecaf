# Leitura pronta: não é necessário modificar este arquivo.
import json  # Converte o texto JSON em objetos Python.
from pathlib import Path  # Representa caminhos de arquivos.


def ler_quantidades(caminho):
    # utf-8 permite ler textos com acentos de modo explícito.
    texto = Path(caminho).read_text(encoding="utf-8")
    dados = json.loads(texto)
    # Estrutura e tipo são verificados aqui, antes da regra de estoque.
    if not isinstance(dados, list):
        raise ValueError("o arquivo deve conter uma lista")
    # type(... ) is int também recusa bool; bool é subtipo de int em Python.
    if any(type(item) is not int for item in dados):
        raise ValueError("cada quantidade deve ser um inteiro")
    return dados
