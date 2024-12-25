# Crear una función que devuelva el cuadrado de un número
# Objetivo: Introducir funciones, argumentos y valores de retorno

# Definir la función para calcular el cuadrado de un número
def cuadrado_num(num):
    return num ** 2

# Solicitar un número al usuario
num = int(input("Escribe un número para calcular su cuadrado: "))

# Mostrar el resultado de la llamada a la función cuadrado_num()
print(f"El cuadrado de {num} es {cuadrado_num(num)}")