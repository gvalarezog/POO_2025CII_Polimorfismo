import animal
from cien_pies import CienPies
from pajaro import Pajaro
from perro import Perro
from pez import Pez

perro1 = Perro('Tobi')
perro1.agregar_patas()

perro2 = Perro('Charlie')
perro2.agregar_patas()

pajaro1 = Pajaro('Beto')
pajaro1.agregar_patas()

pajaro2 = Pajaro('Bob')
pajaro2.agregar_patas()

pez1 = Pez('Doris')
pez1.agregar_patas()

pez2 = Pez('Joe')
pez2.agregar_patas()

cp1 = CienPies('Mario')

animales = list()
animales.append(perro1)
animales.append(perro2)
animales.append(pajaro1)
animales.append(pajaro2)
animales.append(pez1)
animales.append(pez2)
animales.append(cp1)

def contar_patas(animales):
    contador = 0
    for animal in animales:
        contador += animal.numero_patas()
    return contador

def contar_patas2(animales):
    contador = 0
    for animal in animales:
        if isinstance(animal, Perro):
            contador += 4
        elif isinstance(animal, Pez):
            contador += 0
        elif isinstance(animal, CienPies):
            contador += 100
        elif isinstance(animal, Pajaro):
            contador += 2
    return contador

print(contar_patas(animales))
print(contar_patas2(animales))
