# Crear una lista de números del 1 al 10 y calcular la suma
# Objetivo: Introducir la creación de listas, la iteración básica y el uso de funciones integradas como sum().

# Solicitar el número final de la lista
num = int(input("Escribe el número final de la lista: "))

# Crear una lista desde el 1 hasta el número escrito por el usuario
lista = list(range(1, num + 1))

# Calcular la suma de los elementos de la lista
suma = sum(lista)

# Mostrar el resultado
print(f"La suma de los números del 1 al {num} es {suma}")