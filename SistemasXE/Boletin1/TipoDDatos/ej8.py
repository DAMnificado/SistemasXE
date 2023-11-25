'''
Escribir un programa que pida al usuario dos números
enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto
<r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r>
son el cociente y el resto de la división entera respectivamente.
'''


n = float(input("Dime un numero: "))
m = float(input("Dime un numero: "))

def ejercicio8(n, m):
    div = n / m
    resto = n % m
    return f'Resultado de la división tus números: {div} , resto de la operación: {resto}'

print(ejercicio8(n, m))


