'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

 Ingredientes vegetarianos: Pimiento y tofu.
 Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza
elegida es vegetariana o no y todos los ingredientes que lleva.'''

# Solicitar al usuario si quiere una pizza vegetariana o no

# Verificar la elección del usuario
while True:
    # Solicitar al usuario si quiere una pizza vegetariana o no
    opcion = input("¿Quiere una pizza vegetariana? (Sí/No): ")

    if opcion.lower() == "si":
        print("Ingredientes vegetarianos disponibles:")
        print("1. Pimiento")
        print("2. Tofu")

        while True:
            ingrediente_elegido = input("Elija un ingrediente (1 o 2): ")
            if ingrediente_elegido == "1":
                ingredientes = ["Mozzarella", "Tomate", "Pimiento"]
                tipo_pizza = "Vegetariana"
                break
            elif ingrediente_elegido == "2":
                ingredientes = ["Mozzarella", "Tomate", "Tofu"]
                tipo_pizza = "Vegetariana"
                break
            else:
                print("Opción no válida. Por favor, elija 1 o 2.")

        break

    elif opcion.lower() == "no":
        print("Ingredientes carnívoros disponibles:")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")

        while True:
            ingrediente_elegido = input("Elija un ingrediente (1, 2 o 3): ")
            if ingrediente_elegido == "1":
                ingredientes = ["Mozzarella", "Tomate", "Peperoni"]
                tipo_pizza = "Cárnica"
                break
            elif ingrediente_elegido == "2":
                ingredientes = ["Mozzarella", "Tomate", "Jamón"]
                tipo_pizza = "Cárnica"
                break
            elif ingrediente_elegido == "3":
                ingredientes = ["Mozzarella", "Tomate", "Salmón"]
                tipo_pizza = "Cárnica"
                break
            else:
                print("Opción no válida. Por favor, elija 1, 2 o 3.")

        break

    else:
        print("Respuesta no válida. Por favor, responda con 'Sí' o 'No'.")

ingredientes_str = ', '.join(ingredientes[:-1]) + f" y {ingredientes[-1]}"
print(f"Tu pizza es '{tipo_pizza}' y lleva: {ingredientes_str}")
print(f"¿Como? claro, el resto de ingredientes son default, pero el {ingredientes[2]} es especial")



