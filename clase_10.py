# Diff arg y parametros

# ¿Cuál es la diferencia entre los parámetros y argumentos?

# por posicion
# def funcion(parametro1, parametro2):
#     print(parametro1, parametro2)

# argumento1 = 'primero'
# argumento2 = 'segundo'
# funcion(argumento1, argumento2)
# funcion(argumento2, argumento1)

# por nombre
# def funcion(parametro1, parametro2):
#     print(parametro1, parametro2)

# argumento1 = 'primero'
# argumento2 = 'segundo'
# funcion(parametro1=argumento1, parametro2=argumento2)
# funcion(parametro2=argumento2, parametro1=argumento1)

# sin argumentos
# def funcion(parametro1, parametro2):
#     print(parametro1, parametro2)

# argumento1 = 'primero'
# argumento2 = 'segundo'
## funcion() # Esta forma genera error
# funcion(argumento1, argumento2)
# funcion(parametro2=argumento2, parametro1=argumento1)

# parametros por defecto
# def funcion(parametro1='default1', parametro2='default2'):
#     print(parametro1, parametro2)

# argumento1 = 'primero'
# argumento2 = 'segundo'
# funcion()
# funcion(argumento1)
# funcion(argumento2)
# funcion(parametro2=argumento2)
# funcion(argumento1, argumento2)
# funcion(argumento2, argumento1)

# def funcion(parametro1=None, parametro2=None):
#     print(parametro1 + parametro2)

# funcion(1, 2)

# break

# argumentos por valor y referencia

# lista_test = ['hola', 'chau']
# lista_test_2 = lista_test[:]

# lista_test_2.append('hasta luego')

# print(lista_test)
# print(lista_test_2)

# def funcion_con_lista(lista):
#     lista[1] += 54
#     print(lista)

# def funcion_con_numero(numero):
#     numero += 1
#     print(numero)

# valor = 2

# funcion_con_numero(valor)
# print(valor)

# lista_de_arafue = [1,2,3]
# funcion_con_lista(lista_de_arafue[:])
# print(lista_de_arafue)

# argumentos indeterminados
# *args, **kwargs

# def funcion(*args):
#     for dato in args:
#         print(dato)

# funcion(1,2,3)


# def funcion(**kwargs):
#     for llave, valor in kwargs.items():
#         print(llave, valor)

# funcion(parametro2=1,parametro1=2, parametro3=54, parametro14=4, parametro13=5, parametro31=55)

# ejercicio reloj

# def conversor(*args):
#     if len(args) == 1:
#         segundos = args[0]
#         minutos = segundos // 60
#         segundos %= 60
#         horas = minutos // 60
#         minutos %= 60
#         print(f'Hora: {horas}, Minutos: {minutos}, Segundos: {segundos}')
#     if len(args) == 3:
#         horas = args[0]
#         minutos = args[1]
#         segundos = args[2]
#         minutos += horas * 60
#         segundos += minutos * 60
#         print('Segundos:', segundos)

# conversor(3600)
# conversor(1,0,0)


# funciones recursivas

# def recursiva():
#     recursiva()

# recursiva()

# recursividad
# con retorno

# def factorial(numero):
#     print('Valor inicial ->', numero)
#     if numero > 1:
#         numero = numero * factorial(numero -1)
#     print('Valor final ->', numero)
#     return numero

# valor_final = factorial(3)
# print(valor_final)

# sin retorno
# def cuenta_regresiva(numero):
#     numero -= 1
#     if numero > 0:
#         print(numero)
#         cuenta_regresiva(numero)
#     else:
#         print('Boooom!')
#     print('Fin de la función', numero)

# cuenta_regresiva(2)


# funciones integradas ( built-in )
# int(2.3)
# float
# str
# round(2.6)
# print(help(float))
