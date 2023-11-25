'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
usuario tiene que tributar o no.'''
try:
    # Solicitar al usuario su edad e ingresos mensuales
    edad = int(input("Ingrese su edad: "))
    ingresos_mensuales = float(input("Ingrese sus ingresos mensuales en euros: "))

    # Verificar las condiciones para tributar
    if edad > 16 and ingresos_mensuales >= 1000:
        print("Usted debe tributar.")
    else:
        print("Usted no tiene que tributar.")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")