'''
Encontrar la suma de todos los números impares entre 1 y 50.
Usar bucles y condicionales para filtrar y sumar valores.

'''

# Inicializar la suma de los números impares
sumas_impares = 0

# Usar un bucle para iterar a través de los números del 1 al 50
for numero in range(1, 51):
    # Verificar si el número es impar
    if numero % 2 != 0:
        # Sumar el número impar a la suma total
        sumas_impares += numero
        
# Imprimir la suma de los números impares
print(f'La suma de los números impares entre 1 y 50 es: {sumas_impares}')