from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

#TALLERISTA
class Tallerista(Base):
    __tablename__ = "Tallerista"
    id = Column(String, primary_key = True, index = True)
    nombre = Column(String)
    precio = Column(Integer)
    valoracion = Column(Float)
    valoracion_cantidad = Column(Integer)
    contacto_estado = Column(String)
    contacto = Column(String)
    fuente = Column(String)
    id_busqueda = Column(String, ForeignKey("Busqueda.id"))
    busqueda = relationship("Busqueda", back_populates = "resultados_talleristas")

#BÚSQUEDA
class Busqueda(Base):
    __tablename__ = "Busqueda"
    id = Column(String, primary_key = True, index = True)
    prompt = Column(String)
    resultados_talleristas = relationship("Tallerista", back_populates = "busqueda")

#PROPUESTA
class Propuesta(Base):
    __tablename__ = "Propuesta"
    id = Column(String, primary_key = True, index = True)
    descripcion = Column(String)
    modalidad = Column(String)
    numero_vacantes = Column(Integer)
    numero_sesiones = Column(Integer)
    id_tallerista = Column(String, ForeignKey("Tallerista.id"))