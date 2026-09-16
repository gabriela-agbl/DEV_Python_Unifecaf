import json
from pathlib import Path


def carregar_registros(caminho: str) -> list[dict[str, object]]:
    texto = Path(caminho).read_text(encoding="utf-8")
    return json.loads(texto)


def registro_valido(registro: dict[str, object]) -> bool:
    identificador = registro.get("id")
    nome = registro.get("nome")
    return identificador is not None and isinstance(nome, str) and bool(nome.strip())


def calcular_total(registros: list[dict[str, object]]) -> float:
    total = 0.0
    for registro in registros:
        if registro_valido(registro):
            total += float(registro["valor"])
    return total


def main() -> None:
    registros = carregar_registros("data/entrada.json")
    total = calcular_total(registros)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
