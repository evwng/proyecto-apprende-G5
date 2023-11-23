class Tallerista:

    #CONSTRUCTOR
    def __init__(self,
                 fuente = "SuperProf",
                 contacto = None,
                 valoracion = None,
                 valoracion_cantidad = None,
                 nombre = None,
                 precio = None):
        self._fuente = fuente
        self._contacto = contacto
        self._valoracion = valoracion
        self._valoracion_cantidad = valoracion_cantidad
        self._nombre = nombre
        self._precio = precio

    #GETTERS
    def get_fuente(self):
        return self._fuente
    def get_contacto(self):
        return self._contacto
    def get_valoracion(self):
        return self._valoracion
    def get_valoracion_cantidad(self):
        return self._valoracion_cantidad
    def get_nombre(self):
        return self._nombre
    def get_precio(self):
        return self._precio

class Taller:

    #CONSTRUCTOR
    def __init__(self,
                 nombre = None,
                 lugar = "Providencia--Chile,-33.4314474,-70.6093325",
                 vacantes = None):
        self._nombre = nombre
        self._lugar = lugar
        self._vacantes = vacantes

    #GETTERS
    def get_lugar(self):
        return self._lugar