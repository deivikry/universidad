# conexion.py
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tienda"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None
