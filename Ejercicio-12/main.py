'''
Contar el número de vocales en una cadena de texto.
Objetivo: Practicar bucles, funciones, condicionales y trabajar con cadenas.

'''

def contar_vocales(cadena):
    vocales = 'aeiou'
    contador = 0
    for letra in cadena:
        if letra.lower() in vocales:
            contador += 1
    return contador

resultado = contar_vocales(input('Introduce una cadena de texto: '))    

print(f'El número de vocales en la cadena de texto es: {resultado}')