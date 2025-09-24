from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#informcion de la base de datos a la que nos conectaremos
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/claseSD"

#creacion del motor de la base de datos 
engine= create_engine(DATABASE_URL)

#creacion de la sesion de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creacion de la clase base para los modelos
Base = declarative_base()


#dependencia para obtener la sesion de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
# Prueba de conexión a la base de datos
# Este bloque se ejecuta solo si este archivo es el programa principal
if __name__ == "__main__":
    try:
        # Intenta conectar y obtener la versión de MySQL
        with engine.connect() as connection:
            result = connection.execute(text("SELECT VERSION()"))
            print("Conexión exitosa a la base de datos. Versión:", result.fetchone()[0])
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
