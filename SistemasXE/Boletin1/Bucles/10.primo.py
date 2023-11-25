'''Escribir un programa que pida al usuario un número entero y muestre por pantalla
si es un número primo o no.'''

def esPrimo(numero):
    cont = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1

    if cont == 2:
        return print(numero)



for i in range(1,101):
    esPrimo(i)