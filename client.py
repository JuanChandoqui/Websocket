import socket
import time
import pickle

class Client:
    def __init__(self, HOST, PORT, HEADER):
        self.HOST = HOST
        self.PORT = PORT
        self.HEADER = HEADER
        self.startConnection()

    def startConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def sendMessage(self):
        names =  [100, 'MARIA', 'JUAN', '', 'RODRIGO']   
        dataSerial = pickle.dumps(names)
        data_len = str(len(dataSerial))

        data = bytes(f'{data_len:<{self.HEADER}}', 'utf-8') + dataSerial
        print(data)
        self.s.send(data)
        time.sleep(1)
        
    def closeSocket(self):
        self.s.close()
        print('CLOSE CONNECTION')
        