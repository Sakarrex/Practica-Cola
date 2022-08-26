import random
from ColaEncadena import ColaEncadenada

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
        self.__cola = ColaEncadenada()
        self.__frecuenciaLlegada = int(tiempoLlegada)
        self.__tiempoAtencion = int(tiempoAtencion)
        self.__tiempoSimulacion = tiempoSimulacion
        self.__maximo = -1
        self.__tiempoActualCajero = self.__tiempoAtencion + 1
    
    def Simular(self):
        reloj = 0
        while reloj <= self.__tiempoSimulacion:
            self.llegaCliente(reloj)
            self.ManejaCajero(reloj)
            reloj +=1
        print("El tiempo maximo de espera de un cliente fue de: " + str(self.__maximo) + " minutos")
            

    

    def llegaCliente(self,reloj):
        num = random.random()
        if num <= (1/self.__frecuenciaLlegada):
            self.__cola.Insertar(reloj)
        
    def ManejaCajero(self,reloj):
        if self.__tiempoActualCajero == self.__tiempoAtencion + 1:
            if self.__cola.vacia() == False:
                tiempo = reloj - self.__cola.Suprimir()
                self.__tiempoActualCajero = self.__tiempoAtencion
                self.__cajero = True
                if tiempo > self.__maximo:
                    self.__maximo = tiempo
        else:
            self.__tiempoActualCajero -= 1
            if self.__tiempoActualCajero == 0:
                self.__tiempoActualCajero = self.__tiempoAtencion +1
        
        

    
