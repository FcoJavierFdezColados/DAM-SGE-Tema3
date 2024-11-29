"""
                   Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del
país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un
número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

print("Introduce tu número de teléfono con el código de pais y la extensión. Ejemplo: +34-913724710-56")
telephone_number = input("Introduce el número de teléfono: ")

if telephone_number.count("-") == 2:
    telephone_number = telephone_number.split("-")
    if (len(telephone_number[1]) > 2):
        print(f"Su número de telefono es: {telephone_number[1]}")
    if (len(telephone_number[0]) > 2):
        print(f"Su código de pais es: {telephone_number[0]}")

    if(len(telephone_number[1]) == 2):
        print(f"Su extension es: {telephone_number[2]}")
else:
    print("Recuerda que debe contener el código de pais con y la extensión separados por un guión cada uno.")
    print("El número de teléfono debe contener dos guiones exactamente.")

