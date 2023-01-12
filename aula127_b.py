import json

from aula127_a import CAMINHO_ARQUIVO, Person

with open(CAMINHO_ARQUIVO, 'r') as file:
    people_data = json.load(file)

    p1 = Person(**people_data[0])
    p2 = Person(**people_data[1])
    p3 = Person(**people_data[2])
    p4 = Person(**people_data[3])
    p5 = Person(**people_data[4])

    print(p1.name)
    print(vars(p1))
    print(vars(p2))
    print(vars(p3))
    print(vars(p4))
    print(vars(p5))
