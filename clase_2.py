# Listas

lista = ['1', 1, 2, 3, 'pepe', 'hola', 'casa']

otra_lista = [34 ,55, 'otra cosa']

# Listas y Strings

cadena = 'soy una cadena cualquiera'

# print(cadena)
# print(lista)
# print(cadena[-1])
# print(lista[-1])
# print(cadena[2:12])
# print(lista[1:3])

# variable = lista + otra_lista
# variable.append('otro pepe')
# print(variable)
# lista_nueva = lista + ['nuevo', 'dato']
# print(lista_nueva)


# Funciones de listas 
# append
# print(lista)
# lista.append('otro dato')
# print(lista)

# len
# print(len(cadena))
# print(len(lista))

# pop

# print(lista)
# valor_extraido1 = lista.pop()
# print(lista)
# print(valor_extraido1)
# valor_extraido2 = lista.pop(3)
# print(lista)
# print(lista[3])
# print(valor_extraido2)

# count

# print(lista.count(1))
# lista.append(1)
# print(lista)
# print(lista.count(1))

# index
# lista.append('1')
# print(len(lista))
# print(lista.index('1'))
# print(lista.index('1', 2))
# print(lista.index('1', 2, 5))

# Ejercicio de listas (10 min)
# Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:
# - Añade a la LISTA1 el int 1234 y luego el string “Hola”
# - Añade a la LISTA2 el string “Adios” y luego el int 1234
# - Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
# - Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
# - Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

# lista1 = [1, 12, 123]
# lista2 = ["Bye", "Ciao", "Agur", "Adieu"]
# lista1 = lista1 + [1234, 'Hola']
# print(lista1)
# lista2.append('Adios')
# lista2.append(1234)
# print(lista2)
# lista3 = lista1[:-1]
# print(lista3)
# lista4 = lista2[1:-1]
# print(lista4)
# lista5 = lista4 + lista3
# print(lista5)

# lista3 = lista1.pop()
# print(lista1)
# print(lista3)


# print(lista)
# print(lista[4])
# lista[4] = 'persona'
# print(lista)
# print(lista[4])

# break

# Tuplas

tupla1 = ('otra', 1, 2, 'otra')
tupla2 = ('menos', 54, 13, 'mas')
# tupla[2] = 'mas' # Genera un error


# Funciones de tuplas

# len
# print(len(tupla))
# # count
# print(tupla.count('otra'))
# # index
# print(tupla.index('otra'))
# print(tupla.index('otra', 1))
# print(tupla.index('otra', 1, 2)) # Genera un error
# print(tupla.index(3)) # Genera un error

# otra_tupla = tupla1 + tupla2
# print(otra_tupla)

# Anidación
# mas_tuplas = ((1,2,3), ['hola', 'pepe'])
# mas_listas = [('soy', 'una', 'tupla'), 2 ,3 ,4, [(3,1), (15, 2)]]
# print(mas_tuplas)
# print(mas_listas)

# print(mas_tuplas[1][1])

# otra_forma = 1,2,3,4,'mas valores'
# print(otra_forma)
# tupla_solo_valor = 'string',
# print(tupla_solo_valor)

# # Casting
# lista_desde_tupla = list(tupla_solo_valor)
# print(lista_desde_tupla)

# tupla_desde_lista = tuple(lista_desde_tupla)
# print(tupla_desde_lista)


# Ejercicio 2 (10 min)
# A partir de una variable llamada tupla debes 
# imprimir por pantalla de forma ordenada, lo siguiente:
# - El último ítem de tupla
# - El número de ítems de tupla
# - La posición donde se encuentra el ítem 87 de tupla
# - Una lista con los últimos tres ítems de tupla
# - Un ítem que haya en la posición 8 de tupla
# - El número de veces que el ítem 7 aparece en tupla
# Copia esta tupla:
tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
# print(tupla[-1])
# print(len(tupla))
# print(tupla.index(87))
# lista_de_tupla_cortada = list(tupla[-3:])
# print(lista_de_tupla_cortada)
# posicion_8 = tupla[7]
# print(tupla[7])
# print(tupla.count(7))

# print(tupla[3])
# print(tupla[1342]) # Error