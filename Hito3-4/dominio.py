#Incluye sólo las clases y atributos relevantes para la entrega actual

class Tallerista:

    #CONSTRUCTOR
    def __init__(self,
                 fuente = "SuperProf",
                 contacto = None,
                 valoracion = None,
                 nombre = None,
                 precio = None):
        self._fuente = fuente
        self._contacto = contacto
        self._valoracion = valoracion
        self._nombre = nombre
        self._precio = precio
    
    #SETTERS
    def set_fuente(self, fuente):
        self._fuente = fuente
    def set_contacto(self, contacto):
        self._contacto = contacto
    def set_valoracion(self, valoracion):
        self._valoracion = valoracion
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_precio(self, precio):
        self._precio = precio

    #GETTERS
    def get_fuente(self):
        return self._fuente
    def get_contacto(self):
        return self._contacto
    def get_valoracion(self):
        return self._valoracion
    def get_nombre(self):
        return self._nombre
    def get_precio(self):
        return self._precio

class Taller:

    #CONSTRUCTOR
    def __init__(self,
                 lugar = "Providencia"):
        self._lugar = lugar
    
    #SETTERS
    def set_lugar(self, lugar):
        self._lugar = lugar

    #GETTERS
    def get_lugar(self):
        return self._lugar