from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

from uuid import uuid4

from crear_link import *
from scraper import *

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/busqueda", response_model = schemas.Busqueda)
def crear_busqueda(busqueda: schemas.Crear_Busqueda, db: Session = Depends(get_db)):

    db_busqueda = models.Busqueda(id = str(uuid4()), prompt = busqueda.prompt, resultados = [])

    #IMPORTANTE
    '''
    link = crear_link(busqueda.prompt)
    
    talleristas = get_list_from_link(link)
    '''

    #EJEMPLO (BORRAR)
    talleristas = [("Hola", "Juan", 3000, 5, 5), ("linnk", "Nombre", 34287, 3, 5)]
    
    for link, nombre, precio, valoracion, valoracion_cantidad in talleristas:
        db_tallerista = models.Tallerista(id = str(uuid4()),
                                          nombre = nombre,
                                          precio = precio,
                                          valoracion = valoracion,
                                          valoracion_cantidad = valoracion_cantidad,
                                          contacto = "SuperProf.cl" + link,
                                          fuente = "SuperProf.cl",
                                          id_busqueda = db_busqueda.id)
        db.add(db_tallerista)
        db.commit()
        db.refresh(db_tallerista)
        db_busqueda.resultados.append(db_tallerista)
    
    db.add(db_busqueda)
    db.commit()
    db.refresh(db_busqueda)

    return db_busqueda

@app.get("/busquedas", response_model = list[schemas.Busqueda])
def leer_busquedas(db: Session = Depends(get_db)):
    
    return db.query(models.Busqueda)

@app.get("/busqueda/{id}", response_model = schemas.Busqueda)
def leer_busqueda(id: str, db: Session = Depends(get_db)):

    busqueda = db.query(models.Busqueda).filter(models.Busqueda.id == id).first()

    if busqueda is None:
        raise HTTPException(status_code = 400, detail = "Búsqueda no encontrada")
    
    return busqueda