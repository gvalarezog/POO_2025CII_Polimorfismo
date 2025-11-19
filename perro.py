from animal import Animal


class Perro(Animal):
    '''
    Clase para crear objetos de tipo Perro
    '''
    def __init__(self, name):
        Animal.__init__(self, name)

    def agregar_patas(self):
        Animal.agregar_patas(self, patas=4)

    def numero_patas(self):
        return 4

    def __str__(self):
        return f'Perro: {self.__dict__.__str__()}'

if __name__ == '__main__':
    perro = Perro('Perro')
    perro.agregar_patas()
    print(perro)
