
from Simulador import Simulador

if __name__ == "__main__":
    tiempoDeLlegada = int(input("Ingresar tiempo de llegada de clientes: "))
    tiempoDeAtencion = int(input("Ingresar tiempo de atencion de cajero: "))
    tiempoDeSimulacion = int(input("Ingresar tiempo de duracion de la simulacion: "))
    UnSimulador = Simulador(tiempoDeLlegada,tiempoDeAtencion,tiempoDeSimulacion)
    UnSimulador.Simular()