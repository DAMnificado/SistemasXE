'''
Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
coste final total.
'''

import random

numBarraTu = input("Hola buenos dias!¿Cuántas barras quieres?: ")

precioBarraBuena= 3.49
rebaja= float(3.49 * 0.6)
precioBarraResesa = float(3.49 - rebaja)


tuPrecioSinRebaja= float(numBarraTu) * precioBarraBuena
tuPrecioRebajado= float(numBarraTu) * precioBarraResesa

tuDescuento= tuPrecioSinRebaja - tuPrecioRebajado


barrasAyer=random.randint(1,10)
print(f"Ayer sobraron {barrasAyer} barras de pan")

clientesHoy=random.randint(1,10)
print(f"Hoy han venido ya {clientesHoy} clientes, y ",end="")
contador=0

for i in range(clientesHoy):
    numBarraEllos = random.randint(1, 3)
    contador += numBarraEllos

print(f"en total han comprado {contador} barras")


if contador >= barrasAyer:
    print(f"Lo siento, no hay barras resesas, son: {tuPrecioSinRebaja:.2f} euros")
    print(f"Te recuerdo que cada una cuesta {precioBarraBuena} y has comprado {numBarraTu}")
elif barrasAyer >= clientesHoy:
    print(f"Estás de suerte, queda pan reseso, son : {tuPrecioRebajado:.2f} euros")
    print(f"Te recuerdo que cada barra resesa cuesta {precioBarraResesa:.2f} euros, y has comprado {numBarraTu}")
    print(f"Si...está algo durillo pero te estás ahorando {tuDescuento:.2f} euros")

    










