'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.'''

letra = input("Ingrese una letra: ")
frase = input("Ingrese una frase: ")

contador = 0

for caracter in frase:

    if caracter.lower() == letra.lower():
        contador += 1


print(f"La letra '{letra}' aparece {contador} veces en la frase '{frase}'.")