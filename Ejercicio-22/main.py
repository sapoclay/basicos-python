'''
Escribir un programa que encuentre el segundo número más grande en una lista.
Introducir la ordenación de listas y el uso de índices.

'''

def segundo_mas_grande(lista):
    lista.sort()
    return lista[-2]

lista = [14, 32, 23, 42, 45, 46, 77, 18, 449, 110]

print(segundo_mas_grande(lista))