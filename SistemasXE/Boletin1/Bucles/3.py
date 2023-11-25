'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.'''

# Solicitar al usuario un número entero positivo
while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero > 0:
        break
    else:
        print("Por favor, ingrese un número entero positivo.")


# Mostrar los números impares hasta el número ingresado
impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
resultado = ", ".join(impares)
print(f"Números impares hasta {numero}: {resultado}")
