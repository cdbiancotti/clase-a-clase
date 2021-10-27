# Que era POO?
# Para que usar POO?

# Clases

# def funcion_snake_case(par1, par2):
#     return

# class AnimalCamelCase:
#     # pass
#     ...

# perro = AnimalCamelCase()
# gato = AnimalCamelCase()
# print(type(perro))
# print(type(gato))

# Constructor
# self?

# class Animal:

#     def __init__(self):
#         print('hola')

# prueba = Animal()
# print(type(prueba))

# Atributos
# atributos instancia

# class Animal:

#     def __init__(self, color='rojo'):
#         self.color = color
#         print('Se creo un animal de color', self.color)

# animal1 = Animal(color='verde')
# # print(animal.color)
# animal2 = Animal()

# atributos clase
# class Animal:
#     cant_ojos = 2

#     def __init__(self, color='rojo'):
#         self.color = color
#         print('Se creo un animal de color', self.color)

# animal1 = Animal(color='verde')
# # print(animal.color)
# animal2 = Animal()

# print(animal1.cant_ojos)
# print(animal2.cant_ojos)

# Métodos
# class Animal:
#     cant_ojos = 2

#     def __init__(self, color='rojo'):
#         self.color = color
#         print('Se creo un animal de color', self.color)

#     def saltar(self):
#         print('el animal de color', self.color, 'salto')

#     def caminar(self):
#         pasos = input('Cant de pasos dados por el animal: ')
#         print('el animal de color', self.color, 'dio', pasos, 'pasos')


# animal1 = Animal(color='verde')
# animal2 = Animal()

# print(animal1.cant_ojos)

# animal1.saltar()
# animal2.caminar()

# class Coche:
#     atributo_clase = '123123'

#     def __init__(self, par1):
#         self.atributo_instancia = 'qwe'
    
#     def determinar_cantidad_de_ruedas(self, cant_ruedas):
#         self.cant_ruedas = cant_ruedas

# auto = Coche()
# print(type(auto))
# print(auto.cant_ruedas)

# auto.determinar_cantidad_de_ruedas(4)
# print(auto.cant_ruedas)


# Ejercicio Mi primera CLASE ( 10 min )
# Crear una clase para trabajar con una Persona.
# Agregarle 3 atributos de instancia, por lo menos 2 de clase,
# el constructor y dos métodos (uno con parámetros y otro sin parámetro). 

# Luego instanciar a dos personas. 

# class Persona:
#     especie = 'mamifero'
#     idioma = 'hispanohablante'

#     def __init__(self, edad, color_ojos, color_pelo):
#         self.edad = edad
#         self.color_ojos = color_ojos
#         self.color_pelo = color_pelo

#     def saludar(self, nombre):
#         print(f'Hola, {nombre}')

#     def devolver_especie(self):
#         return self.especie

# per1 = Persona(15, 'castaño', 'castaño oscuro')
# per2 = Persona(18, 'rojo', 'castaño claro')

# per1.saludar('Pepe')
# print(per2.devolver_especie())


# Magic Methods

# class Animal:
#     cant_ojos = 2
#     cantidad_de_animales = 0
#     animales = []

#     # __init__
#     def __init__(self, color='rojo'):
#         self.color = color
#         Animal.cantidad_de_animales += 1
#         Animal.animales.append(self)

#     def saltar(self):
#         print('el animal de color', self.color, 'salto')

#     def caminar(self):
#         pasos = input('Cant de pasos dados por el animal: ')
#         print('el animal de color', self.color, 'dio', pasos, 'pasos')
    
#     def cambiar_nombre(self, nuevo_nombre):
#         self.nombre = nuevo_nombre

#     # __str__
#     def __str__(self):
#         return f'Este es un animal de color {self.color}'

#     # __len__
#     def __len__(self):
#         return self.cantidad_de_animales

#     # __getitem__
#     def __getitem__(self, indice):
#         if len(self) >= indice:
#             return self.animales[indice]
#         else:
#             return 'Faltan animales'

#     # __setitem__
#     def __setitem__(self, indice, valor):
#         self.animales[indice] = valor

#     # __iter__
#     def __iter__(self):
#         for animal in self.animales:
#             yield animal


# animal1 = Animal()
# animal2 = Animal('verde')
# print(len(animal1))
# print(len(animal2))
# print(animal1[1])
# animal1[1] = Animal('marron')
# print(animal1[1])

# for animal in animal1:
#     print(animal)


# Break

# Anidamiento

# class Persona:

#     def __init__(self, mascota):
#         self.mascotas = mascota

#     def cambiar_nombre_de_mascota(self, nuevo_nombre):
#         self.mascota.cambiar_nombre(nuevo_nombre)

# per1 = Persona(animal1)
# per1.cambiar_nombre_de_mascota('pesho')
# print(per1.mascota.color)
# print(per1.mascota.nombre)

# Encapsulamiento

# class Persona:
#     __privado = 23

#     def __init__(self, mascota):
#         self.__mascota = mascota

#     def __funcion_privada(self):
#         ...

#     def get_mascota(self):
#         return self.__mascota

#     def set_mascota(self, mascota):
#         self.__mascota = mascota

#     def uso_la_funcion_privada(self):
#         self.__funcion_privada()

# per1 = Persona(mascota=animal1)
# print(per1.__mascota.color)
# print(per1.__funcion_privada())
# print(per1.__privado)


# Ejercicio Olimpiadas ( 15 min )
# Crear una clase Atleta, que tenga su nombre, apellido, altura, 
# peso, teléfono e índice de masa corporal (descripción) .
# Decidir qué atributos deben ser públicos y cuáles privados.
# Crear los métodos get y set que crea necesarios. 

# class Atleta:

#     def __init__(self, nombre, apellido, altura, peso, telefono):
#         # publico
#         self.nombre = nombre
#         # protegido
#         self._apellido = apellido
#         # privado
#         self.__telefono = telefono
#         self.__guardar_datos(altura, peso)

#     def __guardar_datos(self, altura, peso):
#         self.__altura = altura
#         self.__peso = peso
#         self.__calcular_imc()

#     def __calcular_imc(self):
#         self.__imc = self.__peso / self.__altura**2

#     def get_imc_del_atleta(self):
#         if 1 > 0:
#             return 'no quiero saber nada'
#         return self.__imc

#     def set_telefono(self, nuevo_telefono):
#         if self.__telefono != nuevo_telefono:
#             self.__telefono = nuevo_telefono
#         else:
#             return 'ya me tenes guardado'

#     # publico
#     def gritar(self):
#         return 'AAAAAAAAaaaaaaaaaaaa!!!!!'

# atleta1 = Atleta('Pepe', 'Mujica', 1.60, 70, '12312312')
# print(atleta1.nombre)
# print(atleta1.gritar())
# print(atleta1._apellido)
# # print(atleta1.__calcular_imc())
# # print(atleta1._Atleta__telefono)
# print(atleta1.get_imc_del_atleta())
# print(atleta1.set_telefono('123123122'))