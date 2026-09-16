from processador.io import carregar_registros
from processador.servico import calcular_total


def main() -> None:
    registros = carregar_registros("data/entrada.json")
    total = calcular_total(registros)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
