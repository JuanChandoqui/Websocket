from client import Client

HOST = "127.0.0.1" #SERVER IP
PORT = 4321 #LISTENING PORT
HEADER = 10
client = Client(HOST, PORT, HEADER)
client.sendMessage()