import socket
import pickle

class Server:
    def __init__(self, HOST, PORT, HEADER):
        self.HOST = HOST
        self.PORT = PORT
        self.HEADER = HEADER

    def initializeServer(self):
        #AF -> ADDRESS FAMILY 
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.HOST, self.PORT))
            sock.listen(5)

            connection, address = sock.accept()
            try:
                print(f'Connect to {address}: ')
                while True:
                    data = connection.recv(self.HEADER)
                    if not data:
                        break
                    else:
                        newData = b''
                        newData += connection.recv(int(data))
                        dataDeserial = pickle.loads(newData)
                        print(dataDeserial)
                        print(type(dataDeserial))
                    sock.close()

            except KeyboardInterrupt:
                print("bye")
                break

            print('CLOSE CONNECTION')