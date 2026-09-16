from validacao import registro_valido

print(registro_valido({"id": 1, "nome": "Ana"}))
print(registro_valido({"id": 2, "nome": "   "}))
print(registro_valido({"nome": "Bia"}))
