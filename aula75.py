# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def create_multiple(multiple):
    def multiplication(number):
        return number * multiple
    return multiplication


duplicate = create_multiple(2)
triplicate = create_multiple(3)
quadriplicate = create_multiple(4)

print(duplicate(2))
print(triplicate(2))
print(quadriplicate(2))
