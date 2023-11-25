'''Escribir un programa que pregunte el nombre el un producto, su precio y un
número de unidades y muestre por pantalla una cadena con el nombre del
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el
número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2
decimales.'''



def obtener_nombre_valido():
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto.isalpha():
            return nombre_producto
        else:print("No es válido")

def obtener_precio_unitario():

    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto (maximo 6 dígitos): "))
            if precio_unitario < 1_000_000:
                break
            else:
                print("El precio no puede llegar al millon")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def obtener_num_Unidades():

    while True:
        try:
            num_unidades = float(input("Ingrese el numero de unidades (maximo 3 digitos): "))
            if num_unidades <= 0:
                print("Error: Las unidades no pueden ser menores o iguales a 0.")
            elif num_unidades >= 1000:
                print("Error: Las unidades no pueden ser mayores o iguales a 1000.")
            elif num_unidades % 1 != 0:
                print("Error: Las unidades no pueden contener decimales.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")


nombre=obtener_nombre_valido()
precio=obtener_precio_unitario()
numUnidades=obtener_num_Unidades()
coste = float(float(precio) * int(numUnidades))

print(f"Producto: {nombre} Precio: {precio:09.2f}, número de unidades: {numUnidades:03d}, coste total: {coste:011.2f}")
