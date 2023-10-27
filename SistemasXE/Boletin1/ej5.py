"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y
el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

numHours = float(input("How many hours did you work?"))
mPerHour = float(input("How much you earn per hour?"))

print("Your salary this month ",(numHours*mPerHour))