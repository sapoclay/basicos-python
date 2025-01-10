import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    """
    Clase que implementa la lógica de una calculadora básica.

    Métodos:
        agregar_caracter(caracter): Agrega un carácter a la pantalla de la calculadora.
        borrar(): Borra el último carácter de la pantalla.
        calcular(): Realiza el cálculo de la expresión mostrada en la pantalla.
        limpiar(): Limpia la pantalla de la calculadora.
        actualizar_pantalla(): Actualiza la pantalla de la calculadora.
    """
    def __init__(self, pantalla):
        """Inicializa la calculadora con una expresión vacía y referencia a la pantalla."""
        self.expresion = ""
        self.pantalla = pantalla  # Referencia a la pantalla de la calculadora

    def agregar_caracter(self, caracter):
        """Agrega un carácter a la expresión."""
        self.expresion += str(caracter)
        self.actualizar_pantalla()

    def borrar(self):
        """Borra el último carácter de la expresión."""
        self.expresion = self.expresion[:-1]
        self.actualizar_pantalla()

    def calcular(self):
        """Evalúa la expresión matemática y muestra el resultado."""
        try:
            # Evaluamos la expresión y la asignamos como resultado
            self.expresion = str(eval(self.expresion))
        except Exception:
            self.expresion = "Error"
        self.actualizar_pantalla()

    def limpiar(self):
        """Limpia la expresión de la calculadora."""
        self.expresion = ""
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        """Actualiza la pantalla de la calculadora."""
        self.pantalla.config(text=self.expresion)  # Aquí usamos la referencia de la pantalla


class InterfazCalculadora:
    """
    Clase que gestiona la interfaz gráfica de la calculadora.

    Métodos:
        crear_botones(): Crea y organiza los botones de la calculadora.
        configurar_pantalla(): Configura la pantalla donde se muestra la expresión.
    """
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica de la calculadora.

        Args:
            root (tk.Tk): Ventana principal de la aplicación.
        """
        # Crear la pantalla de la calculadora con fondo blanco y borde
        self.pantalla = ttk.Label(root, text="", anchor="e", font=("Helvetica", 20), width=15, background="white", relief="sunken", borderwidth=2) #relief="sunken" y borderwidth=2 para darle un borde a la pantalla
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Crear la calculadora, pasando la referencia de la pantalla
        self.calculadora = Calculadora(self.pantalla)

        # Configuración de la ventana principal
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x250")  # Ajustamos el tamaño de la ventana a más ancha y menos alta
        self.root.resizable(False, False) # Evitamos que se pueda redimensionar la ventana

        # Crear los botones
        self.crear_botones()

    def crear_botones(self):
        """Crea y organiza los botones de la calculadora."""
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("Borrar", 5, 1), ("^", 5, 2), ("√", 5, 3)
             
        ]

        # Crear los botones y organizarlos en la grilla
        for texto, fila, columna in botones:
            if texto == "=":
                btn = ttk.Button(self.root, text=texto, width=10, command=self.calcular)
            elif texto == "C":
                btn = ttk.Button(self.root, text=texto, width=10, command=self.limpiar)
            elif texto == "Borrar":
                btn = ttk.Button(self.root, text=texto, width=10, command=self.borrar)
            elif texto == "^":
                btn = ttk.Button(self.root, text=texto, width=10, command=self.agregar_exponente)
            elif texto == "√":
                btn = ttk.Button(self.root, text=texto, width=10, command=self.agregar_raiz)
            else:
                btn = ttk.Button(self.root, text=texto, width=10, command=lambda t=texto: self.agregar_caracter(t))
            btn.grid(row=fila, column=columna, padx=5, pady=5)

    def agregar_caracter(self, caracter):
        """Llama al método agregar_caracter de la calculadora."""
        self.calculadora.agregar_caracter(caracter)

    def borrar(self):
        """Llama al método borrar de la calculadora."""
        self.calculadora.borrar()

    def limpiar(self):
        """Llama al método limpiar de la calculadora."""
        self.calculadora.limpiar()

    def calcular(self):
        """Llama al método calcular de la calculadora."""
        self.calculadora.calcular()

    def agregar_exponente(self):
        """Agrega el operador de exponente (^) a la expresión."""
        self.calculadora.agregar_caracter("**")

    def agregar_raiz(self):
        """Agrega la operación de raíz cuadrada (√) a la expresión."""
        self.calculadora.agregar_caracter("math.sqrt(")  # Utiliza la función sqrt de math


# Crear la ventana principal y ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCalculadora(root)
    root.mainloop()
