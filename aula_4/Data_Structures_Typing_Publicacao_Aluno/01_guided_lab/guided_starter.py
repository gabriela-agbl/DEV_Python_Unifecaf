usuarios = [
    {"nome": "Ana", "email": "ana@email.com", "idade": 19, "papel": "admin", "ativo": True},
    {"nome": "Leo", "email": "leo@email.com", "idade": 20, "papel": "user", "ativo": False},
]

def buscar_ativos(usuarios):
    return [usuario for usuario in usuarios if usuario["ativo"]]

if __name__ == "__main__":
    print(buscar_ativos(usuarios))
