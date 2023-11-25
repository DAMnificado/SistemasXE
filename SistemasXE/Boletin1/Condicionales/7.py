'''Los tramos impositivos para la declaración de la renta en un determinado país son
los siguientes:
Renta Tipo impositivo
Menos de 10000€ 5%
Entre 10000€ y 20000€ 15%
Entre 20000€ y 35000€ 20%
Entre 35000€ y 60000€ 30%
Más de 60000€ 45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
tipo impositivo que le corresponde.'''

try:
    # Solicitar al usuario su renta anual
    renta_anual = float(input("Ingrese su renta anual en euros: "))

    # Determinar el tipo impositivo
    if renta_anual < 10000:
        tipo_impositivo = 5
    elif 10000 <= renta_anual <= 20000:
        tipo_impositivo = 15
    elif 20000 <= renta_anual <= 35000:
        tipo_impositivo = 20
    elif 35000 <= renta_anual <= 60000:
        tipo_impositivo = 30
    else:
        tipo_impositivo = 45

    # Mostrar el tipo impositivo correspondiente
    print(f"Su tipo impositivo es {tipo_impositivo}%.")

except ValueError:
    print("Por favor, ingrese un valor numérico válido.")