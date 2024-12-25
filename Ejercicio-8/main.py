'''
Verificar si un número es positivo, negativo o cero.
Objetivo: Introducir las declaraciones condicionales (if, elif, else)

'''
# Solicitar un número al usuario
num = int(input("Escribe un número: "))

# Función que evalúa el estado del número
def evaluar_numero(n):
    return {
        n > 0: f"El número {n} es un número positivo",
        n < 0: f"El número {n} es un número negativo",
    }.get(True, f"El número {n} es cero")

print(evaluar_numero(num))
