import socket
import os
import time
import requests
import multiprocessing

from multiprocessing import Pool

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)

# number of cores
cores=multiprocessing.cpu_count()
cash = {}

def createKey(operation, args):
    return operation+str(args)

# check if number is prime
def is_prime(numero):
    contador = 0
    for num in range(1, int(numero) + 1):
        if numero % num == 0:
            contador += 1
    if contador == 2:
        return numero  # se for primo retorna verdadeiro
    return False

def storageInCash(key, value):
    cash[key] = value

def searchInCash(key):
    try: 
        return cash[key]
    except:
        return None 

def get_operation(message):
    return message.split('#')[0]

def get_args(message):
    return message.split('#')[1:]

def soma(args):
    if searchInCash(createKey('soma', args)):
        return searchInCash(createKey('soma', args))
    total = 0
    for num in args:
        total += float(num)
    storageInCash(createKey('soma', args), str(total))
    return str(total)

def produto(args):
    if searchInCash(createKey('produto', args)):
        return searchInCash(createKey('produto', args))
    total = 1
    for num in args:
        total *= float(num)
    storageInCash(createKey('produto', args), str(total))
    return str(total)

def fatorial(args):
    if searchInCash(createKey('fatorial',args[0])):
        return searchInCash(createKey('fatorial',args[0]))
    total = 1
    for num in range(1, int(args[0])+1):
        total *= num
    storageInCash(createKey('fatorial',args[0]), str(total))
    return str(total)

def numerosPrimos(args):
    if searchInCash(createKey('primos',args[0])):
        return searchInCash(createKey('primos',args[0]))
    # generate number list
    l = range(1, int(args[0])+1)
    # create process and execute function
    pool = Pool(processes=cores)
    resp = pool.map(is_prime, l)
    # finish process
    pool.close()
    storageInCash(createKey('primos',args[0]), str([number for number in resp if number != False]))
    return str([number for number in resp if number != False])

def realToDolar(args):
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    res = req.json()
    return str(float(args[0]) * float(res['USDBRL']['bid']))

def get_temp_diff(temp){
    print('TEMP', float(temp[0]))
    print('ATUAL', time.time())
    return time.time() - float(temp[0])
}


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('Servidor rodando na porta ', PORT)
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if not data:
            break
        if get_operation(data) == 'soma':
            conn.sendall(soma(get_args(data)).encode())
        elif get_operation(data) == 'produto':
            conn.sendall(produto(get_args(data)).encode())
        elif get_operation(data) == 'fatorial':
            conn.sendall(fatorial(get_args(data)).encode())
        elif get_operation(data) == 'primo':
            conn.sendall(numerosPrimos(get_args(data)).encode())
        elif get_operation(data) == 'convert':
            conn.sendall(realToDolar(get_args(data)).encode())
        elif get_operation(data) == 'horaCerta':
            conn.sendall(get_temp_diff(get_args(data)).encode())
    conn.close()
    s.close()
            


