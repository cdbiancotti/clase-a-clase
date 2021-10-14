# Errores sintacticos
# pint('pepe')
# pint('pepe')

# Errores semanticos
var = 'pepe7'
# suma = int(input('Ingrese numero: '))
# suma += 4
# var = []
# if len(var) > 1:
#     var.pop()
# print('pepe1')
# print('pepe2')
# print('pepe3')
# print('pepe4')
# print('pepe5')
# print('pepe6')
# print(var[14])
# print('pepe8')
# print('pepe9')
# print('pepe10')
# print('pepe11')

# Desafío de errores
# def dividir(a, b):
#     if b != 0:
#         return a/b
#     else:
#         return None

# print(dividir(1, 0))

# Break

# Excepciones

# try-except

# def dividir(a, b):
#     try:
#         return a/b
#     except:
#         return None

# print(dividir(1, 0))


# try:
#     print(1/0)
# except:
#     1/1
#     2+32
#     print('No se puede dividir por 0 papa')

# var = 'pepe7'
# try:
#     print('pepe6')
#     print(var[14])
#     print('pepe8')
# except:
#     print(var)

# print('pepe')

# else
# var = 'pepe7'
# try:
#     print('pepe6')
#     print('pepe8')
#     print(var[1])
# except:
#     print('No paso por el else')
# else:
#     print('Pase por el else')

# print('pepe')

# try:
#     1/0
# except:
#     print('No se puede dividir por 0')
# else:
#     print('Se dividio por el valor')

# finally
# var = 'codigo del try'
# try:
#     if 1/0:
#         print(var)
# except:
#     print('No se puede dividir por 0')
# else:
#     print('Se dividio por el valor')
# finally:
#     print('Pase por el finally')

# Excepciones multiples
# try:
#     1/0
#     # variable
# except ZeroDivisionError as zeroerror:
#     print(zeroerror)
#     # print('Pase por el error de dividir por 0')
# except NameError:
#     print('Pase por el error de nombre')


# try:
#     try:
#         # print('prueba' + 2)
#         1/0
#         # variable
#     # except ZeroDivisionError:
#     #     print('Pase por el error de dividir por 0')
#     #     print('prueba' + 2)
#     except NameError:
#         print('Pase por el error de nombre')
#     except TypeError:
#         print('Este es un type error') 
#     # except Exception as error:
#     #     print(type(error).__name__)
#         # print('Error general')
#         # print(zeroerror)
# except ZeroDivisionError as error:
#     print('Pase por el try segundo')
#     print(type(error).__name__)


# Desafío de excepciones

# def dividir(a, b):
#     try:
#         return a/b
#     except:
#         return 'No se puede dividir entre ceros'

# print(dividir(1, 0))