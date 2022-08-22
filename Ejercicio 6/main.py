from ColaSecuencial import ColaSecuencial
from ColaEncadena import ColaEncadenada

if __name__ == "__main__":
    NuevaCola = ColaEncadenada()
    NuevaCola.Suprimir()
    NuevaCola.Insertar(20)
    NuevaCola.Insertar(45)
    NuevaCola.Suprimir()
    NuevaCola.Insertar(15)
    NuevaCola.Insertar(260)
    NuevaCola.Insertar(30)
    NuevaCola.recorrer()