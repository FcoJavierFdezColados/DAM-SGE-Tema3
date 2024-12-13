"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo
electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio vivapython.com.
"""

DOMINIO = "vivapython.com"

email = input("Introduce tu correo electrónico: ")
if email.__contains__("@"):

    email_split = email.split("@")
    print(f"Te acabas de registrar en {DOMINIO} con el email: {email_split[0]}@{DOMINIO}")

else:
    print("El correo debe contener una @")