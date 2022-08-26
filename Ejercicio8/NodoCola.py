class NodoCola:
    __paciente = None
    __siguiente = None

    def __init__(self,Paciente):
        self.__paciente = Paciente
        self.__siguiente = None
    
    def getPaciente(self):
        return self.__paciente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente