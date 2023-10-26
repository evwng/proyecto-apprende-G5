class Taller:
    
    #CONSTRUCTOR
    def __init__(self,
                 descripcion,
                 nombre = "",
                 tipo = "Taller USM",
                 contenidos = "",
                 modalidad = "Presencial",
                 precio = "",
                 lugar = ",Providencia",
                 vacantes = "",
                 fecha = "",
                 hora = "",
                 duracion = "1 hora",
                 coffee_break = "No",
                 catering = "No"):
        self._descripcion = descripcion
        self._nombre = nombre
        self._tipo = tipo
        self._contenidos = contenidos
        self._modalidad = modalidad
        self._precio = precio
        self._lugar = lugar
        self._vacantes = vacantes
        self._fecha = fecha
        self._hora = hora
        self._duracion = duracion
        self._coffee_break = coffee_break
        self._catering = catering
    
    #NOMBRE
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre

    #TIPO
    def set_tipo(self, tipo):
        self._tipo = tipo
    def get_tipo(self):
        return self._tipo

    #DESCRIPCION
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    def get_descripcion(self):
        return self._descripcion

    #REPETIR SET Y GET PARA LOS OTROS ATRIBUTOS

class Tallerista:

    #CONSTRUCTOR
    def __init__(self, fuente, contacto, valoracion, nombre, profesion="", edad=-1):
        self._fuente = fuente
        self._contacto = contacto
        self._valoracion = valoracion
        self._nombre = nombre
        self._profesion = profesion
        self._edad = edad

class Insumo(Taller): #Insumo es subtipo de Taller
    
    #CONSTRUCTOR
    def __init__(self, fuente, nombre, cantidad, descripcion="", precio=-1):
        self._fuente = fuente
        self._nombre = nombre
        self._cantidad = cantidad
        self._descripcion = descripcion
        self._precio = precio
    
    #NOMBRE
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre

    #CANTIDAD
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    def get_cantidad(self):
        return self._cantidad

    #REPETIR SET Y GET PARA OTROS ATRIBUTOS

#class Trabajador:

#class Asistente: