'''Escribir un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
primera letra del nombre y de los apellidos en mayúscula. El usuario puede
introducir su nombre combinando mayúsculas y minúsculas como quiera.'''

def procesar_nombre(nombre_completo):

    print("Nombre completo en minúsculas:", nombre_completo.lower())

    print("Nombre completo en mayúsculas:", nombre_completo.upper())

    # Dividir el nombre completo en palabras, en python se entiende que si no pones nada lo separe por espacios
    palabras = nombre_completo.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    nombre_capitalizado = ' '.join(palabras_capitalizadas)
    print("Nombre con la primera letra en mayúscula:", nombre_capitalizado)


# Solicitar el nombre completo al usuario
nombre_usuario = input("Ingresa tu nombre completo: ")

# Llamar a la función para procesar y mostrar el nombre
procesar_nombre(nombre_usuario)