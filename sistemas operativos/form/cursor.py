# cursor.py
from conexion import obtener_conexion
from tkinter import messagebox

def insertar_factura(nombre, cantidad, precio, subtotal, total):
    conexion = obtener_conexion()
    if conexion is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO factura (nombre, cantidad, precio, subtotal, total)
            VALUES (%s, %s, %s, %s, %s)
        """
        datos = (nombre, cantidad, precio, subtotal, total)
        cursor.execute(consulta, datos)
        conexion.commit()
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar datos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
