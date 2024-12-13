"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y
muestre por pantalla cada uno de los productos en una línea distinta.
"""
productos = input("Introduce la lista de la compra separando los productos por comas.")
productos_individuales = productos.split(",")

for producto in productos_individuales:
    print(producto.replace(" ", ""))