from dominio import *
from busqueda import *

class Trabajador:

    #CONSTRUCTOR
    def __init__(self,
                 nombre = None,
                 busquedas = []):
        self._nombre = nombre
        self._busquedas = busquedas

    #CREAR BÚSQUEDA
    def crear_busqueda(self,
                       taller = Taller()):
        print("Nombra un taller:\n")
        prompt_usuario = input()
        print("\n")
        busqueda = Busqueda(prompt_usuario, taller)
        busqueda.buscar()
        self._busqueda.append(busqueda)
        return busqueda