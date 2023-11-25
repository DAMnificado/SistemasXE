'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo con el
sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior o igual
a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde.'''

# Solicitar al usuario su nombre y sexo
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

# Convertir el nombre a minúsculas para facilitar la comparación
nombre = nombre.lower()
sexo = sexo.upper()

# Verificar las condiciones y determinar el grupo
if (sexo == 'M' and nombre[0] <= 'm') or (sexo == 'F' and nombre[0] > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

# Mostrar el grupo al que pertenece el usuario
print(f"Usted pertenece al grupo {grupo}.")