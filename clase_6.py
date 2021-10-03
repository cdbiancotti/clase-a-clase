# Set
# primer_set = {1,2,3,4,5,5}
# print(type(primer_set))
# lista = []
# print(type(lista))
# primer_set = {}
# print(type(primer_set))
# primer_set = set()
# print(type(primer_set))
# primer_set = {1,2,3,4,5,5}
# print(primer_set)
# primer_list = [1,2,3]
# print(primer_list)
# primer_tupla = (1,2,3)
# print(primer_tupla)
# primer_set = set(primer_tupla)
# print(primer_set)
# primer_set = set(range(10))
# print(primer_set)

# Método add
# primer_set = {1,2,3,4,5}
# primer_set = {1, 'prueba', ('tres', 'dos')}
# primer_set.add(6)
# print(primer_set)

# Método update
# primer_set = {1, 'prueba', ('tres', 'dos')}
# primer_set.update(range(5,10))
# print(primer_set)
# primer_set[:2]
# print(primer_set[:2])

# Función len
# primer_set = {1, 'prueba', ('tres', 'dos')}
# print(len(primer_set))

# Método discard
# primer_set = {1, 'prueba', ('tres', 'dos')}
# primer_set.discard(5)
# print(primer_set)

# Método remove
# primer_set = {1, 'prueba', ('tres', 'dos')}
# primer_set.remove(5)
# print(primer_set)

# Operador in
# primer_set = {1, 'prueba', ('tres', 'dos')}
# for valor in primer_set:
#     print(valor)

# print(1 in primer_set)
# print('e' in 'test')

# Método clear
# primer_set = {1, 'prueba', ('tres', 'dos')}
# print(primer_set)
# primer_set.clear()
# print(primer_set)

# Método pop
# primer_lista = [1, 'prueba', ('tres', 'dos')]
# print(primer_lista)
# valor = primer_lista.pop()
# print(valor)
# print(primer_lista)

# primer_set = {1, 'prueba', ('tres', 'dos')}
# print(primer_set)
# valor = primer_set.pop()
# print(valor)
# print(primer_set)
# valor2 = primer_set.pop()
# print(valor2)


# ej sets
# grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
# print(grupo)
# grupo.update(('Ana', 'Ramón', 'Marta', 'Eric', 'David'))
# print(grupo)
# grupo.remove('Mario')
# grupo.remove('Miguel')
# grupo.discard('Esteban')
# print(grupo)


# break

# Diccionarios
# diccionario = {}
# diccionario = {('color', 2): 'rojo'}
# print(diccionario)
# diccionario = {2: 'rojo'}
# print(diccionario)
# diccionario = {
#     'color': {
#         'primarios': ['azul', 'rojo', 'amarillo']
#     },
#     'modelo': 'Ford K'
#     }

# print(diccionario)
# print(diccionario['color']['primarios'][2])

# diccionario = {}
# diccionario['velocidad_maxima'] = 100
# print(diccionario)
# diccionario['velocidad_maxima'] += 100
# print(diccionario)

# Método update
# diccionario = {'color': 'rojo'}
# diccionario = dict(modelo='Ford K')
# print(diccionario)
# diccionario.update({'patente': 'asd123'})
# print(diccionario)

# Función len
# diccionario = {'color': 'rojo', 'patente': 'asd123'}
# print(len(diccionario))

# Función del
# diccionario = {'color': 'rojo', 'patente': 'asd123'}
# del diccionario[2]
# print(diccionario)


# Operador in
# diccionario = {'color': 'rojo', 'patente': 'asd123'}
# print('rojo' in diccionario)

# Método clear
# diccionario = {'color': 'rojo', 'patente': 'asd123'}
# diccionario.clear()
# diccionario = {}
# print(diccionario)

# Método pop
# diccionario = {'color': 'rojo', 'patente': 'asd123'}
# print(diccionario)
# valor = diccionario.pop('color')
# print(valor)
# print(diccionario)

# ej dics
# animales = {"elefante": "", "delfin": ""}
# nuevos_animales = dict(perro='dog',tigre='tiger',mono='monkey')
# nuevos_animales = {
#     'perro': 'dog',
#     'tigre': 'tiger',
#     'mono': 'monkey'
# }
# animales.update(nuevos_animales)
# print(animales)
# animales.update({"elefante": "elephant", "delfin": "dolphin"})
# animales["elefante"] = "elephant"
# animales["delfin"] = "dolphin"
# print(animales)
# del animales['delfin']
# animales.pop('gato', '')
# print(animales)
