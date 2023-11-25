'''Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****'''


altura = int(input("Ingrese un número entero para la altura del triángulo: "))

'''La expresión print('*' * i) consiste en el carácter '*' repetido i veces.'''

for i in range(1, altura + 1):
    print('*' * i)