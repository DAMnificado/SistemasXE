'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.'''

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
