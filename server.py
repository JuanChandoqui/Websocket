import socket
import pickle

HOST = "127.0.0.1" #SERVER IP
PORT = 4321 #LISTENING PORT
HEADER = 10


#AF -> ADDRESS FAMILY 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    try:
        with connection:
            print(f'Connect to {address}: ')
            while True:
                data = connection.recv(HEADER)

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