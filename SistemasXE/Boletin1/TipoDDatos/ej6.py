"""
Escribir un programa que lea un entero positivo, introducido
por el usuario y después muestre en pantalla la suma de
todos los enteros desde 1 hasta la suma de los primeros
enteros positivos puede ser calculada de la siguiente forma
"""
''''
def ejercicio6 (num):
    return num*(num+1) / 2

print(int(ejercicio6(5)))
'''

def ej6(numero):



    numero = 5
    aux = 0
    expresion = ""

    for i in range(1, numero + 1):
        aux += i
        expresion += str(i) + "+"

    print(expresion[:-1], "= " + str(aux))
    'print(expresion[:-1], "=" , aux)'

ej6(5)
