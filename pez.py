from animal import Animal


class Pez(Animal):
    '''
    Clase para crear objetos de tipo Pez
    '''
    def __init__(self, name):
        Animal.__init__(self, name)

    def agregar_patas(self):
        Animal.agregar_patas(self, patas=0)

    def numero_patas(self):
        return 0

    def __str__(self):
        return f'Pez: {self.__dict__.__str__()}'

if __name__ == '__main__':
    pez = Pez('Pez')
    pez.agregar_patas()
    print(pez)