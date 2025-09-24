from sqlalchemy import Column, Integer, String
from database import Base

#definicion del modelo de la tabla tipoidprueba
class tipo_id(Base):
    __tablename__ = 'tipoidprueba'
    
    #definicion de las columnas de la tabla
    id_tipoid = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), nullable=False)