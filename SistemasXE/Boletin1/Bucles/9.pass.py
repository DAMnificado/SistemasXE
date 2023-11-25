'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.'''
# Almacenar la contraseña en una variable
miContraseña = "123"

# Solicitar al usuario que ingrese la contraseña
while True:
    intento = input("Ingrese la contraseña: ")

    if intento == miContraseña:
        print("¡Contraseña correcta! Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Vuelva a intentarlo.")