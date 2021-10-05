# import sys as system
# from sys import argv as argumentos

# print(argumentos)

# if len(argumentos[1:]) == 2:
#     for indice in range(int(argumentos[1])):
#         print(argumentos[2])
# else:
#     print('El primer valor debe ser un entero')


# print(input('Ingresar algo: '))

# ejercicio - Aprobemos ( 20 min )
# Crear un script llamado aprobado.py que realice lo siguiente:

# 1. Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
# 2. Si ambos valores son mayores o igual a 7 imprimir “Promocionado”
# 3. Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”
# 4. Si uno de los dos valores es menor a 4 imprimir “Desaprobado, debe recuperar el primer parcial” 
# (Si el primer argumento es 3 debe recuperar el primer parcial, si no, debe decir lo mismo pero con segundo parcial)
# 5. Si ambos argumentos son menores a 4 debe imprimir “Desaprobó ambos parciales, debe recursar”
# 6. En caso de no mostrar uno o ambos argumentos debe mostrar información de como usar el script.
# import sys

# argumentos = sys.argv[1:]

# valores_posibles = ['0','1','2','3','4','5','6','7','8','9','10']

# if len(argumentos) == 2:
#     if argumentos[0] in valores_posibles and argumentos[1] in valores_posibles:
#         if int(argumentos[0]) >= 7 and int(argumentos[1]) >= 7:
#             print('Promocionado')
#         elif int(argumentos[0]) >= 4 and int(argumentos[1]) >= 4:
#             print('Aprobado, debe rendir final')
#         elif int(argumentos[0]) < 4 and int(argumentos[1]) < 4:
#             print('Desaprobó ambos parciales, debe recursar')
#         elif int(argumentos[0]) < 4 or int(argumentos[1]) < 4:
#             if int(argumentos[0]) == 3:
#                 print('Desaprobado, debe recuperar el primer parcial')
#             else:
#                 print('Desaprobado, debe recuperar el segundo se parcial')
#     else:
#         print('No son valores posibles')
# else:
#     print('''Ademas del archivo a llamar agregue los valores 
# de los parciales separados por espacios de la siguiente manera:
# py <nombre del archivo> <primer valor> <segundo valor>''')


# break

a = 'Una cadena'
b = 'Otra cadena'

# print(a, 'algo', b)

# printf-style
# cadena = '%i algo' % a
# print(cadena)

# format

# cadena = '{segundo_valor} algo {primer_valor}'.format(primer_valor=b, segundo_valor=a)
# print(cadena)

# print(f'{a} algo {5}')

# mini-lenguaje

# cadena = f'{a:<20}'
# print(cadena)

# cadena = f'{a:>20}'
# print(cadena)

# cadena = f'{a:^20}'
# print(cadena)

# cadena = f'{a:^20.3}'
# print(cadena)

# cadena = f'{25:b}'
# cadena = f'{25:c}'
# cadena = f'{25:d}'
# cadena = f'{25:o}'
# cadena = f'{12:x}'
# cadena = f'{12:X}'
# cadena = f'{12123.3123:n}'
# print(cadena)

# ejercicio - Desafío de Salida ( 10 min )
# Formatea los siguientes valores para mostrar el resultado indicado:

texto = 'Hola Mundo'
# 1. "Hola Mundo" → Alineado a la izquierda en 30 caracteres
print(f'{texto:<30}')
# 2. "Hola Mundo" → Truncamiento en el sexto carácter (índice 5)
print('{:.5}'.format('Hola Mundo'))
# 3. "Hola Mundo" → Alineamiento al centro en 10 caracteres con truncamiento en el tercer carácter (índice 2)
print('{:^10.2}'.format(texto))
# 4. 231875 → Formateo a hexadecimal en minúsculas
print('{0:x}'.format(231875))
# 5. 7887 → Formateo a binario
print('{numero:b}'.format(numero=7887))
