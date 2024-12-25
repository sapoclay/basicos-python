'''
Invertir una cadena de texto usando un bucle for.
Objetivo: Enseñar la manipulación de cadenas y la iteración mediante bucles.

'''

# Solicitar una cadena de texto al usuario
cadena = input("Escribe una cadena de texto: ")

# Inicializar una cadena vacía para almacenar el resultado
cadena_invertida = ""

# Iterar sobre la cadena de texto en orden inverso
for letra in cadena:
    cadena_invertida = letra + cadena_invertida
    
# Mostrar la cadena invertida
print(f"Cadena invertida: {cadena_invertida}")