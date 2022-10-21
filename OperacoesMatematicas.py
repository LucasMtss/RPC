import socket
import json
from FormatMessage import encode_message

cash = {}

def storageInCash(key, value):
    cash[key] = value

def searchInCash(key):
    try: 
        return cash[key]
    except:
        return None 

class OperacoesMatematicas:
    def __init__(self, ip='localhost', port=5000):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
    
    def getServerForOperation(self, operation):
        if searchInCash(operation):
            return searchInCash(operation)
        self.socket.sendall(operation.encode())
        data = self.socket.recv(1024)
        print('NOMES ',data.decode())
        storageInCash(operation, data.decode('utf-8').replace("'", '"'))
        return data.decode('utf-8').replace("'", '"')
    
    def soma(self, args):
        servidor = json.loads(self.getServerForOperation('soma'))
        message = encode_message('soma', args)

        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((servidor['ip'], servidor['port']))

        newSocket.sendall(message.encode())
        data = newSocket.recv(1024)
        newSocket.close()
        return data.decode('utf-8')

    def produto(self, args):
        servidor = json.loads(self.getServerForOperation('produto'))
        message = encode_message('produto', args)

        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((servidor['ip'], servidor['port']))

        newSocket.sendall(message.encode())
        data = newSocket.recv(1024)
        newSocket.close()
        return data.decode('utf-8')

    def fatorial(self, x):
        servidor = json.loads(self.getServerForOperation('fatorial'))
        message = encode_message('fatorial', [x])

        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((servidor['ip'], servidor['port']))

        newSocket.sendall(message.encode())
        data = newSocket.recv(1024)
        newSocket.close()
        return data.decode('utf-8')
    
    def numeroPrimo(self, x):
        servidor = json.loads(self.getServerForOperation('primo'))
        message = encode_message('primo', [x])

        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((servidor['ip'], servidor['port']))

        newSocket.sendall(message.encode())
        data = newSocket.recv(1024)
        newSocket.close()
        return data.decode('utf-8')

    def realDolar(self, x):
        servidor = json.loads(self.getServerForOperation('convert'))
        message = encode_message('convert', [x])

        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((servidor['ip'], servidor['port']))

        newSocket.sendall(message.encode())
        data = newSocket.recv(1024)
        newSocket.close()
        return data.decode('utf-8')
