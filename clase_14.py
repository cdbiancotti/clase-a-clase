# Herencia

# class Padre:
#     ...

# class Hija(Padre):
#     ...

# DRY dont repeat yourself

# Super

# class Padre:
#     apellido = 'Fort'

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def correr(self):
#         print('Estoy corriendo')

#     # def saludar(self):
#     #     print('Hola', self.nombre, self.apellido)

# class OtroGato:
#     # ...
#     def saludar(self):
#         print('soy otro gato')

# class OtroPerro:
#     # ...
#     def saludar(self):
#         print('soy otro perro')

# class Hija(Padre, OtroPerro):
    
#     def __init__(self, nombre, edad):
#         super().__init__(nombre)
#         self.edad = edad

#     # def saludar(self):
#     #     # super().saludar()
#     #     print('Adios', self.nombre, self.apellido, self.edad)


# class Nieta(Hija, OtroGato):
    
#     def saludar(self):
#         print('Soy la nieta')
#         super().saludar()

#     def saludar_otro_gato(self):
#         print('Soy la nieta')

# padre = Padre('Octavio')
# # hija = Hija('Estela', 23)
# # # hijo = Hijo('Ricardo')
# nieta = Nieta('Manuelita', 34)
# # padre.saludar()
# # # hija.saludar()
# # # hijo.saludar()
# # nieta.saludar()
# # nieta.saludar_otro_gato()
# padre.correr()
# nieta.correr()

# MRO
# print(Nieta.__mro__)

# Herencia Multiple

# Break

# Polimorfismo

# Duck typing
# "If it walks like a duck and it quacks like a duck, then it must be a duck"

# class Pato:
#     def hablar(self):
#         print('cuak cuak!')

# class Perro:
#     def hablar(self):
#         print('gua gua!')


# def llama_hablar(parametro1):
#     parametro1.hablar()

# pato = Pato()
# perro = Perro()

# # llama_hablar(pato)
# # llama_hablar(perro)

# for animal in Perro(), Pato():
#     llama_hablar(animal)

# Ejercicio Herencia multiple (15min)


# class Mamifero():
#     espe_de_vida = "3 años"

#     def __init__(self, cant_mamas):
#         self.cant_mamas = cant_mamas

#     def mamar(self):
#         print("El mamifero mamó")

#     def nacer(self, animal):
#         print(f"El/La {animal} nació")


# class AnimalMarino():
#     tiene_Branqueas = "Si"
#     especie = "No se"

#     def nadar(self, animal):
#         print(f"El/La {animal} nadó")

# class Cetaceo(Mamifero, AnimalMarino): 
#     notas = "Es un bicho"
#     viven_en = "Oceano"
#     peso = "50KG"

#     def nacer(self, animal):
#         super().nacer(animal)

#     def nadar(self, animal):
#         print(f"El animal {animal} nadó")

# cetaceo = Cetaceo(5)
# cetaceo.nacer('Yubarta')


# class Animal:
#     def caminar(self):
#         ...


# class Perro(Animal):
#     ...

# class Gato(Animal):
#     ...