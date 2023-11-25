'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.'''

while True:
    entrada_usuario = input("Escribe algo (o escribe 'salir' para terminar): ")

    if entrada_usuario.lower() == "salir":
        print("¡Hasta luego!")
        break
    else:
        print(entrada_usuario)