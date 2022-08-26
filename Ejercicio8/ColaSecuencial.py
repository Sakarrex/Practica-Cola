import numpy as np
import math
from Paciente import Paciente
class ColaSecuencial:
    __arreglo = None
    __primero = 0
    __ultimo = 0
    __cantidad = 0

    def __init__(self,tamanio):
        self.__arreglo = np.empty(int(tamanio),dtype=Paciente)
        self.__primero = 0
        self.__ultimo = 0
        self.__cantidad = 0
    
    def vacio(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == len(self.__arreglo)
    
    def Insertar(self,valor):
        if self.__cantidad == len(self.__arreglo):
            return
        else:
            self.__arreglo[self.__ultimo] = valor
            self.__ultimo = (self.__ultimo+1)%(len(self.__arreglo))
            self.__cantidad+=1
    
    def Suprimir(self):
        valorDevolver = None
        if self.vacio():
            print("No se puede suprimir cola vacia")
        else:
            valorDevolver = self.__arreglo[self.__primero]
            self.__arreglo[self.__primero] = 0
            self.__primero = (self.__primero+1)%(len(self.__arreglo))

            self.__cantidad -=1
        return valorDevolver
    
    def recorrer(self):
        for i in range(len(self.__arreglo)):
            print(self.Suprimir())