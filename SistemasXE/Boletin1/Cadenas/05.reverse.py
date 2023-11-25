'''Escribir un programa que pida al usuario que introduzca una frase en la consola y
muestre por pantalla la frase invertida.'''

frase=input("Dime un frase bonita: ")

frase_separada=frase.split()
frase_separada.reverse()
print(frase_separada)

fraseFinal=''.join(frase_separada)
print(fraseFinal)
