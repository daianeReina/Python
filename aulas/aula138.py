# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Estou na classe PESSOA')
        # self.__class__.__name__ => mostra a child class, a classe que está sendo executada no momento.
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA!!!Estou na classe CLIENTE')
        # self.__class__.__name__ => mostra a child class, a classe que está sendo executada no momento.
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    ...


c1 = Cliente('Daiane', 'Reina')
c1.falar_nome_classe()

a1 = Aluno('João', 'Silva')
a1.falar_nome_classe()
