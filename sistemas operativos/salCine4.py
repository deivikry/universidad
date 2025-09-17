import tkinter as tk
import threading
import time
import random

# Tamaño máximo de puestos (sillas disponibles en la sala de cine)
SALA_CINE = 5
buffer = []  # Buffer compartido (sillas disponibles)
lista_espera = []  # Lista de espera para clientes excedentes
empty = threading.Semaphore(SALA_CINE)  # Semáforo para espacios libres en el buffer
full = threading.Semaphore(0)  # Semáforo para espacios ocupados en el buffer
buffer_lock = threading.Lock()  # Bloqueo para acceso al buffer

# Crear ventana de tkinter
ventana = tk.Tk()
ventana.title(" sala de cine")
ventana.geometry("700x500")

# Canvas para representar las sillas en la interfaz gráfica
canvas = tk.Canvas(ventana, width=600, height=300, bg="white")
canvas.pack(pady=30)

# Etiqueta para mostrar la lista de espera
label_lista_espera = tk.Label(ventana, text="Lista de espera: []", font=("Arial", 12))
label_lista_espera.pack()

# Botones para realizar peticiones de clientes para ocupar la cilla
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)
boton1 = tk.Button(frame_botones, text="Petición Cliente 1", font=("Arial", 12), command=lambda: nueva_peticion("Cliente 1"))
boton1.grid(row=0, column=0, padx=10)
boton2 = tk.Button(frame_botones, text="Petición Cliente 2", font=("Arial", 12), command=lambda: nueva_peticion("Cliente 2"))
boton2.grid(row=0, column=1, padx=10)

# Lista para guardar las sillas representadas como rectángulos
rectangulos = []

# Crear las sillas (rectángulos) en la interfaz gráfica
for i in range(SALA_CINE):
    x1, y1 = 50 + i * 100, 100  # Posición inicial
    x2, y2 = x1 + 80, y1 + 150  # Tamaño del rectángulo
    rectangulo = canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
    rectangulos.append(rectangulo)

# Función para actualizar los colores de las sillas (rectángulos)
def actualizar_sillas():
    for i in range(SALA_CINE):
        if i < len(buffer):  # Espacios ocupados
            canvas.itemconfig(rectangulos[i], fill="red")
        else:  # Espacios libres
            canvas.itemconfig(rectangulos[i], fill="green")

# Función para actualizar la lista de espera en la interfaz gráfica
def actualizar_lista_espera():
    label_lista_espera.config(text=f"Lista de espera: {lista_espera}")
    ventana.update()

# Función para nueva petición de cliente
def nueva_peticion(cliente):
    if empty.acquire(blocking=False):  # Intentar ocupar una silla
        buffer_lock.acquire()  # Bloquear el acceso al buffer
        buffer.append(cliente)  # Agregar cliente al buffer (ocupando una silla)
        print(f"{cliente} ocupó una silla")
        actualizar_sillas()  # Actualizar colores en la interfaz gráfica
        buffer_lock.release()  # Liberar el acceso al buffer
        full.release()  # Incrementar espacios ocupados
        threading.Thread(target=uso_silla, args=(cliente,)).start()  # Hilo para uso de la silla
    else:
        # Si no hay sillas libres, pasar a la lista de espera
        lista_espera.append(cliente)
        print(f"{cliente} pasó a la lista de espera")
        actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica

# Función para gestionar el uso de una silla por un cliente
def uso_silla(cliente):
    time.sleep(random.uniform(2, 4))  # Tiempo de uso de la silla (simulado)
    buffer_lock.acquire()  # Bloquear el acceso al buffer
    buffer.remove(cliente)  # Liberar la silla ocupada por el cliente
    print(f"{cliente} liberó su silla")
    actualizar_sillas()  # Actualizar colores en la interfaz gráfica
    buffer_lock.release()  # Liberar el acceso al buffer
    empty.release()  # Incrementar espacios libres

    # Verificar si hay clientes en la lista de espera
    if lista_espera:
        nuevo_cliente = lista_espera.pop(0)  # Sacar el primer cliente de la lista de espera
        print(f"{nuevo_cliente} ocupó la silla liberada por {cliente}")
        actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica
        nueva_peticion(nuevo_cliente)  # Asignar la silla al cliente de la lista de espera

# Crear e iniciar hilos de salas para producir peticiones (simulado aquí como eventos automáticos)
ventana.mainloop()