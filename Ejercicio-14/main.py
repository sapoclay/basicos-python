'''
Usar un bucle para imprimir un patrón de estrellas que forme un triángulo simpe, uno centrado y otro invertido.
Practicar bucles anidados y la creación de patrones.

'''

print("Triángulo de estrellas simple alineado a la izquierda:")

# Solicitar el número de filas al usuario
rows = int(input("Escribe el número de filas: "))

# Generar el triángulo de estrellas
print("\n")
for i in range(1, rows + 1):
    print('*' * i)
    
print("\nTriángulo de estrellas alineado al centro:")
# Generar el triángulo de estrellas alineado al centro
print("\n")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

print("\nTriángulo de estrellas simple invertido:")
# Generar el triángulo de estrellas invertido
print("\n")
for i in range(rows, 0, -1):
    print('*' * i)
