'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.'''

palabra = input("Dime: ")

lista = list(palabra)

lista.reverse()

for i in range(0, len(lista)):
    print(lista[i])