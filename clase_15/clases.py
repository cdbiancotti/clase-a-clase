class Atleta:
    altura = 1.80

    def __init__(self, peso=70):
        self.peso = peso

    def correr(self):
        print('El atleta esta corriendo.')

class Auto:
    ...

class Gato:
    ...

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def hablar(self):
        print(f'Hola soy {self.nombre} {self.apellido}')