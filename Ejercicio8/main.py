from Simulador import Simulador

if __name__ == "__main__":
    tiempoSimulacion = int(input("Tiempo de simulacion: "))
    tiempoLlegada = int(input("Tiempo de llegada: "))
    tiempoAtencionTurnos = int(input("Tiempo de atencion de turnos: "))
    tiempoAtencionEspecialidades = int(input("Tiempo de atencion de especialidades: "))

    UnSimulador = Simulador(tiempoSimulacion,tiempoLlegada,tiempoAtencionTurnos,tiempoAtencionEspecialidades)
    UnSimulador.Simula()