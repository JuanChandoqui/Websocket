import socket
import pickle


class Server:
    def __init__(self, HOST, PORT, HEADER):
        self.HOST = HOST
        self.PORT = PORT
        self.HEADER = HEADER
        # HOST = "127.0.0.1" #SERVER IP
        # PORT = 4321 #LISTENING PORT
        # HEADER = 10

    def initializeServer(self):
        #AF -> ADDRESS FAMILY 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            connection, address = s.accept()
            try:
                with connection:
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

            except KeyboardInterrupt:
                pass

        print('CLOSE CONNECTION')