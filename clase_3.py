# OPERADORES

# + -
# 4 + 5
# pepe = 123123
# 4 + 5 - pepe

# EL TIPO LÓGICO
# True
# False


# OPERADORES RELACIONALES
# Igualdad/Desigualdad/Menor-Mayor que
variable_1 = 1
variable_2 = 2
variable_3 = 3
variable_4 = 5
# print(variable == 1)

# NEGACIÓN
# !
# print(variable != 1)

# print(variable_1 < 5)
# print(variable_2 > 5)
# print(variable_3 <= 5)
# print(variable_4 >= 5)

# ¿Operadores en Strings?
primer_cadena = 'hola'
segunda_cadena = 'adios'
tercer_cadena = 'a'
cuarta_cadena = 'la'

# print(primer_cadena == segunda_cadena)
# print(primer_cadena != segunda_cadena)
# print(primer_cadena < segunda_cadena)
# print(segunda_cadena < tercer_cadena)
# print(segunda_cadena <= segunda_cadena)
# print(segunda_cadena[0] == primer_cadena[-1])
# print(segunda_cadena[0] == tercer_cadena)
# print(primer_cadena[2:] == cuarta_cadena)

# print(True == 1)
# print(False == 0)
# print(True > False)

# print(False == '')
# print(False == None)
# print(True == None)

# Ejercicio 1 (10min)

# expresiones = [
#     False == True,
#     10 >= 2*4,
#     33/3 == 11,
#     True > False,
#     True*5 == 2.5*2
# ]
# print(expresiones)


# OPERADORES LÓGICOS
# not
# print(True)
# print(not True)
# print(False)
# print(not False)
# print(not True != False)

# and
# print(True == False)
# print(True == True)
# print(True == False and True == True)
# print(True == True and True == True)
# print(True == True and True == False)
# print(False == False and False == False)

# or
# print(True == False)
# print(True == True)
# print(True == False or True == True)
# print(True == True or True == True)
# print(True == True or True == False)
# print(False == False or False == False)
# print(False != False or False != False)
# print(3 > 1 or 4 == 5)
# print(3 > 1 and 4 == 5)


# True or True    ----> True          | True and True    ----> True
# False or True    ----> True         | False and True    ----> False
# True or False    ----> True         | True and False    ----> False
# False or False    ----> False       | False and False    ----> False


# Ejercicio 2 (10min)
# expresiones = [
#     not False,
#     not 3 == 5,
#     33/3 == 11 and 5 > 2,
#     True or False,
#     True*5 == 2.5*2 or 123 >= 23,
#     12 > 7 and True < False
# ]
# print(expresiones)

# Break

# EXPRESIONES ANIDADAS
# a ** b / 3**a / a * b >= 15 and not (a%b**2) != 0
# 5 / 6 / a * b >= 15 and not (a%6) != 0
# 14 >= 15 and not 1 != 0
# False and not True
# False and False
# False


# Ejercicio 3 (10min)
# A partir de dos variables llamadas NOMBRE y EDAD, 
# debes crear una variable que almacene si se cumplen 
# TODAS las siguientes condiciones, encadenando operadores lógicos en una sola línea:
# NOMBRE sea diferente de cuatro asteriscos
# EDAD sea mayor que 10 y a su vez menor que 18
# Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
# EDAD multiplicada por 4 sea mayor que 40

# nombre = 'Juan Carlos'
# edad = 15
# puntos = [
#     nombre != '****',
#     # 10 < edad < 18,
#     edad>10 and edad<18,
#     # 3 <= len(nombre) < 10,
#     len(nombre)>=3 and len(nombre)<10,
#     edad*4 > 40
# ]
# print(puntos)



# OPERADORES DE ASIGNACIÓN

# var = 100
# print(var)
# var += 15
# print(var)
# var -= 100
# print(var)
# var *= 2
# print(var)
# var /= 3
# print(var)
# var **= 2
# print(var)
# var %= 3
# print(var)