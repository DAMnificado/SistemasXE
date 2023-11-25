'''Escribir un programa que pida al usuario que introduzca una frase en la consola y
muestre por pantalla la frase invertida.'''

frase=input("Dime un frase bonita: ")

frase_separada=frase.split()

frase_separada_reves=frase_separada[::-1]

fraseFinal = ''.join(frase_separada_reves)
print(fraseFinal)
