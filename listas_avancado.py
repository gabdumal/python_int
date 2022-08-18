# -*- coding: utf-8 -*-

# #  List comprehension
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [i**2 for i in lista1]
# lista3 = [i for i in lista1 if i % 2 != 0]

# print("Usando list comprehension")
# print(lista1)
# print(lista2)
# print(lista3)

# # Função enumerate
# lista1 = ["abacate", "bola", "cachorro"]
# for i, nome in enumerate(lista1):
#     print(f"{i}: {nome}")

# Função map
def dobro(x):
    return x * 2


valores = [1, 2, 3, 4, 5]
valoresDobrados = map(dobro, valores)
valoresDobrados = list(valoresDobrados)
print(valoresDobrados)