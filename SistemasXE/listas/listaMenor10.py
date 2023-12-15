import random

def main():
    # Solicitar al usuario el tamaño del array
    n = int(input("Ingrese la cantidad de posiciones para el array: "))

    # Crear un array con números aleatorios
    mi_array = [random.randint(1, 20) for _ in range(n)]

    # Mostrar el array original
    print("Array original:", mi_array)

    # Filtrar y mostrar solo los números menores de 10
    numeros_menores_10 = [num for num in mi_array if num < 10]
    print("Números menores de 10:", numeros_menores_10)


if __name__ == '__main__':
    main()