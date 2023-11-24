from pydantic import BaseModel
from typing import List

#TALLERISTA
class Base_Tallerista(BaseModel):
    nombre: str
    precio: int
    valoracion: float
    valoracion_cantidad: int
    contacto: str
    fuente: str
class Crear_Tallerista(Base_Tallerista):
    pass
class Tallerista(Base_Tallerista):
    id: str
    id_busqueda: str
    class Config:
        orm_mode = True

#BÚSQUEDA
class Base_Busqueda(BaseModel):
    prompt: str
class Crear_Busqueda(Base_Busqueda):
    pass
class Busqueda(Base_Busqueda):
    id: str
    resultados: List[Tallerista] = []
    class Config:
        orm_mode = True