
class Animal:
    '''
    Esta clase representa un animal en un objeto
    '''
    def __init__(self, nombre):
        self._nombre = nombre
        self._patas = 0

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    def numero_patas(self):
        return self._patas

    def agregar_patas(self, patas):
        if patas >= 0:
            self._patas = patas

    def __str__(self):
        return f'Animal: {self.__dict__.__str__()}'

if __name__ == '__main__':
    animal = Animal('Animal')
    animal.agregar_patas(4)
    print(animal)
