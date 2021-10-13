# def funcion():
#     funcion()

# funcion()

# fibonacci

# 34 >> 21 + 13
# 21 >> 13 + 8
# 13 >> 8 + 5
# 8 >> 5 + 3
# 5 >> 2 + 3
# 3 >> 2 + 1
# 2 >> 1 + 1
# 1
# 0

# posicion >>> 0 1 2 3 4 5 6  7  8  9
# valor    >>> 0 1 1 2 3 5 8 13 21 34

# fibo(0) >> 0
# fibo(1) >> 1
# fibo(2) >> 1
# fibo(3) >> 2
# fibo(4) >> 3
# def fibo(4):
#     if posicion <= 1:
#         return posicion
#     else:
#         return fibo(4 - 1) + fibo(4 - 2)

def fibo(posicion):
    if posicion <= 1:
        return posicion
    else:
        return fibo(posicion - 1) + fibo(posicion - 2)

# posicion >>> 0 1 2 3 4 5 6  7  8  9
# valor    >>> 0 1 1 2 3 5 8 13 21 34

for i in range(20):
    print(fibo(i))



def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero - 1)
    return numero


print(factorial(3))