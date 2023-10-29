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

        #Talleristas
        talleristas = get_list_from_link(link)
        for link, nombre, precio, rating, rating_c in talleristas:
            tallerista = Tallerista(fuente = "SuperProf", contacto = "SuperProf.cl" + link, valoracion = rating, valoracion_cantidad = rating_c, nombre = nombre, precio = precio)
            self._resultados_talleristas.append(tallerista)
        
        #Insumos (no para esta entrega)

        #IMPRIMIR RESULTADOS
        print("Talleristas:\n")
        for tallerista in self._resultados_talleristas:
            print("Nombre: " + str(tallerista.get_nombre()))
            print("Valoración: " + str(tallerista.get_valoracion()) + " (" + str(tallerista.get_valoracion_cantidad()) + " opiniones)")
            print("Precio (hr): $" + str(tallerista.get_precio()))
            print("Contacto: " + str(tallerista.get_contacto()))
            print("\n")