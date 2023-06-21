

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro_1 = Carro('Qashqai')
motor_1 = Motor('1.5')
fabricante_1 = Fabricante('Nissan')

carro_1.fabricante = fabricante_1
carro_1.motor = motor_1

print(carro_1.nome)
print(carro_1.fabricante.nome)
print(carro_1.motor.nome)

carro_2 = Carro('Chevet')
fabricante_2 = Fabricante('Chevrolet')

carro_2.fabricante = fabricante_2
carro_2.motor = motor_1

print(carro_2.nome)
print(carro_2.fabricante.nome)
print(carro_2.motor.nome)

carro_3 = Carro('KA')
fabricante_3 = Fabricante('Ford')
motor_3 = Motor('1.0')

carro_3.fabricante = fabricante_3
carro_3.motor = motor_3

print(carro_3.nome)
print(carro_3.fabricante.nome)
print(carro_3.motor.nome)
