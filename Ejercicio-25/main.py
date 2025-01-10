import tkinter as tk
from tkinter import ttk

class Cronometro:
    """
    Clase que implementa la lógica de un cronómetro básico.

    Métodos:
        iniciar(): Inicia o reanuda el cronómetro.
        pausar(): Detiene temporalmente el cronómetro.
        reiniciar(): Resetea el cronómetro a 0.
        obtener_tiempo_actual(): Obtiene el tiempo actual en segundos desde el sistema.
        obtener_tiempo(): Calcula el tiempo transcurrido del cronómetro.
    """
    def __init__(self):
        """Inicializa el cronómetro con valores predeterminados."""
        self.tiempo_inicial = 0
        self.tiempo_acumulado = 0
        self.corriendo = False

    def iniciar(self):
        """Inicia o reanuda el cronómetro."""
        if not self.corriendo:
            self.tiempo_inicial = self.obtener_tiempo_actual()
            self.corriendo = True

    def pausar(self):
        """Pausa el cronómetro y acumula el tiempo transcurrido."""
        if self.corriendo:
            self.tiempo_acumulado += self.obtener_tiempo_actual() - self.tiempo_inicial
            self.corriendo = False

    def reiniciar(self):
        """Reinicia el cronómetro, estableciendo el tiempo acumulado en 0."""
        self.tiempo_inicial = 0
        self.tiempo_acumulado = 0
        self.corriendo = False

    def obtener_tiempo_actual(self):
        """
        Obtiene el tiempo actual en segundos con precisión milimétrica.

        Returns:
            float: Tiempo actual en segundos.
        """
        return tk._default_root.tk.call('clock', 'milliseconds') / 1000

    def obtener_tiempo(self):
        """
        Calcula el tiempo transcurrido en el cronómetro.

        Returns:
            float: Tiempo transcurrido en segundos.
        """
        if self.corriendo:
            return self.tiempo_acumulado + (self.obtener_tiempo_actual() - self.tiempo_inicial)
        return self.tiempo_acumulado

class InterfazCronometro:
    """
    Clase que gestiona la interfaz gráfica del cronómetro.

    Métodos:
        iniciar(): Inicia el cronómetro.
        pausar(): Pausa el cronómetro.
        reiniciar(): Reinicia el cronómetro.
        actualizar_tiempo(): Actualiza la etiqueta de tiempo en la interfaz.
    """
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica del cronómetro.

        Args:
            root (tk.Tk): Ventana principal de la aplicación.
        """
        self.cronometro = Cronometro()

        # Configuración de la ventana principal
        self.root = root
        self.root.title("Cronómetro")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Etiqueta para mostrar el tiempo
        self.tiempo_label = ttk.Label(root, text="00:00:00.000", font=("Helvetica", 30))
        self.tiempo_label.pack(pady=20)

        # Botones de control
        botones_frame = ttk.Frame(root)
        botones_frame.pack(pady=10)

        self.iniciar_btn = ttk.Button(botones_frame, text="Iniciar", command=self.iniciar)
        self.iniciar_btn.grid(row=0, column=0, padx=5)

        self.pausar_btn = ttk.Button(botones_frame, text="Pausar", command=self.pausar)
        self.pausar_btn.grid(row=0, column=1, padx=5)

        self.reiniciar_btn = ttk.Button(botones_frame, text="Reiniciar", command=self.reiniciar)
        self.reiniciar_btn.grid(row=0, column=2, padx=5)

        # Actualizar la etiqueta del tiempo
        self.actualizar_tiempo()

    def iniciar(self):
        """Llama al método iniciar del cronómetro."""
        self.cronometro.iniciar()

    def pausar(self):
        """Llama al método pausar del cronómetro."""
        self.cronometro.pausar()

    def reiniciar(self):
        """Llama al método reiniciar del cronómetro."""
        self.cronometro.reiniciar()

    def actualizar_tiempo(self):
        """
        Actualiza la etiqueta de tiempo en la interfaz gráfica.

        La función se ejecuta periódicamente cada 10 ms para reflejar los cambios
        en el tiempo en tiempo real.
        """
        tiempo_total = self.cronometro.obtener_tiempo()
        horas, resto = divmod(int(tiempo_total), 3600)
        minutos, resto = divmod(resto, 60)
        segundos = int(resto)
        milisegundos = int((tiempo_total - int(tiempo_total)) * 1000)
        tiempo_formateado = f"{horas:02}:{minutos:02}:{segundos:02}.{milisegundos:03}"
        self.tiempo_label.config(text=tiempo_formateado)

        # Llamar a esta función nuevamente después de 10 ms
        self.root.after(10, self.actualizar_tiempo)

# Crear la ventana principal y ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCronometro(root)
    root.mainloop()
