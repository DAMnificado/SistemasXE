'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.'''

fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, anio = fecha_nacimiento.split("/")

if len(dia) == 1:
    dia = "0" + dia

if len(mes) == 1:
    mes = "0" + mes

print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)