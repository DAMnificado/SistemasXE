'''Escribir un programa que pregunte el nombre del usuario en la consola y un
número entero e imprima por pantalla en líneas distintas el nombre del usuario
tantas veces como el número introducido.'''

def obtener_nombre_valido():
    while True:
        nombre_usuario = input("Ingresa tu nombre: ")
        if nombre_usuario.isalpha():
            return nombre_usuario
        else:print("No es válido")

def obtener_numero_positivo():
    while True:
        try:
            numero_repeticiones = int(input("Ingresa un número entero positivo: "))
            if numero_repeticiones > 0:
                return numero_repeticiones
            else: print("Tiene que ser un número entero positivo")



        except ValueError:
            print("Eso no es un número")


nombre_usuario = obtener_nombre_valido()
numero_repeticiones = obtener_numero_positivo()

for i in range(numero_repeticiones):
    print(nombre_usuario)