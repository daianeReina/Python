# __dict__ e vars para atributos de instância


class Pessoa:
    atributo = 'valor'
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_born_year(self):
        return Pessoa.year - self.age


dados = {'name': 'João', 'age': 37}
p1 = Pessoa(**dados)
# p1 = Pessoa('João', 37)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['name'] = 'EITA'

# del p1.__dict__['name']

print(p1.__dict__)
print(vars(p1))
