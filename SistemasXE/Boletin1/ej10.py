'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.

deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda.

Cada payaso pesa 112 g y cada muñeca 75 g.

Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
'''


def muñecas(numPayasos, numMuñecas):

    pesoTotal = (numPayasos*112) + (numMuñecas*75)
    return pesoTotal

numPayasos=input("Cuantos payasos vendiste?: ")
numMuñecas=input("Cuantos muñecas vendiste?: ")

print(muñecas(1,1))