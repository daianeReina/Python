# @property + @setter - getter e setter no modo Pythônico
# - como getter => getter = a obter um valor
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
         self._cor = cor
         self._cor_tampa = None

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no SETTER...', valor)
        self._cor= valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


def mostrar(caneta):
    return caneta.cor




caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
caneta.cor_tampa = 'azul'
print(caneta.cor_tampa)

