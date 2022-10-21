from ctypes.wintypes import POINT
import socket
import random

PORT = 65432

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
DEFAULT_PORT = 5000
nomes = {
    "soma": [{"ip": "localhost", "port": DEFAULT_PORT}],
    "produto": [{"ip": "localhost", "port": DEFAULT_PORT}],
    "fatorial": [{"ip": "10.3.1.18", "port": DEFAULT_PORT}],
    "primo": [{"ip": "10.3.1.18", "port": DEFAULT_PORT}],
    "convert": [{"ip": "10.3.1.18", "port": DEFAULT_PORT}],
}

def get_operation(message):
    return message.split('#')[0]

def generateRandomIndex(listLength):
    return random.randint(0,listLength-1)

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
                conn.sendall(str(nomes['soma'][generateRandomIndex(len(nomes['soma']))]).encode())
            elif get_operation(data) == 'produto':
                conn.sendall(str(nomes['produto'][generateRandomIndex(len(nomes['produto']))]).encode())
            elif get_operation(data) == 'fatorial':
                conn.sendall(str(nomes['fatorial'][generateRandomIndex(len(nomes['fatorial']))]).encode())
            elif get_operation(data) == 'primo':
                conn.sendall(str(nomes['primo'][generateRandomIndex(len(nomes['primo']))]).encode())
            elif get_operation(data) == 'convert':
                conn.sendall(str(nomes['convert'][generateRandomIndex(len(nomes['convert']))]).encode())