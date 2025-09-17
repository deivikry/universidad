import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")  # Título de la ventana

# Configurar el tamaño inicial de la ventana
ventana.geometry("400x300")  # Ancho x Alto

# Crear una etiqueta dentro de la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!", font=("Arial", 16))
etiqueta.pack(pady=20)  # Agregar la etiqueta con espaciado vertical

# Ejecutar el bucle principal para mostrar la ventana
ventana.mainloop()

