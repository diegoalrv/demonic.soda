import socket

HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto en el que el servidor escucha las conexiones

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola, mundo')
    data = s.recv(1024)

print('Recibido', repr(data))
