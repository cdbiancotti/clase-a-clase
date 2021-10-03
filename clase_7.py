# Strings

cadena1 = 'pRiMerteXtoer'
cadena2 = 'segunda texto'

# cadena1 = cadena1.split()
# print(cadena1)

# Método upper
# cadena1 = cadena1.upper()
# print(cadena1)

# Método lower
# cadena1 = cadena1.lower()
# print(cadena1)


# Método capitalize
# cadena1 = cadena1.capitalize()
# print(cadena1)


# Método title
# cadena1 = cadena1.title()
# print(cadena1)


# Método count
# print(cadena1.count('ER'))


# Método find
# print(cadena1.find('e'))


# Método rfind
# print(cadena1.rfind('e'))


# Método split
# print(cadena1.split())
# cadena1 = cadena1.split()

# Método join
# print(''.join(cadena1))


# Método strip
# cadena3 = f'       {cadena1}       '
# print(cadena3)
# cadena3 = cadena3.strip()
# print(cadena3)


# Método replace
# cadena1.replace('er', 'az')
# cadena1 = cadena1.replace('er', 'az')
# print(cadena1)

# Listas

lista1 = ['primera', 'lista', 1]
lista2 = ['segunda', 'lista', 2]
lista_numeros = ['5','1','2','3','4','10']

# Método clear
# lista1.clear()
# print(lista1)

# Método extend
# print(lista1 + lista2)
# lista1 += lista2
# print(lista1)
# lista1.extend(lista2)
# print(lista1)


# Método insert
# lista2.insert(-1, True)
# print(lista2)


# Método reverse
# print(cadena1)
# print(cadena1[::-1])
# lista2.reverse()
# print(lista2)
# print(cadena1.split())


# Método sort
# lista_numeros.sort()
# print(lista_numeros)


# ejercicio - colecciones 1
# texto = ('gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies'
#          ' -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista')

# lista = texto.split('&')
# print(lista)
# for indice, substring in enumerate(lista):
#     lista[indice] = substring[0].upper() + substring[1:]
# texto = '.\n- '.join(lista)
# texto = texto.replace('.', '...', 1)
# print(texto)


# Conjuntos

conjunto1 = {1, 'conjunto1', (1, True)}
conjunto2 = {1, 'conjunto2', (1, True)}

# Método copy
# conjunto3 = conjunto1.copy()
# conjunto3.add(54)
# print(conjunto1)
# print(conjunto3)
# conjunto3 = conjunto1
# conjunto3.add(54)
# print(conjunto1)
# print(conjunto3)

# Método isdisjoint
# print(conjunto1.isdisjoint(conjunto2))

# Método issubset
# print(conjunto2.issubset(conjunto1))


# Método issuperset
# print(conjunto1.issuperset(conjunto2))


# Método union
# print(conjunto1.union(conjunto2))


# Método difference
# print(conjunto1.difference(conjunto2))
# print(conjunto1)

# Método difference_update
# print(conjunto1.difference_update(conjunto2))
# print(conjunto1)


# Método intersection
# print(conjunto1.intersection(conjunto2))
# print(conjunto1)


# Método intersection_update
# print(conjunto1.intersection_update(conjunto2))
# print(conjunto1)



# Diccionarios

diccionario1 = {'estado': 'Activo', 'deporte': 'Paddle'}
diccionario2 = {'deporte': 'Paddle'}

# Método get
# diccionario1['pepe']

# diccionario1.get('pepe', 'esa key no exite')

# for x in diccionario1:
#     print(x)

# Método keys
# print(diccionario1.keys())
# for key in diccionario1.keys():
#     print(key)

# Método values
# print(diccionario1.values())
# for value in diccionario1.values():
#     print(value)

# dict_items([('estado', 'Activo'), ('deporte', 'Paddle')])

# Método items
# print(diccionario1.items())
# for key, value in diccionario1.items():
#     print(f'{key}')




# ejercicio - colecciones 2
# A partir de una lista realizar las siguientes tareas sin modificar la lista original:

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1. Borrar los elementos duplicados
sin_duplicados = list(set(lista))
# print(sin_duplicados)

# 2. Ordenar la lista de mayor a menor
sin_duplicados.sort()
sin_duplicados.reverse()
# print(lista_ordenada)

# 3. Eliminar todos los números impares
lista_sin_impares = []
for valor in sin_duplicados:
    if valor % 2 == 1:
        continue
    else:
        lista_sin_impares.append(valor)

# print(lista_sin_impares)


# 4. Realizar una suma de todos los números que quedan
suma = sum(lista_sin_impares)
# print(suma)

# 5. Añadir como primer elemento de la lista la suma realizada
lista_sin_impares.insert(0, suma)

# 6. Devolver la lista modificada
# print(lista_sin_impares)


# 7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
# los números a partir del segundo, concuerda con el primer número de la lista
suma_total = sum(lista_sin_impares[1:])
# print(suma_total)

# Nota:
# Recorda que para sumar todos los números de una lista podes usar sum