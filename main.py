from server import Server

if __name__ == "__main__":
    HOST = "127.0.0.1" #SERVER IP
    PORT = 4321 #LISTENING PORT
    HEADER = 10
    server = Server(HOST, PORT, HEADER)

    print('START SERVER')
    server.initializeServer()