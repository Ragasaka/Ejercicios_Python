class Animal () :
    def __init__(self, medio, extremidades, gestacion, familia):
        self.medio = medio
        self.extremidades = extremidades
        self.gestacion = gestacion
        self.familia = familia
        self.estructura = 'Pluricelular'
    
    def tipo (self) :
        print(f'Ser vivo {self.estructura}')

class Perro (Animal) :
    def ladra(self) :
        print(f'{{Perro}} ladra : gau')

class Gato (Animal) :
    def maulla(self) :
        print(f'{{Gato}} maulla : miau')

mara = Perro('tierra', 4, 'mamifero', 'canino')

print(f'{mara.estructura}')
print(f'{mara.extremidades}')
print(f'{mara.familia}')
print(f'{mara.gestacion}')
mara.ladra()

tati = Gato('tierra', 4, 'mamifero', 'canino')

print(f'{mara.estructura}')
print(f'{mara.extremidades}')
print(f'{mara.familia}')
print(f'{mara.gestacion}')
tati.maulla()