# MÉTODOS DE CLASSE + FACTORIES(FÁBRICAS)
# São métodos onde "Self" será "cls", ou seja,
# Ao invés de receber a instância no primeiro parâmetro,
# receberemos a própria classe.

class Person:
    year = 2022  # Atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #faz com que eu p+ossa chamar um método sem passar self
    def class_method(cls):
        print('Hey!')

    @classmethod #factorie method
    def person_without_name(cls, idade):
        return cls('Anônima',idade)

    @classmethod #factorie method
    def person_with_50_years(cls, name):
        return cls(name,50)
    

p1=Person('Daiane', 36)
# print(Person.year)
# Person.class_method()

p2 = Person.person_with_50_years('Maria')
print(p2.name, p2.age)

p3= Person.person_without_name(25)
print(p3.name, p3.age)
