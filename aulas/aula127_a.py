# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127.json'


class Person:
    year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_born_year(self):
        return Person.year - self.age


p1 = Person('Daiane', 36)
p2 = Person('Marco', 36)
p3 = Person('Ben', 4)
p4 = Person('Maria', 64)
p5 = Person('Pedro', 74)

data_base = [vars(p1), vars(p2), vars(p3), vars(p4), vars(p5)]

with open(CAMINHO_ARQUIVO, 'w') as file:
    json.dump(data_base, file, ensure_ascii=False, indent=2)
