# Atributos de classe


class Pessoa:
    atributo = 'valor'
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_born_year(self):
        return Pessoa.year - self.age


p1 = Pessoa('João', 37)
p2 = Pessoa('MAria', 65)
print(Pessoa.year)
print(p1.get_born_year())
print(p2.get_born_year())
