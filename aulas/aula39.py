"""
Iterando strings com while
"""

nome = 'Daiane'

tamanho_nome = len(nome)

indice = 0
nova_string = ''

while indice < tamanho_nome:
    nova_string += '*' + nome[indice]
    indice += 1

print(nova_string)
