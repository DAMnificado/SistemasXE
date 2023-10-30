'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión
'''

def beneficio(canInver,interes,numA):
    capital = (canInver+interes) * numA
    return capital

print(beneficio(100,0.2,2))

