'''
Encontrar la longitud de la palabra más larga en una lista.
Enseñar la iteración sobre listas y el cálculo de la longitud de cadenas.

'''

# Definimos la lista de palabras
palabras = ['hola', 'mundo', 'python', 'programacion', 'lenguaje', 'programa']

# Definimos una variable para almacenar la longitud de la palabra más larga
palabra_mas_larga = max(palabras, key=len)

# Mostramos la palabra más larga
print('La palabra más larga es:', palabra_mas_larga)