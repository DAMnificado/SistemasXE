'''Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''


n = int(input("Ingrese un número entero para la altura del triángulo: "))

# Imprimir el triángulo rectángulo
for i in range(1, n , 2):

    for j in range(i, 0, -2):
        print(j, end=' ')
    print()
