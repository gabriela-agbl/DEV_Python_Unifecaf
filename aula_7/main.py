# Coordena leitura, validação e apresentação. Já está pronto.
from pathlib import Path
from io_dados import ler_quantidades
from validacao import validar_quantidade


def main():
    # O caminho depende deste arquivo, não da pasta aberta no terminal.
    caminho = Path(__file__).resolve().parent / "dados" / "estoque.json"
    try:
        quantidades = ler_quantidades(caminho)
    except (OSError, ValueError) as erro:
        print(f"Não foi possível ler os dados: {erro}")
        return 1
    for quantidade in quantidades:
        try:
            resultado = validar_quantidade(quantidade)
            print(f"quantidade={quantidade} | retorno={resultado}")
        except NotImplementedError as erro:
            print(f"PENDENTE: {erro}")
            return 2
        except ValueError as erro:
            # Rejeitar um valor inválido é comportamento previsto.
            print(f"quantidade={quantidade} | rejeitada: {erro}")
    return 0


# Importar este módulo não inicia automaticamente a aplicação.
if __name__ == "__main__":
    raise SystemExit(main())
