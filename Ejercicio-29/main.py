import time
def temporizador(func):
    def envoltura():
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
    return envoltura
@temporizador
def funcion_demorada():
    time.sleep(2)
funcion_demorada()