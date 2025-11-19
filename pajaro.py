from animal import Animal


class Pajaro(Animal):
    '''
    Clase para crear objetos de tipo Pajaro
    '''
    def __init__(self, name):
        Animal.__init__(self, name)

    def agregar_patas(self):
        Animal.agregar_patas(self, patas=2)

    def numero_patas(self):
        return 2

    def __str__(self):
        return f'Pajaro: {self.__dict__.__str__()}'

if __name__ == '__main__':
    pajaro = Pajaro('Pajaro')
    pajaro.agregar_patas()
    print(pajaro)