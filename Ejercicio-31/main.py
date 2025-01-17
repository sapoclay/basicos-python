import os
import platform

def es_numero(valor):
    """Verifica si un valor es un número entero o flotante."""
    try:
        float(valor)  # Si se puede convertir a flotante, es un número
        return True
    except ValueError:
        return False

"""
    Agrega un nuevo producto al inventario.

    Verifica si el producto ya existe y si los datos ingresados son válidos.
    Si el producto es nuevo, lo añade al diccionario almacen con sus detalles.
"""
def agregar_producto(almacen, nombre, cantidad, precio, stock_minimo):
    nombre = nombre.lower()
    if not es_numero(cantidad) or float(cantidad) <= 0:
        print("La cantidad debe ser un número positivo.")
        pausar()
        return
    if not es_numero(precio) or float(precio) <= 0:
        print("El precio debe ser un número positivo.")
        pausar()
        return
    if not es_numero(stock_minimo) or float(stock_minimo) < 0:
        print("El stock mínimo debe ser un número mayor o igual a 0.")
        pausar()
        return
    
    cantidad = int(cantidad)
    precio = float(precio)
    stock_minimo = int(stock_minimo)

    if nombre in almacen:
        print(f"El producto '{nombre}' ya existe.")
        pausar()
    else:
        almacen[nombre] = {'cantidad': cantidad, 'precio': precio, 'stock_minimo': stock_minimo}
        print(f"Producto '{nombre}' añadido correctamente.")
        pausar()

"""
    Registra una entrada de productos al inventario.

    Aumenta la cantidad del producto existente en el inventario.
"""
def registrar_entrada(almacen, nombre, cantidad):
    nombre = nombre.lower()
    if not es_numero(cantidad) or int(cantidad) <= 0:
        print("La cantidad debe ser un número positivo.")
        pausar()
        return
    cantidad = int(cantidad)
    
    if nombre in almacen:
        almacen[nombre]['cantidad'] += cantidad
        print(f"Se han añadido {cantidad} unidades de '{nombre}'.")
        pausar()
    else:
        print(f"El producto '{nombre}' no existe en el almacén. Añádelo primero.")
        pausar()

"""
    Registra una salida de productos del inventario.

    Disminuye la cantidad del producto existente en el inventario,
    siempre y cuando haya suficiente stock.
"""
def registrar_salida(almacen, nombre, cantidad):
    nombre = nombre.lower()
    if not es_numero(cantidad) or int(cantidad) <= 0:
        print("La cantidad debe ser un número positivo.")
        pausar()
        return
    cantidad = int(cantidad)
    
    if nombre in almacen:
        if almacen[nombre]['cantidad'] >= cantidad:
            almacen[nombre]['cantidad'] -= cantidad
            print(f"Se han retirado {cantidad} unidades de '{nombre}'.")
            pausar()
        else:
            print(f"No hay suficiente stock de '{nombre}'.")
            pausar()
    else:
        print(f"El producto '{nombre}' no existe en el almacén.")
        pausar()

"""
    Muestra el inventario actual guardado en el diccionario almacen.
"""
def mostrar_inventario(almacen):
    limpiar()
    print("\nInventario actual:\n")
    
    for nombre, datos in almacen.items():
        print(f"Producto: {nombre}")
        print(f"Cantidad: {datos['cantidad']}")
        print(f"Precio: {datos['precio']}€")
        print(f"Stock mínimo: {datos['stock_minimo']}")
        print("-------------------------------------")
    pausar()

"""
    Verifica si algún producto tiene stock por debajo del nivel mínimo.
"""
def verificar_stock_minimo(almacen):
    limpiar()
    print("\nProductos con stock bajo el mínimo:\n")
    for nombre, datos in almacen.items():
        if datos['cantidad'] < datos['stock_minimo']:
            print(f"- {nombre}: Cantidad actual {datos['cantidad']}, Stock mínimo {datos['stock_minimo']}")
    pausar()

"""
    Pausa el programa y espera a que el usuario presione Enter.
    Limpia la pantalla después de presionar Enter.
"""
def pausar():
    input("\nPresione Enter para continuar...")
    if platform.system() == "Windows":
        os.system('cls')  # Limpiar pantalla en Windows
    else:
        os.system('clear')  # Limpiar pantalla en Linux y macOS
        
"""
    Función para SOLO limpiar la pantalla
"""
def limpiar():
    if platform.system() == "Windows":
        os.system('cls') 
    else:
        os.system('clear')

"""
    Menú principal y producto guardados en el almacén por defecto.
"""
def menu():
    almacen = {
        'manzanas': {'cantidad': 50, 'precio': 0.5, 'stock_minimo': 10},
        'naranjas': {'cantidad': 30, 'precio': 0.7, 'stock_minimo': 15},
        'platanos': {'cantidad': 4, 'precio': 0.3, 'stock_minimo': 5}
    }
    
    """
        Limpia la pantalla, según el S.O.
    """
    if platform.system() == "Windows":
        os.system('cls') 
    else:
        os.system('clear')
        
    """
        Menú principal del programa.
    """
    while True:
        print("\nMenú principal: \n")
        print("1. Registrar nuevo producto")
        print("2. Registrar entrada de productos")
        print("3. Registrar salida de productos")
        print("4. Mostrar inventario")
        print("5. Verificar stock mínimo")
        print("6. Salir")
        print(" ")
        opcion = input("Selecciona una opción: ")

        """
            Opciones del menú principal.
            Con inserción de datos por parte del usuario.
            Y llamada a las funciones correspondientes.
        """
        if opcion == '1':
            limpiar()
            print("Registrar nuevo producto\n")
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad inicial: ")
            precio = input("Precio: ")
            stock_minimo = input("Stock mínimo: ")
            agregar_producto(almacen, nombre, cantidad, precio, stock_minimo)
                
        elif opcion == '2':
            limpiar()
            print("Registrar entrada de productos\n")
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad a ingresar: ")
            registrar_entrada(almacen, nombre, cantidad)

        elif opcion == '3':
            limpiar()
            print("Registrar salida de productos\n")
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad a retirar: ")
            registrar_salida(almacen, nombre, cantidad)

        elif opcion == '4':
            mostrar_inventario(almacen)

        elif opcion == '5':
            verificar_stock_minimo(almacen)

        elif opcion == '6':
            if platform.system() == "Windows":
                os.system('cls') 
            else:
                os.system('clear')
            
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

""" 
    Inicio del programa
"""
if __name__ == "__main__":
    menu()
