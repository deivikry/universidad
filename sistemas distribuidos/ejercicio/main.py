#usar swagger ui para probar la API -con unicorn: uvicorn main:app --reload
#es donde se inicia la API
#importaciones de fastapi para crear la API
from fastapi import FastAPI, Depends, HTTPException, status

#importaciones de sqlalchemy para manejar la base de datos
from sqlalchemy.orm import Session

#importaciones de typing para manejar listas
from typing import List

#importaciones de los archivos
from database import get_db, engine
from models import tipo_id
from schemas import TipoIDCreate, TipoIDResponse
import models


#crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)    

app=FastAPI(title="API de Tipo de Identificación", description="API para gestionar tipos de identificación", version="1.0.0")

#crear un nuevo tipo de identificacion ID 
@app.post("/tipoid/", response_model=TipoIDResponse, status_code=status.HTTP_201_CREATED)
#funcion para crear un nuevo tipo de identificacion
def crear_tipoid(tipoid: TipoIDCreate, db: Session = Depends(get_db)):
    #verificar si el tipo de identificacion ya existe
    db_tipo=db.query(tipo_id).filter(tipo_id.id_tipoid == tipoid.id_tipoid).first()
    if db_tipo:
        raise HTTPException(
            status_code=400,
            detail="El tipo de identificación ya existe"
        )
    #crear el nuevo tipo de identificacion
    db_tipo = tipo_id(**tipoid.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo