from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#informcion de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost:3307/claseSD"
engine= create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
#dependencia para obtener la sesion de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()