import time
import threading
import os
import keyboard  # Asegúrate de instalar esta biblioteca: pip install keyboard

class Cronometro:
    def __init__(self):
        self.tiempo_inicio = None
        self.tiempo_acumulado = 0
        self.corriendo = False
        self.mostrando = True

    def iniciar(self):
        if not self.corriendo:
            self.tiempo_inicio = time.time()
            self.corriendo = True

    def pausar(self):
        if self.corriendo:
            self.tiempo_acumulado += time.time() - self.tiempo_inicio
            self.corriendo = False

    def reiniciar(self):
        self.tiempo_inicio = None
        self.tiempo_acumulado = 0
        self.corriendo = False

    def detener(self):
        self.pausar()

    def obtener_tiempo(self):
        if self.corriendo:
            return self.tiempo_acumulado + (time.time() - self.tiempo_inicio)
        return self.tiempo_acumulado

def mostrar_cronometro(cronometro):
    """Actualiza la visualización del cronómetro en tiempo real."""
    while cronometro.mostrando:
        os.system("cls" if os.name == "nt" else "clear")  # Limpiar pantalla
        print(f"Cronómetro: {cronometro.obtener_tiempo():.2f} segundos\n")
        print("Seleccione una opción:")
        print("[i] Iniciar  [p] Pausar  [r] Reiniciar  [d] Detener  [s] Salir")
        time.sleep(0.1)

def main():
    cronometro = Cronometro()
    # Hilo para mostrar el cronómetro continuamente
    hilo_visual = threading.Thread(target=mostrar_cronometro, args=(cronometro,), daemon=True)
    hilo_visual.start()

    print("Use las teclas indicadas para controlar el cronómetro.")
    while True:
        if keyboard.is_pressed('i'):
            cronometro.iniciar()
            time.sleep(0.2)  # Pequeño retraso para evitar múltiples registros
        elif keyboard.is_pressed('p'):
            cronometro.pausar()
            time.sleep(0.2)
        elif keyboard.is_pressed('r'):
            cronometro.reiniciar()
            time.sleep(0.2)
        elif keyboard.is_pressed('d'):
            cronometro.detener()
            time.sleep(0.2)
        elif keyboard.is_pressed('s'):
            cronometro.mostrando = False
            time.sleep(0.2)
            print("Saliendo del cronómetro.")
            break

if __name__ == "__main__":
    main()
