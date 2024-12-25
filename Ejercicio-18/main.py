'''
Usar un bucle para imprimir la secuencia de Fibonacci hasta el décimo término.
Practicar la iteración con bucles y la generación de secuencias.

'''

# Definimos la función fibonacci
def fibonacci(n):
    a, b = 0, 1
    # _ es una variable que no se usa
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Llamamos a la función fibonacci
fibonacci(10)
