'''
Crear un bucle anidado para imprimir una tabla de multiplicar para los números del 1 al 9.
Enseñar el uso de bucles anidados y operaciones aritméticas básicas.

'''

# Bucle anidado para imprimir una tabla de multiplicar para los números del 1 al 9.

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=",
                i * j)
    print()