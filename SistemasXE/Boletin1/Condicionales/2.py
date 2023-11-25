'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas.'''

# Almacenar la contraseña en una variable
contrasena_guardada = "123 AbC"

# Preguntar al usuario por la contraseña
contrasena_usuario = input("Ingrese la contraseña: ")

# Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
if contrasena_guardada.lower() == contrasena_usuario.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")