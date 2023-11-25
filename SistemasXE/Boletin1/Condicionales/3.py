'''Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.'''

def calcular():
    try:
        # Solicitar al usuario dos números
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor: "))

        # Verificar si el divisor es cero
        if divisor == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = dividendo / divisor
            return print(f"El resultado es: {round(resultado,2)}")

    except ValueError:
        print("Por favor, ingrese números válidos.")


calcular()