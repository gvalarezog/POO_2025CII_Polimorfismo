from animal import Animal


class CienPies(Animal):
    '''
    Crear objetos tipo Cien Pies
    '''
    def __init__(self, nombre):
        Animal.__init__(self, nombre)

    def __str__(self):
        return f'Cien Pies: {self.__dict__.__str__()}'

    def numero_patas(self):
        return 100

if __name__ == '__main__':
    cp1 = CienPies('MArio')
    print(cp1)