import socket
host= "127.0.0.1"
port=65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    while True:
        mensaje = input("escriba un mensaje (o 'salir' para terminar): ")
        if mensaje.lower() == 'salir':
            print("Cerrando la conexion.")
            break
        s.sendall(mensaje.encode())
        data= s.recv(1024)
        print(f"respuesta del servidor: {data.decode()}")