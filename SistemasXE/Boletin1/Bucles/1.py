'''1. Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces.'''

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Mostrar la palabra 10 veces
for i in range(1,11):
    print(f"{i}: {palabra}")