import socket
import time
import pickle

HOST = "127.0.0.1"    #SERVER IP
PORT = 4321           #SENDING PORT
HEADER = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    names =  [100, 'MARIA', 'JUAN', '', 'RODRIGO']

    dataSerial = pickle.dumps(names)
    data_len = str(len(dataSerial))
    
    data = bytes(f'{data_len:<{HEADER}}', 'utf-8') + dataSerial
    print(data)
    s.send(data)
    time.sleep(1)

print('CLOSE CONNECTION')