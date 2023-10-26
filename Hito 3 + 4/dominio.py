#HITO 3-4: SE PIDE IMPLEMENTAR LO NECESARIO PARA LA HISTORIA DE USUARIO QUE ENTREGA LISTADO DE TALLERISTAS

from busqueda import *

class Taller:
    
    #CONSTRUCTOR
    def __init__(self,
                 descripcion = None,
                 nombre = None,
                 tipo = None,
                 contenidos = [],
                 modalidad = "Presencial",
                 precio = None,
                 lugar = "Providencia",
                 vacantes = None,
                 fecha = None,
                 duracion = None,
                 coffee_break = None,
                 catering = None,
                 insumos = [],
                 talleristas = []):
        self._descripcion = descripcion
        self._nombre = nombre
        self._tipo = tipo
        self._contenidos = contenidos
        self._modalidad = modalidad
        self._precio = precio
        self._lugar = lugar
        self._vacantes = vacantes
        self._fecha = fecha
        self._duracion = duracion
        self._coffee_break = coffee_break
        self._catering = catering
        self._insumos = insumos
        self._talleristas = talleristas
    
    '''
    #SETTERS
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_tipo(self, tipo):
        self._tipo = tipo
    def set_contenidos(self, contenidos):
        self._contenidos = contenidos
    def set_modalidad(self, modalidad):
        self._modalidad = modalidad
    def get_precio(self, precio):
        self._precio = precio
    def set_lugar(self, lugar):
        self._lugar = lugar
    def set_vacantes(self, vacantes):
        self._vacantes = vacantes
    def set_fecha(self, fecha):
        self._fecha = fecha
    def set_duracion(self, duracion):
        self._duracion = duracion
    def set_coffee_break(self, coffee_break):
        self._coffee_break = coffee_break
    def set_catering(self, catering):
        self._catering = catering

    #GETTERS
    def get_descripcion(self):
        return self._descripcion
    def get_nombre(self):
        return self._nombre
    def get_tipo(self):
        return self._tipo
    def get_contenidos(self):
        return self._contenidos
    def get_modalidad(self):
        return self._modalidad
    def get_precio(self):
        return self._precio
    def get_lugar(self):
        return self._lugar
    def get_vacantes(self):
        return self._vacantes
    def get_fecha(self):
        return self._fecha
    def get_duracion(self):
        return self._duracion
    def get_coffee_break(self):
        return self._coffee_break
    def get_catering(self):
        return self._catering
    def get_insumos(self):
        return self._insumos
    def get_talleristas(self):
        return self._talleristas

    #AGREGAR INSUMO
    def add_insumo(self, insumo):
        self._insumos.append(insumo)
    #REMOVER INSUMO
    def remover_insumo(self, insumo):
    
    #AGREGAR TALLERISTA
    def agregar_tallerista(self, tallerista):
        self._talleristas.append(tallerista)
    #REMOVER TALLERISTA
    def remover_tallerista(self, tallerista):
        self._talleristas.remove(tallerista)
    '''

class Tallerista:

    #CONSTRUCTOR
    def __init__(self,
                 fuente = None,
                 contacto = None,
                 valoracion = None,
                 nombre = None,
                 profesion = None,
                 edad = None):
        self._fuente = fuente
        self._contacto = contacto
        self._valoracion = valoracion
        self._nombre = nombre
        self._profesion = profesion
        self._edad = edad
    
    #SETTERS
    def set_fuente(self, fuente):
        self._fuente = fuente
    def set_contacto(self, contacto):
        self._contacto = contacto
    def set_valoracion(self, valoracion):
        self._valoracion = valoracion
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_profesion(self, profesion):
        self._profesion = profesion
    def set_edad(self, edad):
        self._edad = edad

    #GETTERS
    def get_fuente(self):
        return self._fuente
    def get_contacto(self):
        return self._contacto
    def get_valoracion(self):
        return self._valoracion
    def get_nombre(self):
        return self._nombre
    def get_profesion(self):
        return self._profesion
    def get_edad(self):
        return self._edad
    
class Trabajador:

    #CONSTRUCTOR
    def __init__(self,
                 nombre = None,
                 busquedas = []):
        self._nombre = nombre
        self._busquedas = busquedas

    #CREAR BÚSQUEDA
    def crear_busqueda(self):
        busqueda = Busqueda()
        self._busquedas.append(busqueda)
        return busqueda

'''
class Insumo:
    
    #CONSTRUCTOR
    def __init__(self,
                 fuente = None,
                 nombre = None,
                 cantidad = None,
                 descripcion = None,
                 precio = None):
        self._fuente = fuente
        self._nombre = nombre
        self._cantidad = cantidad
        self._descripcion = descripcion
        self._precio = precio

class Asistente:

    #CONSTRUCTOR
    def __init__(self,
                 nombre = None,
                 edad = None,
                 profesion = None):
        self._nombre = nombre
        self._edad = edad
        self._profesion = profesion

'''