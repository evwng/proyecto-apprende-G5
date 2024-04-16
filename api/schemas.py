from pydantic import BaseModel
from typing import List

#TALLERISTA
class Base_Tallerista(BaseModel):
    nombre: str
    precio: int
    valoracion: float
    valoracion_cantidad: int
    contacto: str
    contacto_estado: str
    fuente: str
class Crear_Tallerista(Base_Tallerista):
    pass
class Tallerista(Base_Tallerista):
    id: str
    id_busqueda: str
    class Config:
        from_attributes = True

#INSUMO
class Base_Insumo(BaseModel):
    nombre: str
    fuente: str
class Crear_Insumo(Base_Insumo):
    pass
class Insumo(Base_Insumo):
    id: str
    id_busqueda: str
    class Config:
        from_attributes = True

#BÚSQUEDA
class Base_Busqueda(BaseModel):
    prompt: str
class Crear_Busqueda(Base_Busqueda):
    pass
class Busqueda(Base_Busqueda):
    id: str
    resultados_talleristas: List[Tallerista] = []
    resultados_insumos: List[Insumo] = []
    class Config:
        from_attributes = True