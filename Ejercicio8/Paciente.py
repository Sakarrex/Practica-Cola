import random
class Paciente:
    __nombre = "a"
    __DNI = "1"
    __especialidad = None
    __tiempoEspera = None
    
    def __init__(self,tiempodeEspera) -> None:
        self.__especialidad = random.randint(0,3)
        self.__tiempoEspera = tiempodeEspera
    
    def getTiempoEspera(self):
        return self.__tiempoEspera
    
    def getEspecialidad(self):
        return self.__especialidad
    
    def setTiempoDeEspera(self,tiempodespera):
        self.__tiempoEspera = tiempodespera