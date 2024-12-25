'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.

'''

cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés porcentual anual: "))
años = int(input("Introduce el número de años: "))

print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))