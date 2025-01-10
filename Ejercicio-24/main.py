import os

def mostrar_menu():
    """Muestra el menú de opciones en la terminal."""
    os.system("cls" if os.name == "nt" else "clear")  # Limpiar pantalla
    print("=== Calculadora ===")
    print("[1] Sumar")
    print("[2] Restar")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Potencia")
    print("[6] Raíz cuadrada")
    print("[7] Salir")
    print("===================")

def pedir_numero(mensaje="Ingrese un número: "):
    """Pide un número al usuario y maneja errores de entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def calcular():
    """Lógica principal de la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':  # Suma
            num1 = pedir_numero("Primer número: ")
            num2 = pedir_numero("Segundo número: ")
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':  # Resta
            num1 = pedir_numero("Primer número: ")
            num2 = pedir_numero("Segundo número: ")
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':  # Multiplicación
            num1 = pedir_numero("Primer número: ")
            num2 = pedir_numero("Segundo número: ")
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':  # División
            num1 = pedir_numero("Primer número: ")
            num2 = pedir_numero("Segundo número: ")
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif opcion == '5':  # Potencia
            base = pedir_numero("Base: ")
            exponente = pedir_numero("Exponente: ")
            print(f"Resultado: {base} ^ {exponente} = {base ** exponente}")
        elif opcion == '6':  # Raíz cuadrada
            num = pedir_numero("Número: ")
            if num >= 0:
                print(f"Resultado: √{num} = {num ** 0.5}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        elif opcion == '7':  # Salir
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    calcular()
