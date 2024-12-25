'''
Crear un diccionario para contar la cantidad de veces que aparece cada carácter en
una cadenauna cadena.
Enseñar el uso de diccionarios y la iteración sobre cadenas.

'''

# Definir la cadena de texto
texto = "Josefino Finito de la Calle"
# Crear un diccionario vacío para almacenar los conteos
conteos = {}
# Iterar sobre cada carácter en la cadena
for char in texto:
    if char in conteos:
        conteos[char] += 1
    else:
        conteos[char] = 1
# Mostrar el diccionario con los conteos
print(conteos)