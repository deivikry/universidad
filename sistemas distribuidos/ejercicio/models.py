from sqlalchemy import Column, Integer, String
from database import Base

class tipoi_d(Base):
    __tablename__ = 'tipoid'
    
    id_tipoid = Column(Integer(11), primary_key=True, index=True)
    descripcion = Column(String(100), nullable=False)