import tkinter as tk
import threading
import random
import time

# Tamaño máximo de puestos (número de rectángulos)
SALA_CINE = 5
buffer = []  # Buffer compartido (sala de cine)
lista_espera = []  # Lista de espera para consumidores
empty = threading.Semaphore(SALA_CINE)  # Espacios vacíos disponibles en el buffer
full = threading.Semaphore(0)  # Elementos disponibles en el buffer
buffer_lock = threading.Lock()  # Bloqueo para acceso al buffer

# Crear ventana de tkinter
ventana = tk.Tk()
ventana.title("Simulación Sala - Persona Multitarea")
ventana.geometry("600x600")

# Canvas para mostrar los rectángulos
canvas = tk.Canvas(ventana, width=500, height=300, bg="white")
canvas.pack(pady=20)

# Etiqueta para mostrar la lista de espera
label_lista_espera = tk.Label(ventana, text="Lista de espera: []", font=("Arial", 12))
label_lista_espera.pack()

# Botones para consumidores
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

boton_persona_1 = tk.Button(frame_botones, text="Consumidor 1", font=("Arial", 12), command=lambda: consumir(1))
boton_persona_1.grid(row=0, column=0, padx=10)

boton_persona_2 = tk.Button(frame_botones, text="Consumidor 2", font=("Arial", 12), command=lambda: consumir(2))
boton_persona_2.grid(row=0, column=1, padx=10)

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

# Función para actualizar la lista de espera en la interfaz gráfica
def actualizar_lista_espera():
    label_lista_espera.config(text=f"Lista de espera: {lista_espera}")
    ventana.update()

# Función del sala (productor)
def sala(id):
    while True:
        item = random.randint(1, 50)  # Generar un puesto aleatorio

        if empty.acquire(blocking=False):  # Intentar adquirir un espacio en el buffer
            buffer_lock.acquire()  # Bloquear acceso al buffer
            buffer.append(item)  # Agregar puesto al buffer
            print(f"Sala {id} liberó puesto: {item}")
            actualizar_rectangulos()  # Actualizar colores en la interfaz gráfica
            buffer_lock.release()  # Liberar acceso al buffer
            full.release()  # Incrementar el semáforo de elementos disponibles
        else:
            # Si el buffer está lleno, añadir a la lista de espera
            lista_espera.append(item)
            print(f"Sala {id} añadió puesto {item} a la lista de espera")
            actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica

        time.sleep(random.uniform(2, 4))  # Simular tiempo de producción

# Función de consumidor activada por el botón
def consumir(id):
    if full.acquire(blocking=False):  # Intentar adquirir un espacio ocupado en el buffer
        buffer_lock.acquire()  # Bloquear acceso al buffer

        # Consumir del buffer principal
        puestos_tomados = []
        while buffer:  # Mientras haya elementos en el buffer
            item = buffer.pop(0)  # Retirar el primer elemento del buffer
            puestos_tomados.append(item)
            empty.release()  # Incrementar el semáforo de espacios vacíos

        print(f"Persona {id} tomó puestos: {puestos_tomados}")
        actualizar_rectangulos()  # Actualizar colores en la interfaz gráfica
        buffer_lock.release()  # Liberar acceso al buffer
    else:
        # Si no hay elementos en el buffer, agregar el consumidor a la lista de espera
        lista_espera.append(f"Consumidor {id}")
        print(f"Consumidor {id} añadido a la lista de espera")
        actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica

# Crear e iniciar hilos de sala
salaes = [threading.Thread(target=sala, args=(i,)) for i in range(2)]

for p in salaes:
    p.start()

# Ejecutar la ventana de tkinter
ventana.mainloop()