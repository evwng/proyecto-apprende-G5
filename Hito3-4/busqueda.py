from datetime import datetime
from dominio import *
from scraper import *
from crear_link import *

class Busqueda:

    #CONSTRUCTOR
    def __init__(self,
                 busqueda,
                 taller = None,
                 resultados_talleristas = [],
                 resultados_insumos = [],
                 fecha = datetime.now()):
        self._busqueda = busqueda
        self._taller = taller
        self._resultados_talleristas = resultados_talleristas
        self._resultados_insumos = resultados_insumos
        self._fecha = fecha

    #GETTERS
    def get_busqueda(self):
        return self._busqueda
    def get_resultados_talleristas(self):
        return self._resultados_talleristas
    #def get_resultados_insumos(self):
    #    return self._resultados_insumos
    def get_fecha(self):
        return self._fecha

    #BÚSQUEDA
    def buscar(self):
        link = crear_link(self._busqueda, self._taller)

        talleristas = get_list_from_link(link) #Talleristas
        for link, nombre, precio in talleristas:
            tallerista = Tallerista()
            tallerista.set_contacto = link
            tallerista.set_nombre = nombre
            tallerista.set_precio = precio
            self._resultados_talleristas.append(tallerista)
        
        #Insumos (no para esta entrega)

        #IMPRIMIR RESULTADOS