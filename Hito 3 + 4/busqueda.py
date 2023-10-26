#HITO 3-4: SE PIDE IMPLEMENTAR LO NECESARIO PARA LA HISTORIA DE USUARIO QUE ENTREGA LISTADO DE TALLERISTAS

import datetime

class Busqueda:

    #CONSTRUCTOR
    def __init__(self,
                 busqueda = None,
                 resultados_talleristas = [],
                 resultados_insumos = [],
                 fecha = datetime.now()):
        self._busqueda = busqueda
        self._resultados_talleristas = resultados_talleristas
        self._resultados_insumos = resultados_insumos
        self._fecha = fecha
    
    #SETTERS
    def set_busqueda(self, busqueda):
        self._busqueda = busqueda
    def set_resultados_talleristas(self, resultados_talleristas):
        self._resultados_talleristas = resultados_talleristas
    #def set_resultados_insumos(self, resultados_insumos):
    #    self._resultados_insumos = resultados_insumos
    def set_fecha(self, fecha):
        self._fecha = fecha

    #AGREGAR TALLERISTA
    #def agregar_tallerista(self, tallerista):
    #    self._resultados_talleristas.append(tallerista)

    #AGREGAR INSUMO
    #def agregar_insumo(self, insumo):
    #    self._resultados_insumos.append(insumo)

    #GETTERS
    def get_busqueda(self):
        return self._busqueda
    def get_resultados_talleristas(self):
        return self._resultados_talleristas
    #def get_resultados_insumos(self):
    #    return self._resultados_insumos
    def get_fecha(self):
        return self._fecha
    
    #INICIAR BÚSQUEDA
    def iniciar_busqueda():
        prompt_usuario = input()
