'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
cada cantidad a dos decimales.
'''

def ahorros(liquidez,interes):

    for i in range(1 , 4 , 1):
        total = liquidez * interes * 1
        print(f"En una cuenta con {liquidez} euros , a {interes}% de interés fijo en el año {i} año/-s obtendrás {total}")
        liquidez+=total
    return total


print(ahorros(100,0.04))