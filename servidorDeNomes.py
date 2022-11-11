from ctypes.wintypes import POINT
import socket
import random

PORT = 65432

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
DEFAULT_PORT = 5000
nomes = {
    "soma": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
    "produto": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
    "fatorial": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
    "primo": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
    "convert": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
    "horaCerta": [{"ip": "localhost", "port": DEFAULT_PORT}, {"ip": "127.0.0.1", "port": DEFAULT_PORT}],
}

def get_operation(message):
    return message.split('#')[0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Servidor rodando na portaaa ', PORT)
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            data = data.decode('utf-8')
            if not data:
                break
            if get_operation(data) == 'soma':
                random.shuffle(nomes['soma'])
                conn.sendall(str(nomes['soma']).encode())
            elif get_operation(data) == 'produto':
                random.shuffle(nomes['produto'])
                conn.sendall(str(nomes['produto']).encode())
            elif get_operation(data) == 'fatorial':
                random.shuffle(nomes['fatorial'])
                conn.sendall(str(nomes['fatorial']).encode())
            elif get_operation(data) == 'primo':
                random.shuffle(nomes['primo'])
                conn.sendall(str(nomes['primo']).encode())
            elif get_operation(data) == 'convert':
                random.shuffle(nomes['convert'])
                conn.sendall(str(nomes['convert']).encode())
            elif get_operation(data) == 'horaCerta':
                random.shuffle(nomes['horaCerta'])
                conn.sendall(str(nomes['horaCerta']).encode())