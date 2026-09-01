from typing import TypedDict

class Usuario(TypedDict):
    nome: str
    email: str
    idade: int
    papel: str
    ativo: bool

usuarios: list[Usuario] = [
    {"nome": "Ana", "email": "ana@email.com", "idade": 19, "papel": "admin", "ativo": True}
]

# Descomente durante a atividade:
usuario_invalido: list[Usuario] = [{
     "nome": "Bia",
     "email": "bia@email.com",
     "idade": "19",  # int esperado
     "papel": "user",
     "ativo": True,
 }]

def buscar_ativos(usuario_invalido: list[Usuario]) -> list[Usuario]:
    return [usuario for usuario in usuario_invalido if usuario["ativo"]]

if __name__ == "__main__":
    print(buscar_ativos(usuario_invalido))
