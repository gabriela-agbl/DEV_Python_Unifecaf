from processador.LACUNA_1 import carregar_registros
from processador.LACUNA_2 import calcular_total


def main() -> None:
    registros = LACUNA_3("data/entrada.json")
    total = LACUNA_4(registros)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
