'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''

while True:
    # Solicitar al usuario un número entero positivo
    numero = int(input("Ingrese un número entero positivo: "))

    # Verificar que el número ingresado sea positivo
    if numero > 0:
        break
    else:
        print("Por favor, ingrese un número entero positivo.")

# Mostrar la cuenta atrás desde el número hasta 0
cuenta = [str(i) for i in range(numero, -1, -1)]
cuentaAtras= ", ".join(cuenta)
print(f"Cuenta atrás desde {numero} hasta 0: {cuentaAtras}")