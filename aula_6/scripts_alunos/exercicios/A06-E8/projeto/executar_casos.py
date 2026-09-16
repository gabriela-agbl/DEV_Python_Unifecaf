from validacao import registro_valido

caso_1 = {"id": 1, "nome": "Ana", "categoria": "A"}
caso_2 = {"id": 2, "nome": "Bia", "categoria": "   "}
caso_3 = {"id": 3, "nome": "Caio"}

print(registro_valido(caso_1))
print(registro_valido(caso_2))
print(registro_valido(caso_3))
