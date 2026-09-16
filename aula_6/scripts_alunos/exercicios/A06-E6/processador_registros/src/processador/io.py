import json
from pathlib import Path


def carregar_registros(caminho: str) -> list[dict[str, object]]:
    texto = Path(caminho).read_text(encoding="utf-8")
    return json.loads(texto)
