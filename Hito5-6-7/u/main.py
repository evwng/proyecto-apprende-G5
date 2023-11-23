'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#pip3 install fastapi
#pip3 install "uvicorn[standard]"
#python -m uvicorn u.main:app --reload
#http://localhost:8000/

@app.get("/")
async def root():
    return {"message": "Hello World"}
'''

'''
@app.get("/busquedas")
async def obtener_busquedas():
retorna lista de tallerista

@app.get("/busqueda/id")
async def obtener_busqueda():
retorna todas busquedas

@app.post("/busquedas")
async def crear_busqueda():
return id de la busqueda
'''

from pydantic import BaseModel
from typing import List
from itertools import count

class AutoIncrementID(BaseModel):
    _id_counter: int = 0

    @classmethod
    def _generate_id(cls):
        cls._id_counter += 1
        return cls._id_counter

class Tallerista(BaseModel, AutoIncrementID):

    nombre: str = ""
    precio: int = None
    valoracion: int = None
    valoracion_cantidad: int = None
    contacto: int = None
    fuente: str = "SuperProf"
    id: int = AutoIncrementID._generate_id()

class Taller(BaseModel):
    id: int #AUTOMATICO
    lugar: str = "Providencia--Chile,-33.4314474,-70.6093325"

class Busqueda(BaseModel):
    id: int #AUTOMATICO
    busqueda: str
    taller: Taller
    resultados: List[Tallerista] #LISTA DE IDS A LOS TALLERISTAS

###############
#BORRAR
###############

# Ejemplo de uso
emp1 = Tallerista()
emp2 = Tallerista()
emp3 = Tallerista()

print(emp1.id)