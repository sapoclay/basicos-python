# Calcular el factorial de un número usando un bucle while.
# Objetivo: Introducir bucles while y control básico de bucles.
# El factorial es el producto de todos los enteros positivos desde 1 hasta el número en cuestión.

# Solicitar un número al usuario
num = int(input("Escribe un número para calcular su factorial: "))

# Inicializamos variables
factorial = 1
i = 1

# Usar un bucle while para calcular el factorial
while i <= num:
    factorial *= i
    i += 1
    
# Mostrar el resultado
print(f"El factorial de {num} es {factorial}")