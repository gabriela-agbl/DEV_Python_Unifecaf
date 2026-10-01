# A07-E1: complete somente esta função.
def validar_quantidade(quantidade):
    """Recebe inteiro. Aceita zero/positivo; rejeita negativo com ValueError."""
    if quantidade < 0:
        raise ValueError("quantidade negativa")
    if quantidade >= 0:
        return True
