#este archivo contiene los esquemas de pydantic para la validacion de datos y para manejar las respuestas

from pydantic import BaseModel
from typing import Optional

# preparacion de los esquemas
class TipoIDBase(BaseModel):
    id_tipoid :int
    descripcion: str
    
# esquema para crear un nuevo tipo de identificacion
class TipoIDCreate(TipoIDBase):
    pass
# esquema para actualizar un tipo de identificacion, esto me indica que hay respuestas cuando concsulto un tipo de identificacion
class TipoIDResponse(TipoIDBase):
    class Config:
        from_attributes = True
        
        
