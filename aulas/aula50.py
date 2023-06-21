"""
Exercicio
Exiba os indices da lista
"""
lista = ['Maria', 'João', 'Helena']
lista.append('Ben')

# index = 0

# for nome in lista:
#     print(index, nome)
#     index += 1

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
