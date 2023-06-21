# Métodos em instâncias de classes Python

class Car:
    def __init__(self, car_name):
        # self.name = 'Fusca' # Hard Coded - algo que foi escrito diretamente no código
        self.name = car_name

    def speed_up(self):
        print(f'The {self.name} is speeding up...')


fusca = Car('Fusca')
print(fusca.name)
fusca.speed_up()

celta = Car('Celta')
print(celta.name)
celta.speed_up()
