'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).'''

# Pedir al usuario su edad
edad = int(input("Ingrese su edad: "))

# Mostrar los años que ha cumplido
for i in range(1, edad+1):
   print(i)