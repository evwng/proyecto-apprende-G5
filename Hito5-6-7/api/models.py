from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Tallerista(Base):
    __tablename__ = "Tallerista"
    id = Column(String, primary_key = True, index = True)
    nombre = Column(String)
    precio = Column(Integer)
    valoracion = Column(Float)
    valoracion_cantidad = Column(Integer)
    contacto = Column(String)
    fuente = Column(String)
    id_busqueda = Column(String, ForeignKey("Busqueda.id"))
    busqueda = relationship("Busqueda", back_populates = "resultados")

class Busqueda(Base):
    __tablename__ = "Busqueda"
    id = Column(String, primary_key = True, index = True)
    prompt = Column(String)
    resultados = relationship("Tallerista", back_populates = "busqueda")