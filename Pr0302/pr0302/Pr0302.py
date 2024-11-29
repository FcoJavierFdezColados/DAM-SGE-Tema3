# ejercicio 1
'''
                   Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en
líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre = input("Ingrese el nombre del usuario: ")
numero = int(input("Ingrese un numero entero: "))

print( (nombre +"\n" )* numero )