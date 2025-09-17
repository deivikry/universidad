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
ventana.title("sala de cine")
ventana.geometry("700x500")

# Canvas para representar las sillas en la interfaz gráfica
canvas = tk.Canvas(ventana, width=600, height=300, bg="white")
canvas.pack(pady=20)

# Etiqueta para mostrar la lista de espera
label_lista_espera = tk.Label(ventana, text="Lista de espera: []", font=("Arial", 12))
label_lista_espera.pack()

# Botones para realizar peticiones de clientes
embotones = tk.Frame(ventana)
embotones.pack(pady=20)
boton1 = tk.Button(embotones, text="Petición Cliente 1", font=("Arial", 12), command=lambda: nueva_peticion("Cliente 1"))
boton1.grid(row=0, column=0, padx=10)
boton2 = tk.Button(embotones, text="Petición Cliente 2", font=("Arial", 12), command=lambda: nueva_peticion("Cliente 2"))
boton2.grid(row=0, column=1, padx=10)

# Lista para guardar las sillas representadas como rectángulos
rectangulos = []

# Crear las sillas (rectángulos) en la interfaz gráfica
for i in range(SALA_CINE):
    x1, y1 = 50 + i * 100, 100  # Posición inicial
    x2, y2 = x1 + 80, y1 + 150  # Tamaño del rectángulo
    rectangulo = canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
    rectangulos.append(rectangulo)

#  actualizar los colores de las sillas (rectángulos)
def actualizar_sillas():
    for i in range(SALA_CINE):
        if i < len(buffer):  # Espacios ocupados
            canvas.itemconfig(rectangulos[i], fill="red")
        else:  # Espacios libres
            canvas.itemconfig(rectangulos[i], fill="green")

#  actualizar la lista de espera en la interfaz gráfica
def actualizar_lista_espera():
    label_lista_espera.config(text=f"Lista de espera: {lista_espera}")
    ventana.update()

#  nueva petición de cliente
def nueva_peticion(cliente):
    if empty.acquire(blocking=False):  # Intentar ocupar una silla
        buffer_lock.acquire()  # Bloquear el acceso al buffer
        silla = len(buffer) + 1  # Obtener número de la silla ocupada
        buffer.append((cliente, silla))  # Agregar cliente y silla al buffer
        print(f"{cliente} ocupó la silla {silla}")
        actualizar_sillas()  # Actualizar colores en la interfaz gráfica
        buffer_lock.release()  # Liberar el acceso al buffer
        full.release()  # Incrementar espacios ocupados
        threading.Thread(target=uso_silla, args=(cliente, silla)).start()  # Hilo para uso de la silla
    else:
        # Si no hay sillas libres, pasar a la lista de espera
        lista_espera.append(cliente)
        print(f"{cliente} pasó a la lista de espera")
        actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica

#  gestionar el uso de una silla por un cliente
def uso_silla(cliente, silla):
    tiempo_uso = random.uniform(2, 4)  # Tiempo de uso de la silla (simulado)
    print(f"{cliente} está utilizando la silla {silla} durante {tiempo_uso:.2f} segundos")
    time.sleep(tiempo_uso)  # Simular tiempo de uso
    buffer_lock.acquire()  # Bloquear el acceso al buffer
    buffer.remove((cliente, silla))  # Liberar la silla ocupada por el cliente
    print(f"{cliente} liberó la silla {silla}")
    actualizar_sillas()  # Actualizar colores en la interfaz gráfica
    buffer_lock.release()  # Liberar el acceso al buffer
    empty.release()  # Incrementar espacios libres

    # Verificar si hay clientes en la lista de espera
    if lista_espera:
        nuevo_cliente = lista_espera.pop(0)  # Sacar el primer cliente de la lista de espera
        print(f"{nuevo_cliente} ocupó la silla {silla} liberada por {cliente}")
        actualizar_lista_espera()  # Actualizar la lista de espera en la interfaz gráfica
        nueva_peticion(nuevo_cliente)  # Asignar la silla al cliente de la lista de espera

#  generar clientes automáticamente
def generar_clientes():
    contador = 3  # Inicializar el contador para numerar a los clientes
    while True:
        cliente = f"Cliente {contador}"
        nueva_peticion(cliente)  # Crear una nueva petición automáticamente
        contador += 1
        time.sleep(random.uniform(2, 4))  # Intervalo aleatorio entre peticiones

# iniciar hilo para generación automática de clientes
threading.Thread(target=generar_clientes, daemon=True).start()


ventana.mainloop()