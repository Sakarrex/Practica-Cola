import random
from ColaSecuencial import ColaSecuencial

class Simulador:
    __cajero = None
    __cola = None
    __frecuenciaLlegada = None
    __tiempoAtencion = None
    __tiempoSimulacion = None
    __tiempoAcualCajero = None
    __maximo = None

    def __init__(self,tiempoLlegada,tiempoAtencion,tiempoSimulacion) -> None:
        self.__cajero = False
        self.__cola = ColaSecuencial()
        self.__frecuenciaLlegada = int(tiempoLlegada)
        self.__tiempoAtencion = int(tiempoAtencion)
        self.__tiempoSimulacion = tiempoSimulacion
        self.__maximo = -1
        self.__tiempoActualCajero = 0
    
    def Simular(self):
        reloj = 0
        tiempocajero = self.__tiempoAtencion
        while reloj <= self.__tiempoAtencion:
            self.llegaCliente()
            if self.__cola.vacio() == False:
                self.ManejaCajero()
            
            

    

    def llegaCliente(self):
        num = random.random()
        if num <= 1/self.__frecuenciaLlegada:
            self.__cola.Insertar(0)
        
    def ManejaCajero(self):
        if self.__cajero == False:
            tiempo = self.__cola.Suprimir()
            self.__cajero = True
            self.__tiempoActualCajero = self.__tiempoAtencion
            if tiempo > self.__maximo:
                self.__maximo = tiempo               
        else:
            self.__tiempoActualCajero -= 1
            if self.__tiempoActualCajero == 0:
                self.__cajero = True
        
        

    
