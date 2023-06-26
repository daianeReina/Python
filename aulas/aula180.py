# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'


lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereco': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereco': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereco': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as file:
    nome_colunas = lista_clientes[0].keys()

    escritor = csv.DictWriter(
        file,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w') as file:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(file)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         # print(cliente.values())
#         # escritor.writerow(cliente.values())
#         escritor.writerow(cliente)

# # print(lista_clientes[0].keys())
