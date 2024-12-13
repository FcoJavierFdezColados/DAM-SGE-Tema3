"""
Escribir un programa que pregunte el nombre un producto, su precio y un número de unidades y muestre por pantalla una
cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
unidades = float(input("Ingrese la cantidad de unidades."))

print(f"Producto: {producto}, precio: {precio: 6.2f}, unidades: {unidades: 8.2f}")