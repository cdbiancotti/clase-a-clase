# Módulo
from typing import List
from funcion import funcion1, funcion2
# import funcion
from funcion_otras import *
from clases import Atleta as At, Auto, Gato, Persona
from modulos.modulo1 import suma_gato_caniche

# atleta = At(60)
# atleta.correr()

# auto = Auto()
# gato = Gato()

# print(funcion1() + funcion2())

# Ejercicio (10 min)
# Hacer una clase fácil, como Persona, con nombre y apellido, con un método hablar()
# Crear una instancia de persona, mostrando sus datos y llamando al método desde otro módulo.

# persona = Persona('Pepe', 'Grillo')
# persona.hablar()

# Paquete

# Paquetes redistribuibles

# Paquetes/módulos externos

# collections
    # namedtuple
from collections import namedtuple, Counter

# print(type(list()))
# print(type(tuple()))
# print(type(dict()))
# tupla = ('Pepe', 'Grillo', 24)
# print(tupla)
# print(tupla[1])

# Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad'])
# persona = Persona('Pepe', 'Grillo', 24)

# print(persona)
# # print(persona.nombre)

# diccionario = {tupla: 'value'}
# # diccionario = {persona: 'value'}

# for key in diccionario:
#     # print(key.nombre)
#     print(key[1])
#     print(key[2])


# Counter
# tupla = ('Pepe', 24, 'Grillo', 24)
# texto = 'perro corre perro rapido'

# print(Counter(tupla))
# print(Counter(texto.split()))
# print(Counter(texto))
# c = Counter(texto)
# print(c.most_common())
# print(c.most_common(3))

# datetime
# import datetime

# date = datetime.datetime.now()
# mi_fecha = datetime.datetime(2021,12,31)
# print(date)
# print(mi_fecha)
# # print(date.day)
# # print(date.strftime('%A %d %B %Y %I:::%M'))

# diferencia = mi_fecha - date
# otra_fecha = mi_fecha.replace(year=2000)
# print(otra_fecha)


# Ejercicio ( 10 min )
# Calcular tu edad con la mayor precisión posible.
# Utilizando un módulo llamado fechas.py.

# Math

# import math

# numero = 2.4

# print(math.pow(2, 2))
# print(math.ceil(numero))
# print(math.floor(numero))
# print(math.pi)

# Random

# import random

# valores = ['pepe', 'grillo', 'hola', 'casa']

# # print(random.randint(10, 25))
# # print(math.ceil((random.random() * 5) + 1))
# print(random.choice(valores))
# print(random.choices(valores))