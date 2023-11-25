'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es
mayor de edad o no.'''
try:
    # Solicitar al usuario su edad
    edad = int(input("Ingrese su edad: "))

    # Verificar si es mayor de edad
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted no es mayor de edad.")

except ValueError:
    print("Por favor, ingrese un valor numérico válido.")