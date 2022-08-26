
from ColaEncadena import ColaEncadenada
from ColaSecuencial import ColaSecuencial
import random
from Paciente import Paciente

class Simulador:
    __tiempoSimulacion = None
    __tiempoAtencionTurnos = None
    __tiempoActualTurnos = None
    __tiempoLlegada = None
    __colaTurnos = None
    __colaEspecialidades = None
    __sumEsperas = None
    __pacienteEnTurnos = None
    __tiempoAtencionEspecialidades = None
    __cantSinTurno = None
    __tiempoActualEspecialidades = []
    __sumEspecialidades = []
    __cantEspecialidadesAtendidas = []
    __cantTurnosAtendidos = None



    def __init__(self,tiempoSimulacion,tiempoLlegada,tiempoAtencionTurnos,tiempoAtencionEspecialidades):
        self.__colaTurnos = ColaEncadenada()
        self.__cantSinTurno = 0
        self.__tiempoSimulacion = tiempoSimulacion
        self.__tiempoLlegada = 1/tiempoLlegada
        self.__colaEspecialidades = []
        self.__tiempoActualEspecialidades = []
        self.__sumEspecialidades = []
        self.__cantEspecialidadesAtendidas = []
        self.__tiempoAtencionEspecialidades = tiempoAtencionEspecialidades
        for i in range(4):
            self.__colaEspecialidades.append(ColaSecuencial(10))
            self.__tiempoActualEspecialidades.append(self.__tiempoAtencionEspecialidades+1)
            self.__sumEspecialidades.append(0)
            self.__cantEspecialidadesAtendidas.append(0)
        self.__tiempoAtencionTurnos = tiempoAtencionTurnos
        
        self.__tiempoActualTurnos = tiempoAtencionTurnos + 1
        self.__cantTurnosAtendidos = 0 

    
    def Simula(self):
        reloj = 0
        for reloj in range(self.__tiempoSimulacion):
           
            self.llegaCliente(reloj)
            self.procesarTurno(reloj)
            self.procesarPacientes(reloj)
            
        print("Personas que no pudieron sacar turno: {}".format(self.__cantSinTurno))
        print("Tiempo promedio de espera de turnos: {}".format(self.__sumEsperas/self.__cantTurnosAtendidos))
        for i in range(4):
            promedio = 0
            if self.__cantEspecialidadesAtendidas[i] != 0:
                promedio = self.__sumEspecialidades[i]/self.__cantEspecialidadesAtendidas[i]
            print("Promedio Espera especialidad {}: {}".format(i+1,promedio))


    def llegaCliente(self,reloj):
        num = random.random()
        if num <= (1/self.__tiempoLlegada):
            self.__colaTurnos.Insertar(Paciente(reloj))
    
    
    def procesarTurno(self,reloj):
        if reloj < 60:
            if self.__tiempoActualTurnos == self.__tiempoAtencionTurnos + 1:
                if self.__colaTurnos.vacia() == False:
                    self.__pacienteEnTurnos = self.__colaTurnos.Suprimir()
                    
                    self.__tiempoActualTurnos = self.__tiempoAtencionTurnos
                    
            else:
                self.__tiempoActualTurnos -= 1
                if self.__tiempoActualTurnos == 0:
                    self.__sumEsperas = reloj - self.__pacienteEnTurnos.getTiempoEspera()
                    self.__cantTurnosAtendidos +=1
                    self.__pacienteEnTurnos.setTiempoDeEspera(reloj)
                    if self.__colaEspecialidades[self.__pacienteEnTurnos.getEspecialidad()].lleno() == False:
                        self.__colaEspecialidades[self.__pacienteEnTurnos.getEspecialidad()].Insertar(self.__pacienteEnTurnos)
                    else:
                        self.__cantSinTurno +=1
                        
                    self.__tiempoActualTurnos = self.__tiempoAtencionTurnos + 1
        else:
            if self.__colaTurnos.vacia() == False:
                for i in range(self.__colaTurnos.getCantidad()):
                    self.__colaTurnos.Suprimir()
                    self.__cantSinTurno += 1
                
            
        
        
    def procesarPacientes(self,reloj):
        for i in range(len(self.__colaEspecialidades)):
            if self.__tiempoActualEspecialidades[i] == self.__tiempoAtencionEspecialidades+1:
                if self.__colaEspecialidades[i].vacio() == False:
                    paciente = self.__colaEspecialidades[i].Suprimir()
                    self.__sumEspecialidades[i] += reloj - paciente.getTiempoEspera()
                    self.__tiempoActualEspecialidades[i] = self.__tiempoAtencionEspecialidades
                    self.__cantEspecialidadesAtendidas[i] += 1
            else:
                self.__tiempoActualEspecialidades[i] -= 1
                if self.__tiempoActualEspecialidades[i] == 0:
                    self.__tiempoActualEspecialidades[i] = self.__tiempoAtencionEspecialidades + 1

