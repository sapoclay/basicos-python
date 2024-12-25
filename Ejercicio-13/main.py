'''
Encontrar el número máximo en una lista sin usar funciones incorporadas.
Enseñar cómo iterar a través de una lista y comparar valores.

'''

# Definir la lista de números
numbers = [10, 22, 53, 42, 5, 78, 14, 28, 19, 12]

# Inicializar el valor máximo como el primero número de la lista
max_number = numbers[0]

# Iterar a través de la lista
for number in numbers:
    # Comparar el número actual con el valor máximo
    if number > max_number:
        # Actualizar el valor máximo si el número actual es mayor
        max_number = number
        
# Imprimir el número máximo
print(f'El número máximo es: {max_number}')