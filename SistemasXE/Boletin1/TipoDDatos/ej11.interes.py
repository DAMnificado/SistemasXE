'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
cada cantidad a dos decimales.
'''

def ahorros(liquidez, interes):
    for i in range(1, 4):
        beneficio = liquidez * (interes / 100)
        total = liquidez + beneficio
        print(f"En tu cuenta con {round(liquidez, 2)} euros, a {interes}% de interés fijo en el {i}º año, obtendrás {round(beneficio, 2)} euros de beneficio")
        liquidez = total

    return liquidez

liquidez = 100
interes = 5
total_final = ahorros(liquidez, interes)
print(f"La cantidad final que tendrás en tu cuenta al final del tercer año será: {round(total_final, 2)} euros")