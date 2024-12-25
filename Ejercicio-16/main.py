'''
Escribir una función para verificar si una cadena es un palíndromo.
Introducir la manipulación de cadenas y la comparación de texto.

'''

# Definir una función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar los espacios
    cadena = cadena.lower().replace(' ', '')
    
    # Comparar la cadena original con la cadena invertida
    return cadena == cadena[::-1]

# Solicitar al usuario que ingrese una cadena
cadena = input("Ingresa una cadena para verificar si es un palíndromo: ")

# Verificar si la cadena es un palíndromo
if es_palindromo(cadena):
    print(f'La cadena "{cadena}" es un palíndromo.')
else:
    print(f'La cadena "{cadena}" no es un palíndromo.')
    