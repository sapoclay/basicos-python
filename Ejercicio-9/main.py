'''
Crear una lista de números pares del 1 al 20 usando un bucle for.
Objetivo: Enseñar cómo usar bucles (for) y lógica condicional.

'''

# Crear una lista vacía para almacenar los números pares
numeros_pares = []

# Iterar sobre los números del 1 al 20
for i in range(1, 21):
    # Verificar si el número es par
    if i % 2 == 0:
        # Agregar el número a la lista
        numeros_pares.append(i)

# Mostrar la lista de números pares
print(f"Números pares del 1 al 20: {numeros_pares}")
