'''Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.'''


precioProducto = float(input("Precio?: "))
precioProducto=round(precioProducto,2)

precioProducto=str(precioProducto)

euros,centimos=precioProducto.split('.')
print("Euros:" , euros)
print("Centimos:" , centimos)
