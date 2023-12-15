def obtener_nombre_valido():
    while True:
        nombre_usuario = input("Ingresa tu nombre: ")
        if nombre_usuario.replace(" ", "").isalpha():
            return "Hola: " + nombre_usuario
        else:print("No es válido")




nombre_usuario = obtener_nombre_valido()
print(nombre_usuario)