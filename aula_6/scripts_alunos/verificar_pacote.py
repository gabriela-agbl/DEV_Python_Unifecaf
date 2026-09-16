from pathlib import Path

raiz = Path(__file__).parent
ids = [f"E{i}" for i in range(10)]
faltando = []
for codigo in ids:
    pasta = raiz / "exercicios" / f"A06-{codigo}"
    for nome in ("ENUNCIADO.md", "PROMPT_PACIF.md", "RESPOSTA.md"):
        if not (pasta / nome).exists():
            faltando.append(str(pasta / nome))

if faltando:
    print("Pacote incompleto. Arquivos ausentes:")
    for item in faltando:
        print(f"- {item}")
    raise SystemExit(1)

print("Pacote íntegro: exercícios A06-E0 a A06-E9 disponíveis.")
