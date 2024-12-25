'''
Escribe un programa que imprima los números del 1 al 30, pero para múltiplos de 3
imprima “Tres”, para múltiplos de 5 imprima “Cinco” y para múltiplos de ambos imprima “Tres yimprima “Tres”, para múltiplos de 5 
imprima “Cinco” y para múltiplos de ambos imprima “Tres y Cinco”.

'''

# Iterar sobre los números del 1 al 30
for i in range(1, 31):
    # Comprobar si el número es múltiplo de 3 y de 5
    if i % 3 == 0 and i % 5 == 0:
        print("Tres y Cinco")
    # Comprobar si el número es múltiplo de 3
    elif i % 3 == 0:
        print("Tres")
    # Comprobar si el número es múltiplo de 5
    elif i % 5 == 0:
        print("Cinco")
    # Si no es múltiplo de 3 ni de 5, imprimir el número
    else:
        print(i)