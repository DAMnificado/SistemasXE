'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

# Bucle externo para el factor del 1 al 10
for factor in range(1, 11):
    # Bucle interno para el multiplicador del 1 al 10
    for multiplicador in range(1, 11):
        # Calcular y mostrar el resultado de la multiplicación
        producto = factor * multiplicador
        print(f"{factor} x {multiplicador} = {producto}")

    # Imprimir una línea en blanco después de cada tabla de multiplicar
    print()
