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



def eje6(numero):
    auxi=0
    for i in range(1, numero+1):
        auxi+=i
        print(i)
    print(auxi)
eje6(5)
