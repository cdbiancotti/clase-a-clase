# Funciones

# print(2)
# a = 'texto'
# a
# 2
# print(a)
# print(len(a))
# print('Texto', a, sep='...')

# len(a)

# def saludar(edad, nombre, apellido):
#     print(f'Hola {nombre} {apellido}! Tu edad es {edad}')
#     suma = 1 + 2
#     print(suma)
#     return suma

# print('Texto', a, sep='...')

# suma_de_saludar = saludar(edad=24, apellido='Dominguez', nombre='Pedro')

# if type(suma_de_saludar).__name__ == 'int':
#     print('Es un entero!')

# if suma_de_saludar == 3:
#     print('Es un 3!')

# print(suma_de_saludar)

# prueba de funcion con año de nacimiento
# def saludar(edad, nombre, apellido):
#     print(f'Hola {nombre} {apellido}! Tu edad es {edad}')
#     año_de_nacimiento = 2021 - edad
#     return año_de_nacimiento


# nacimiento = saludar(edad=24, apellido='Dominguez', nombre='Pedro')

# otro_nacimiento = saludar(edad=18, apellido='Dominguez', nombre='Pedro')

# print(nacimiento)

# if type(nacimiento).__name__ == 'int':
#     print('Es un entero!')

# if saludar(edad=18, apellido='Dominguez', nombre='Pedro') == 1997:
#     print('Es un 1997!')

# edad = 24

# def calcular_anio():
#     fecha_de_nacimiento = 2021 - edad
#     print(fecha_de_nacimiento)

# calcular_anio()


# edad = 24
# def calcular_anio():
#     edad = 21
#     fecha_de_nacimiento = 2021 - edad
#     print(fecha_de_nacimiento)


# valor = calcular_anio()
# print(valor)


# def calcular_anio(edad):
#     fecha_de_nacimiento = 2021 - edad
#     return fecha_de_nacimiento


# fecha = calcular_anio(24)
# print(fecha)


# def calcular_anio(edad):
#     fecha_de_nacimiento = 2021 - edad

#     if fecha_de_nacimiento == 1997:
#         return
#     return 'La fecha no es 1997'

# print(calcular_anio(24))

#
# ejercicio - Par o Impar ( 15 min )
# Realizar una función llamada par_o_impar:

# Recibirá un número por parámetro
# Imprimirá Par si el número es par
# Imprimirá Impar si el número es impar
# Si se ingresa algo que no sea número debe indicar que se ingrese un número.



# def par_o_impar(numero):
#     if type(numero).__name__ != 'int':
#         if not numero.isdigit():
#             return 'Debe ingresar un valor entero'
#         numero = int(numero)
#     if numero % 2 == 0:
#         return 'par'
#     else:
#         return 'impar'

# print(par_o_impar('asdasd'))