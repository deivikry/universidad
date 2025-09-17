import tkinter as tk
import threading
import random
import time

# Tamaño máximo de puestos (número de rectángulos)
SALA_CINE = 5
buffer = []  # Buffer compartido
empty = threading.Semaphore(SALA_CINE)  # Espacios vacíos disponibles
full = threading.Semaphore(0)  # Elementos disponibles en el buffer
buffer_lock = threading.Lock()  # Bloqueo para acceso al buffer

# Crear ventana de tkinter
ventana = tk.Tk()
ventana.title("Simulación Sala - Persona")
ventana.geometry("600x400")

# Canvas para mostrar los rectángulos
canvas = tk.Canvas(ventana, width=500, height=300, bg="white")
canvas.pack(pady=20)

# Lista para guardar los rectángulos
rectangulos = []

# Crear rectángulos inicialmente libres
for i in range(SALA_CINE):
    x1, y1 = 50 + i * 80, 100  # Posición inicial
    x2, y2 = x1 + 60, y1 + 100  # Tamaño del rectángulo
    rectangulo = canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
    rectangulos.append(rectangulo)

# Función para actualizar los colores de los rectángulos
def actualizar_rectangulos():
    for i in range(SALA_CINE):
        if i < len(buffer):  # Espacios ocupados
            canvas.itemconfig(rectangulos[i], fill="red")
        else:  # Espacios libres
            canvas.itemconfig(rectangulos[i], fill="green")

# Función del sala (productor)
def sala(id):
    while True:
        item = random.randint(1, 50)  # Generar un puesto aleatorio
        empty.acquire()  # Esperar espacio en el buffer
        buffer_lock.acquire()  # Bloquear acceso al buffer
        buffer.append(item)  # Agregar puesto al buffer
        print(f"Sala {id} liberó puesto: {item}")
        actualizar_rectangulos()  # Actualizar colores en la interfaz gráfica
        buffer_lock.release()  # Liberar acceso al buffer
        full.release()  # Incrementar el semáforo de elementos disponibles
        time.sleep(random.uniform(2, 4))  # Simular tiempo de producción

# Función de persona (consumidor)
def persona(id):
    while True:
        full.acquire()  # Esperar a que haya elementos en el buffer
        buffer_lock.acquire()  # Bloquear acceso al buffer

        # Tomar todos los elementos disponibles en el buffer
        puestos_tomados = []
        while buffer:  # Mientras haya elementos en el buffer
            item = buffer.pop(0)  # Retirar el primer elemento del buffer
            puestos_tomados.append(item)
            empty.release()  # Incrementar el semáforo de espacios vacíos

        print(f"Persona {id} tomó puestos: {puestos_tomados}")
        actualizar_rectangulos()  # Actualizar colores en la interfaz gráfica
        buffer_lock.release()  # Liberar acceso al buffer
        time.sleep(random.uniform(4, 8))  # Simular tiempo de consumo

# Crear e iniciar hilos de sala y persona
salaes = [threading.Thread(target=sala, args=(i,)) for i in range(2)]
personaes = [threading.Thread(target=persona, args=(i,)) for i in range(2)]

for p in salaes:
    p.start()
for c in personaes:
    c.start()

# Ejecutar la ventana de tkinter
ventana.mainloop()