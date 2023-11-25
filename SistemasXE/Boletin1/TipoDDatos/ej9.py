'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión
'''

canInver = float(input("Cantidad a invertir: "))
interes = float(input("A cuanto interés?: "))
numA = float(input("En cuantos años: "))

def beneficio(canInver,interes,numA):
    montonAcumulado = canInver * (1 + (interes / 100)) ** numA
    return montonAcumulado - canInver


beneficioCalculado=beneficio(canInver,interes,numA)

beneficioRedondeado=round(beneficioCalculado,2)

print(f"Tu beneficio es: {beneficioRedondeado} euros")

