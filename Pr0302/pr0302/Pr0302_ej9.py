"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan
con un solo carácter.
"""

fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
fecha_split = fecha.split("/")
print(f"El día introducido es: {fecha_split[0]}, el mes introducido es: {fecha_split[1]}, el año introducido es: {fecha_split[2]}")