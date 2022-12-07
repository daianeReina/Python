"""
Imprecisão de ponto flutuante

"""
import decimal
num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2

print(num_3, "=> esse é o problema do ponto flutuante")
print(f'{num_3:.2f} => corrigingo transformando em string')
print(round(num_3, 2))

# Usando o Módulo Decimal
num_11 = decimal.Decimal('0.1')
num_12 = decimal.Decimal('0.7')
num_13 = num_11 + num_12
print(num_13)
