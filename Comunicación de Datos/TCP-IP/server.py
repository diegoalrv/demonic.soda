import socket

HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto en el que el servidor escucha las conexiones

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Conexión establecida por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
