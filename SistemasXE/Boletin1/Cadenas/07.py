# Pedir al usuario que ingrese su correo electrónico
correo_original = input("Ingresa tu correo electrónico: ")

# Dividir el correo electrónico en nombre de usuario y dominio
nombre_usuario, dominio = correo_original.split("@")

# Crear un nuevo correo con el mismo nombre de usuario y dominio ceu.es
nuevo_correo = str(nombre_usuario) + "@ceu.es"

# Mostrar el resultado
print("Correo con dominio ceu.es:", nuevo_correo)