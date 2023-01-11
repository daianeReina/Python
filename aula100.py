# copy, sorted, produtos.sort

# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [{**produto, 'preco': round(produto['preco']*1.1, 2)}
                  for produto in produtos]
deep_copy_novos_produtos = copy.deepcopy(novos_produtos)

# print(novos_produtos)
# print(deep_copy_novos_produtos)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

deep_copy_produtos_ordenados_por_nome = copy.deepcopy(
    produtos)


def name_func(e):
    return e['nome']


deep_copy_novos_produtos.sort(key=name_func, reverse=True)

print(deep_copy_novos_produtos)
#
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)


def price_products(e):
    return e['preco']


produtos_ordenados_por_preco.sort(key=price_products)

print(produtos_ordenados_por_preco)
