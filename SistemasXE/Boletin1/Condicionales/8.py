'''En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario.'''

try:
    # Solicitar al usuario su puntuación
    puntuacion = float(input("Ingrese su puntuación: "))

    # Verificar si la puntuación es válida
    if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
        # Determinar el nivel de rendimiento y calcular el dinero correspondiente
        if puntuacion == 0.0:
            nivel = "Inaceptable"
            dinero = 0
        elif puntuacion == 0.4:
            nivel = "Aceptable"
            dinero = 2400 * puntuacion
        else:
            nivel = "Meritorio"
            dinero = 2400 * puntuacion

        # Mostrar el nivel de rendimiento y la cantidad de dinero
        print(f"Su nivel de rendimiento es {nivel}.")
        print(f"Usted recibirá {dinero}€.")
    else:
        print("Puntuación no válida. La puntuación debe ser 0.0, 0.4 o 0.6 o más.")

except ValueError:
    print("Por favor, ingrese una puntuación numérica válida.")
