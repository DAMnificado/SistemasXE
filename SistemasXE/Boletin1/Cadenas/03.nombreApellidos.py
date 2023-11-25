'''Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de
letras que tienen el nombre.'''

# Preguntar el nombre al usuario
nombre_usuario = input("Ingresa tu nombre completo: ")

# Convertir el nombre a mayúsculas
nombre_en_mayusculas = nombre_usuario.upper()

# Calcular el número de letras en el nombre
numero_letras = sum(letra.isalpha() for letra in nombre_usuario)

# Mostrar el resultado
print(f"{nombre_en_mayusculas} tiene {numero_letras} letras.")